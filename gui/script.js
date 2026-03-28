const FIREBASE_URL = "https://sysc3010-l1-g9-demo-default-rtdb.firebaseio.com";

let climateChart;
const activityLog = [];

function latestChild(obj) {
  if (!obj || typeof obj !== "object") return null;
  const keys = Object.keys(obj);
  if (keys.length === 0) return null;
  return obj[keys[keys.length - 1]];
}

function formatUnixTs(ts) {
  if (!ts) return "--";
  return new Date(Number(ts) * 1000).toLocaleString();
}

function setConnection(ok, text) {
  const dot = document.getElementById("connDot");
  const textEl = document.getElementById("connText");
  dot.className = "dot " + (ok ? "ok" : "err");
  textEl.textContent = text;
  document.getElementById("logsConnectionMirror").textContent = text;
  document.getElementById("firebaseConnMirror").textContent = text;
}

function setStatus(el, text, cls) {
  el.textContent = text;
  el.className = "status-pill " + cls;
}

function tempStatus(temp) {
  if (temp == null) return ["Status: No Data", "critical"];
  if (temp > 35) return ["Status: Critical", "critical"];
  if (temp > 28) return ["Status: Warning", "warning"];
  return ["Status: Optimal", "optimal"];
}

function humidityStatus(h) {
  if (h == null) return ["Status: No Data", "critical"];
  if (h < 30 || h > 80) return ["Status: Warning", "warning"];
  return ["Status: Optimal", "optimal"];
}

function soilStatus(m) {
  if (m == null) return ["Status: Waiting for Node 2", "critical"];
  if (m < 30) return ["Status: Critical", "critical"];
  if (m < 45) return ["Status: Warning", "warning"];
  return ["Status: Optimal", "optimal"];
}

function addActivity(message) {
  const time = new Date().toLocaleTimeString();
  activityLog.unshift(`[${time}] ${message}`);
  if (activityLog.length > 8) activityLog.pop();

  const feed = document.getElementById("activityFeed");
  feed.innerHTML = "";
  activityLog.forEach(item => {
    const div = document.createElement("div");
    div.className = "feed-item";
    div.textContent = item;
    feed.appendChild(div);
  });
}

async function fetchJson(path) {
  const res = await fetch(`${FIREBASE_URL}${path}.json`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return await res.json();
}

function initChart() {
  const ctx = document.getElementById("climateChart").getContext("2d");
  climateChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: [],
      datasets: [
        {
          label: "Temperature (°C)",
          data: [],
          borderColor: "#59a7ea",
          backgroundColor: "rgba(89,167,234,0.12)",
          tension: 0.35,
          fill: true
        },
        {
          label: "Humidity (%)",
          data: [],
          borderColor: "#37a861",
          backgroundColor: "rgba(55,168,97,0.10)",
          tension: 0.35,
          fill: true
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          labels: { color: "#eef4fb" }
        }
      },
      scales: {
        x: {
          ticks: { color: "#a9b4c3" },
          grid: { color: "#2d3a49" }
        },
        y: {
          ticks: { color: "#a9b4c3" },
          grid: { color: "#2d3a49" }
        }
      }
    }
  });
}

function updateChart(temp, hum) {
  if (temp == null && hum == null) return;

  const label = new Date().toLocaleTimeString();
  climateChart.data.labels.push(label);
  climateChart.data.datasets[0].data.push(temp);
  climateChart.data.datasets[1].data.push(hum);

  if (climateChart.data.labels.length > 8) {
    climateChart.data.labels.shift();
    climateChart.data.datasets[0].data.shift();
    climateChart.data.datasets[1].data.shift();
  }

  climateChart.update();
}

async function refreshDashboard() {
  try {
    const [climateData, irrigationData, overrideData, healthData] = await Promise.all([
      fetchJson("/nodes/node1/climate"),
      fetchJson("/nodes/node2/irrigation"),
      fetchJson("/commands/override"),
      fetchJson("/nodes/node3/health")
    ]);

    const climate = latestChild(climateData);
    const irrigation = latestChild(irrigationData);
    const health = latestChild(healthData);

    const temp = climate?.temperature_c ?? null;
    const hum = climate?.humidity_pct ?? null;
    const soil = irrigation?.soil_moisture_pct ?? null;
    const light = health?.light_level ?? null;

    document.getElementById("tempValue").innerHTML =
      temp != null ? `${Number(temp).toFixed(1)}<span class="unit">°C</span>` : `--<span class="unit">°C</span>`;
    const [tempLabel, tempClass] = tempStatus(temp);
    setStatus(document.getElementById("tempStatus"), tempLabel, tempClass);

    document.getElementById("humValue").innerHTML =
      hum != null ? `${Math.round(Number(hum))}<span class="unit">%</span>` : `--<span class="unit">%</span>`;
    const [humLabel, humClass] = humidityStatus(hum);
    setStatus(document.getElementById("humStatus"), humLabel, humClass);

    document.getElementById("soilValue").innerHTML =
      soil != null ? `${Math.round(Number(soil))}<span class="unit">%</span>` : `--<span class="unit">%</span>`;
    const [soilLabel, soilClass] = soilStatus(soil);
    setStatus(document.getElementById("soilStatus"), soilLabel, soilClass);

    let pumpOn = false;
    if (irrigation && typeof irrigation.pump_status === "string") {
      pumpOn = irrigation.pump_status.toUpperCase() === "ON";
    } else if (overrideData && typeof overrideData.pump_enable === "boolean") {
      pumpOn = overrideData.pump_enable;
    }

    document.getElementById("pumpToggle").checked = pumpOn;
    setStatus(
      document.getElementById("pumpStatusText"),
      pumpOn ? "Irrigation System Active" : "Irrigation System Inactive",
      pumpOn ? "optimal" : "warning"
    );

    document.getElementById("climateTempDetail").textContent = temp != null ? `${temp} °C` : "--";
    document.getElementById("climateHumDetail").textContent = hum != null ? `${hum} %` : "--";
    document.getElementById("climateTs").textContent = formatUnixTs(climate?.ts);
    document.getElementById("climateSource").textContent = climate?.source || "--";

    document.getElementById("irrigationSoilDetail").textContent = soil != null ? `${soil} %` : "--";
    document.getElementById("irrigationPumpDetail").textContent = pumpOn ? "Pump ON" : "Pump OFF";
    document.getElementById("irrigationTs").textContent = formatUnixTs(irrigation?.ts);
    document.getElementById("overrideState").textContent =
      typeof overrideData?.pump_enable === "boolean"
        ? (overrideData.pump_enable ? "Pump ON" : "Pump OFF")
        : "--";

    document.getElementById("lightLevelValue").textContent = light != null ? `${light}` : "--";
    document.getElementById("lightLevelStatus").textContent =
      light != null ? "Node 3 data available" : "Waiting for Node 3";

    const nowStr = new Date().toLocaleTimeString();
    const source = climate?.source || irrigation?.source || overrideData?.source || "--";

    document.getElementById("lastUpdated").textContent = nowStr;
    document.getElementById("sourceInfo").textContent = source;
    document.getElementById("overrideSource").textContent = overrideData?.source || "--";
    document.getElementById("logsUpdatedMirror").textContent = nowStr;
    document.getElementById("firebaseRefreshMirror").textContent = nowStr;
    document.getElementById("firebaseSourceMirror").textContent = source;

    const msg = "Dashboard updated successfully.";
    document.getElementById("messageBox").textContent = msg;
    document.getElementById("logsMessageMirror").textContent = msg;

    setConnection(true, "Connected to Firebase");
    updateChart(temp, hum);
    addActivity(`Temp=${temp ?? "--"}°C, Hum=${hum ?? "--"}%, Soil=${soil ?? "--"}%, Pump=${pumpOn ? "ON" : "OFF"}`);
  } catch (err) {
    const msg = "Dashboard refresh error: " + err.message;
    document.getElementById("messageBox").textContent = msg;
    document.getElementById("logsMessageMirror").textContent = msg;
    setConnection(false, "Firebase connection error");
    addActivity(`Refresh failed: ${err.message}`);
  }
}

async function sendOverride(state) {
  const payload = {
    ts: Math.floor(Date.now() / 1000),
    pump_enable: state,
    source: "gui_operator"
  };

  try {
    const res = await fetch(`${FIREBASE_URL}/commands/override.json`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const msg = `Success: Pump commanded ${state ? "ON" : "OFF"}.`;
    document.getElementById("messageBox").textContent = msg;
    document.getElementById("logsMessageMirror").textContent = msg;
    addActivity(`Manual override sent: ${state ? "Pump ON" : "Pump OFF"}`);
    await refreshDashboard();
  } catch (err) {
    const msg = "Error sending command: " + err.message;
    document.getElementById("messageBox").textContent = msg;
    document.getElementById("logsMessageMirror").textContent = msg;
    addActivity(`Override failed: ${err.message}`);
  }
}

function setupTabs() {
  const buttons = document.querySelectorAll(".nav-item[data-tab]");
  const sections = document.querySelectorAll(".tab-section");

  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      const target = btn.dataset.tab;

      buttons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      sections.forEach(sec => sec.classList.add("hidden"));
      document.getElementById(`tab-${target}`).classList.remove("hidden");
    });
  });
}

setupTabs();
initChart();
refreshDashboard();
setInterval(refreshDashboard, 4000);

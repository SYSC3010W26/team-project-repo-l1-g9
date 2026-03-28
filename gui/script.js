const FIREBASE_URL = "https://sysc3010-l1-g9-demo-default-rtdb.firebaseio.com";

let climateChart;
const activityLog = [];

// -----------------------------
// Helpers
// -----------------------------
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

function setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

function setHTML(id, value) {
  const el = document.getElementById(id);
  if (el) el.innerHTML = value;
}

function setConnection(ok, text) {
  const dot = document.getElementById("connDot");
  const textEl = document.getElementById("connText");

  if (dot) dot.className = "dot " + (ok ? "ok" : "err");
  if (textEl) textEl.textContent = text;

  setText("logsConnectionMirror", text);
  setText("firebaseConnMirror", text);
}

function setStatus(el, text, cls) {
  if (!el) return;
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
  if (!feed) return;

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

// -----------------------------
// Chart
// -----------------------------
function initChart() {
  const canvas = document.getElementById("climateChart");
  if (!canvas) return;

  const ctx = canvas.getContext("2d");
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
  if (!climateChart) return;
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

// -----------------------------
// Main refresh
// -----------------------------
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

    // Dashboard cards
    setHTML(
      "tempValue",
      temp != null ? `${Number(temp).toFixed(1)}<span class="unit">°C</span>` : `--<span class="unit">°C</span>`
    );
    const [tempLabel, tempClass] = tempStatus(temp);
    setStatus(document.getElementById("tempStatus"), tempLabel, tempClass);

    setHTML(
      "humValue",
      hum != null ? `${Math.round(Number(hum))}<span class="unit">%</span>` : `--<span class="unit">%</span>`
    );
    const [humLabel, humClass] = humidityStatus(hum);
    setStatus(document.getElementById("humStatus"), humLabel, humClass);

    setHTML(
      "soilValue",
      soil != null ? `${Math.round(Number(soil))}<span class="unit">%</span>` : `--<span class="unit">%</span>`
    );
    const [soilLabel, soilClass] = soilStatus(soil);
    setStatus(document.getElementById("soilStatus"), soilLabel, soilClass);

    // Pump state
    let pumpOn = false;
    if (irrigation && typeof irrigation.pump_status === "string") {
      pumpOn = irrigation.pump_status.toUpperCase() === "ON";
    } else if (overrideData && typeof overrideData.pump_enable === "boolean") {
      pumpOn = overrideData.pump_enable;
    }

    const pumpToggle = document.getElementById("pumpToggle");
    if (pumpToggle) pumpToggle.checked = pumpOn;

    setStatus(
      document.getElementById("pumpStatusText"),
      pumpOn ? "Irrigation System Active" : "Irrigation System Inactive",
      pumpOn ? "optimal" : "warning"
    );

    // Climate tab
    setText("climateTempDetail", temp != null ? `${temp} °C` : "--");
    setText("climateHumDetail", hum != null ? `${hum} %` : "--");
    setText("climateTs", formatUnixTs(climate?.ts));
    setText("climateSource", climate?.source || "--");

    // Irrigation tab
    setText("irrigationSoilDetail", soil != null ? `${soil} %` : "--");
    setText("irrigationPumpDetail", pumpOn ? "Pump ON" : "Pump OFF");
    setText("irrigationTs", formatUnixTs(irrigation?.ts));
    setText(
      "overrideState",
      typeof overrideData?.pump_enable === "boolean"
        ? (overrideData.pump_enable ? "Pump ON" : "Pump OFF")
        : "--"
    );

    // Health tab
    setText("lightLevelValue", light != null ? `${light}` : "--");
    setText("lightLevelStatus", light != null ? "Node 3 data available" : "Waiting for Node 3");

    // Shared info
    const nowStr = new Date().toLocaleTimeString();
    const source = climate?.source || irrigation?.source || overrideData?.source || "--";

    setText("lastUpdated", nowStr);
    setText("sourceInfo", source);
    setText("overrideSource", overrideData?.source || "--");
    setText("logsUpdatedMirror", nowStr);
    setText("firebaseRefreshMirror", nowStr);
    setText("firebaseSourceMirror", source);

    const overrideStateText =
      typeof overrideData?.pump_enable === "boolean"
        ? (overrideData.pump_enable ? "Pump ON" : "Pump OFF")
        : "--";

    setText("overrideStateMirror", overrideStateText);

    const msg = "Dashboard updated successfully.";
    setText("messageBox", msg);
    setText("logsMessageMirror", msg);

    // Raw Firebase viewer
    setText(
      "rawClimate",
      climate ? JSON.stringify(climate, null, 2) : "No climate data found"
    );
    setText(
      "rawIrrigation",
      irrigation ? JSON.stringify(irrigation, null, 2) : "No irrigation data found"
    );
    setText(
      "rawHealth",
      health ? JSON.stringify(health, null, 2) : "No health data found"
    );
    setText(
      "rawOverride",
      overrideData ? JSON.stringify(overrideData, null, 2) : "No override data found"
    );

    setConnection(true, "Connected to Firebase");
    updateChart(temp, hum);
    addActivity(`Temp=${temp ?? "--"}°C, Hum=${hum ?? "--"}%, Soil=${soil ?? "--"}%, Pump=${pumpOn ? "ON" : "OFF"}`);
  } catch (err) {
    const msg = "Dashboard refresh error: " + err.message;
    setText("messageBox", msg);
    setText("logsMessageMirror", msg);
    setConnection(false, "Firebase connection error");
    addActivity(`Refresh failed: ${err.message}`);

    setText("rawClimate", "Error loading climate data");
    setText("rawIrrigation", "Error loading irrigation data");
    setText("rawHealth", "Error loading health data");
    setText("rawOverride", "Error loading override data");
  }
}

// -----------------------------
// Override command
// -----------------------------
async function sendOverride(state) {
  const sendingMsg = "Sending override command...";
  setText("messageBox", sendingMsg);
  setText("logsMessageMirror", sendingMsg);

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
    setText("messageBox", msg);
    setText("logsMessageMirror", msg);
    addActivity(`Manual override sent: ${state ? "Pump ON" : "Pump OFF"}`);
    await refreshDashboard();
  } catch (err) {
    const msg = "Error sending command: " + err.message;
    setText("messageBox", msg);
    setText("logsMessageMirror", msg);
    addActivity(`Override failed: ${err.message}`);
  }
}

// -----------------------------
// Tabs
// -----------------------------
function setupTabs() {
  const buttons = document.querySelectorAll(".nav-item[data-tab]");
  const sections = document.querySelectorAll(".tab-section");

  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      const target = btn.dataset.tab;

      buttons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      sections.forEach(sec => sec.classList.add("hidden"));

      const targetSection = document.getElementById(`tab-${target}`);
      if (targetSection) {
        targetSection.classList.remove("hidden");
      }
    });
  });
}

// -----------------------------
// Init
// -----------------------------
setupTabs();
initChart();
refreshDashboard();
setInterval(refreshDashboard, 4000);

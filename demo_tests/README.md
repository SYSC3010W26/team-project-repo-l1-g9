# demo_tests (SYSC3010 Comms Demo)

## Setup (run once per terminal)
cd ~/team-project-repo-l1-g9
source .venv/bin/activate
source demo_tests/env.sh

## Demo scripts (run in separate terminals)
### Esteban (Node1 -> Firebase)
python3 demo_tests/node1_firebase_publish.py

### Karthikeyan (Firebase -> Node4 -> SQLite)
python3 demo_tests/node4_firebase_to_sqlite.py

### Karthikeyan (SQLite auto-view)
python3 demo_tests/show_sqlite_tail.py

### Kezi (GUI -> Firebase override)
python3 demo_tests/gui_publish_override.py

### Vlad (Firebase override -> Node2 receive)
python3 demo_tests/node2_poll_override.py

## Optional backup links
python3 demo_tests/node2_uart_read.py
python3 demo_tests/node4_flask_status_poll.py

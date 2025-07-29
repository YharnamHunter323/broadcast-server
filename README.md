# 🛰️ Broadcast Server (Python CLI WebSocket Chat)

A simple command-line WebSocket broadcast server and client built with Python. This project demonstrates real-time communication between multiple clients using WebSockets — perfect for learning how chat apps, live feeds, or multiplayer games sync data.

https://roadmap.sh/projects/broadcast-server

---

## 📦 Features

- CLI interface to start a server or connect as a client
- Broadcast messages to all connected clients
- Handles multiple clients and disconnections gracefully
- Works entirely via terminal (no GUI)
- No cloud setup required — runs locally

---

## 📁 Project Structure

broadcast-server/
├── broadcast_server/
│ ├── init.py
│ ├── server.py
│ ├── client.py
│ └── cli.py
├── requirements.txt
├── .gitignore
└── README.md

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.7+
- `pip` installed

### 🔧 Installation

#### 1. Clone the repository

```bash
git clone <your-repo-url>
cd broadcast-server
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### Usage

### Start the Server

```bash
python -m broadcast_server.cli start
```

### Connect as a Client

Open a new terminal:

```bash
python -m broadcast_server.cli connect
```

Type messages to broadcast to all other clients.

### CLI Command Summary

Command Description
start [--host] [--port] Start the broadcast server
connect [--host] [--port] Connect as a client to the server

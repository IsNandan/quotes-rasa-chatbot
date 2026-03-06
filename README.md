# Quotes Recommendation Chatbot (Rasa NLU)

A Rasa-based conversational chatbot that recommends meaningful quotes based on user intent, category, and emotional cues.

## What This Project Does
- Understands user messages using Rasa NLU.
- Recommends quotes in categories: `inspiration`, `motivation`, `success`, `love`, `humor`.
- Uses emotion-to-category mapping (example: `sad -> inspiration`, `stressed -> motivation`).
- Asks follow-up feedback (`Did this help?`) for engagement.
- Supports browser chat via Rasa REST API.

## Tech Stack
- Rasa Open Source `3.6.20`
- Rasa SDK `3.6.2`
- Python `3.10` (required for this Rasa version)

## Project Structure
```text
.
├── Makefile
├── actions/
│   ├── __init__.py
│   └── actions.py
├── data/
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
├── frontend/
│   ├── app.js
│   ├── index.html
│   └── style.css
├── tests/
│   └── test_stories.yml
├── config.yml
├── credentials.yml
├── domain.yml
├── endpoints.yml
├── requirements.txt
├── scripts/
│   └── smoke_test.sh
└── README.md
```

## Prerequisites
- OS: Ubuntu/WSL/Linux
- Python: `3.10.x`
- `pip` and `venv`

Important:
- Rasa `3.6.x` does **not** support Python `3.11+` or `3.12`.
- If your default Python is `3.12`, install and use Python `3.10` specifically.

## 1. Install Python 3.10 (If Not Installed)
```bash
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.10 python3.10-venv python3.10-distutils
```

Check:
```bash
python3.10 --version
```

## 2. Create and Activate Virtual Environment
From project root:
```bash
cd /home/nandan/quotes-rasa-chatbot
python3.10 -m venv .venv
source .venv/bin/activate
```

Upgrade packaging tools:
```bash
python -m pip install --upgrade pip setuptools wheel
```

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```

`requirements.txt` includes compatibility pins for this setup:
- `setuptools>=68,<76`
- `sqlalchemy<2.0`

## Quick Start With Make
If `make` is available, this is the fastest path:
```bash
cd /home/nandan/quotes-rasa-chatbot
make setup
make train
```

## 4. Train the Model
```bash
rasa train
```

Expected output:
- A model file in `models/` (example: `models/<timestamp>.tar.gz`)

## 5. Run the Chatbot (3 Terminals)
Use project root in all terminals.

Terminal 1 (Action Server):
```bash
make run-actions
```

Terminal 2 (Rasa Server + REST API):
```bash
make run-server
```

Terminal 3 (Frontend Static Server):
```bash
make run-frontend
```

Open in browser:
- `http://localhost:8000`

## 6. Test Messages
Try these in the chat UI:
- `I feel sad, give me a quote`
- `give me a motivational quote`
- `I want something funny`
- `what categories do you support`
- `I am stressed`

## REST API Test (Without Frontend)
```bash
curl -X POST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"sender":"cli-user","message":"I need motivation"}'
```

Or run the built-in smoke test:
```bash
make smoke
```

## Key Config Files
- `config.yml`: NLU pipeline and policies. Includes required `assistant_id`.
- `domain.yml`: intents, entities, slots, responses, actions.
- `data/nlu.yml`: training examples for intents/entities/synonyms.
- `data/stories.yml` and `data/rules.yml`: conversation behavior.
- `actions/actions.py`: custom quote selection logic.
- `credentials.yml`: enables REST channel.
- `endpoints.yml`: action server URL.

## Common Errors and Fixes

### 1) `This environment is externally managed`
Cause:
- Trying to install packages into system Python.

Fix:
- Always use virtualenv (`.venv`) and install with `pip` inside it.

### 2) `No matching distribution found for rasa==3.6.20`
Cause:
- Using unsupported Python version (3.11/3.12).

Fix:
- Use Python `3.10` and recreate `.venv`.

### 3) `ModuleNotFoundError: No module named 'pkg_resources'`
Cause:
- Missing `setuptools` in virtualenv.

Fix:
```bash
source .venv/bin/activate
pip install --upgrade setuptools
pip install -r requirements.txt
```

### 4) SQLAlchemy `MovedIn20Warning`
Cause:
- Rasa internals emit warning with SQLAlchemy 2.x compatibility concerns.

Fix:
- Already handled by pinning `sqlalchemy<2.0` in `requirements.txt`.

### 5) Frontend says it cannot reach Rasa server
Checks:
- Is `rasa run --enable-api --cors "*" -p 5005` running?
- Is action server running on port `5055`?
- Is frontend loaded from `http://localhost:8000`?

## Development Workflow
After changing training data/config/domain:
```bash
make train
```
Restart servers after retraining.

## Optional CLI Chat Test
```bash
make shell
```

## Additional Make Targets
```bash
make help        # list all targets
make validate    # validate domain/data consistency
make test        # run rasa tests
make clean       # clean local cache artifacts
```

## Telemetry (Optional)
Disable anonymous telemetry if desired:
```bash
rasa telemetry disable
```

# Quotes Recommendation Chatbot (Rasa)

A conversational AI chatbot built with Rasa that recommends quotes based on user intent, mood, and preferred category.

## Features

- Intent and entity detection with Rasa NLU
- Quote recommendation via custom action server
- Supported quote categories: Inspiration, Motivation, Success, Love, Humor
- Web chat frontend using Rasa REST API
- CLI and automated smoke-test support

## Tech Stack

- Python 3.10
- Rasa `3.6.20`
- Rasa SDK `3.6.2`

## Project Structure

```text
.
├── actions/              # Custom Rasa actions
├── data/                 # NLU data, stories, rules
├── frontend/             # Browser chat UI
├── tests/                # Test stories
├── scripts/              # Utility scripts (smoke test)
├── config.yml            # Rasa pipeline and policies
├── domain.yml            # Intents, entities, responses, actions
├── endpoints.yml         # Action server endpoint
├── credentials.yml       # REST channel config
├── requirements.txt      # Python dependencies
└── Makefile              # Common commands
```

## Prerequisites

- Python `3.10`
- `make`
- Linux/WSL/macOS terminal

## Quickstart

From the project root:

```bash
make setup
make train
```

Run these in separate terminals:

```bash
# Terminal 1
make run-actions
```

```bash
# Terminal 2
make run-server
```

```bash
# Terminal 3
make run-frontend
```

Open the app:

```text
http://localhost:8000
```

## Useful Commands

```bash
make help       # List all available tasks
make validate   # Validate training data/domain
make test       # Run Rasa tests
make shell      # Chat in terminal
make smoke      # REST webhook smoke test
make clean      # Remove local cache artifacts
```

## API Endpoints

- Rasa server: `http://localhost:5005`
- REST webhook: `http://localhost:5005/webhooks/rest/webhook`
- Action server health: `http://localhost:5055/health`

## Report and Demo

- Project Report: `Project_Report.pdf` (add at repo root or `docs/Project_Report.pdf`)
- Demo Video Link: `PASTE_DEMO_VIDEO_LINK_HERE`

## Submission Checklist

- All project files committed (code, configs, tests, scripts, frontend)
- Project report included in the repository
- Demo video link added in this README
- Repository pushed to GitHub and shared on submission platform

## Troubleshooting

- If `make setup` fails, verify Python 3.10 is installed and available as `python3.10`.
- If smoke test fails, ensure `make run-server` is active before `make smoke`.
- If custom actions do not run, start `make run-actions` and confirm `http://localhost:5055/health` is reachable.

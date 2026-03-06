# Quotes Recommendation Chatbot

Simple Rasa chatbot that gives quotes by category or emotion.

## 1. Prerequisites

- Python `3.10` (required)
- `make`
- Terminal (Linux/WSL/macOS)

Check Python:

```bash
python3.10 --version
```

## 2. Setup (Run Once)

From project root:

```bash
make setup
make train
```

## 3. Run the Project

Open **3 terminals** in project root.

Terminal 1:

```bash
make run-actions
```

Terminal 2:

```bash
make run-server
```

Terminal 3:

```bash
make run-frontend
```

Open in browser:

```text
http://localhost:8000
```

## 4. Quick Verification

In a new terminal:

```bash
make smoke
```

Expected: non-empty response and `Smoke test passed.`

## 5. Useful Commands

```bash
make shell      # chat in terminal
make test       # run Rasa tests
make validate   # validate training data/domain
make clean      # clean local cache files
```

## 6. Common Issues

- `python3.10 not found`: install Python 3.10, then run `make setup` again.
- Empty smoke response: ensure `make run-server` is running.
- Action errors: ensure `make run-actions` is running.

## 7. Report and Demo

- Project report file: `project_report.pdf`
- Demo video link: `https://drive.google.com/file/d/17ABaiosKWO2MkKdLFq9KG2aAsmfNc9u-/view?usp=sharing`

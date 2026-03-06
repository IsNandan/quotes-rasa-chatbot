#!/usr/bin/env bash
set -euo pipefail

RASA_URL="http://localhost:5005/webhooks/rest/webhook"
ACTION_URL="http://localhost:5055/health"
PAYLOAD='{"sender":"smoke-test","message":"give me a motivational quote"}'

if ! curl -sS -o /dev/null "${RASA_URL%/webhooks/rest/webhook}"; then
  echo "Smoke test failed: Rasa server is not reachable on port 5005."
  echo "Start it in another terminal with:"
  echo "  make run-server"
  exit 1
fi

if ! curl -sS -o /dev/null "${ACTION_URL}"; then
  echo "Warning: Action server on port 5055 is not reachable."
  echo "Custom actions may fail. Start it with:"
  echo "  make run-actions"
fi

echo "Sending smoke request to ${RASA_URL}"
response=$(curl -sS -X POST "${RASA_URL}" \
  -H "Content-Type: application/json" \
  -d "${PAYLOAD}")

echo "Response: ${response}"

if [[ "${response}" == "[]" || -z "${response}" ]]; then
  echo "Smoke test failed: empty response"
  exit 1
fi

echo "Smoke test passed."

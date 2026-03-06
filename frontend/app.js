const RASA_REST_WEBHOOK = "http://localhost:5005/webhooks/rest/webhook";
const SENDER_ID = "web-user";

const chatWindow = document.getElementById("chat-window");
const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");

function appendBubble(text, sender) {
  const div = document.createElement("div");
  div.className = `bubble ${sender}`;
  div.textContent = text;
  chatWindow.appendChild(div);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function sendMessage(message) {
  const payload = {
    sender: SENDER_ID,
    message,
  };

  const response = await fetch(RASA_REST_WEBHOOK, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }

  return response.json();
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const message = input.value.trim();
  if (!message) return;

  appendBubble(message, "user");
  input.value = "";

  try {
    const botResponses = await sendMessage(message);

    if (!botResponses.length) {
      appendBubble("I have no response right now. Please try again.", "bot");
      return;
    }

    for (const item of botResponses) {
      if (item.text) {
        appendBubble(item.text, "bot");
      }
    }
  } catch (error) {
    appendBubble(
      "Cannot reach Rasa server at http://localhost:5005. Start the backend and try again.",
      "bot"
    );
  }
});

appendBubble(
  "Hi, I am your Quotes Recommendation Chatbot. Ask me for a quote by mood or category.",
  "bot"
);

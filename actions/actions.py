from __future__ import annotations

import random
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


QUOTE_BANK: Dict[Text, List[Text]] = {
    "inspiration": [
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "The future depends on what you do today. - Mahatma Gandhi",
        "Small steps every day lead to big changes over time.",
    ],
    "motivation": [
        "Discipline is choosing what you want most over what you want now.",
        "Success is the sum of small efforts repeated day in and day out. - Robert Collier",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "Push yourself, because no one else is going to do it for you.",
        "The hard days are what make you stronger. - Aly Raisman",
    ],
    "success": [
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "Dream big. Start small. Act now.",
        "Opportunities don't happen. You create them. - Chris Grosser",
        "There are no shortcuts to any place worth going. - Beverly Sills",
    ],
    "love": [
        "Where there is love there is life. - Mahatma Gandhi",
        "Love recognizes no barriers. - Maya Angelou",
        "To love and be loved is to feel the sun from both sides. - David Viscott",
        "Love is composed of a single soul inhabiting two bodies. - Aristotle",
        "The best thing to hold onto in life is each other. - Audrey Hepburn",
    ],
    "humor": [
        "I'm on a seafood diet. I see food and I eat it.",
        "People say nothing is impossible, but I do nothing every day. - A.A. Milne",
        "My wallet is like an onion; opening it makes me cry.",
        "I used to think I was indecisive, but now I'm not sure.",
        "If at first you don't succeed, skydiving is not for you. - Steven Wright",
    ],
}

EMOTION_TO_CATEGORY: Dict[Text, Text] = {
    "sad": "inspiration",
    "low": "inspiration",
    "down": "inspiration",
    "anxious": "motivation",
    "stressed": "motivation",
    "tired": "motivation",
    "confident": "success",
    "confidence": "success",
    "excited": "success",
    "heartbroken": "love",
    "heartbreak": "love",
    "lonely": "love",
    "happy": "humor",
}

CATEGORY_KEYWORDS = {
    "inspiration": {"inspiration", "inspirational", "inspire"},
    "motivation": {"motivation", "motivational", "motivate"},
    "success": {"success", "successful", "achieve", "achievement"},
    "love": {"love", "romantic", "heart"},
    "humor": {"humor", "funny", "joke", "laugh"},
}


class ActionGetPersonalizedQuote(Action):
    def name(self) -> Text:
        return "action_get_personalized_quote"

    def _extract_category_from_text(self, text: Text) -> Text | None:
        lowered = text.lower()
        for category, keywords in CATEGORY_KEYWORDS.items():
            if any(word in lowered for word in keywords):
                return category
        return None

    def _extract_emotion_from_text(self, text: Text) -> Text | None:
        lowered = text.lower()
        for emotion in EMOTION_TO_CATEGORY.keys():
            if emotion in lowered:
                return emotion
        return None

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        latest_text = (tracker.latest_message.get("text") or "").strip()
        detected_entities = tracker.latest_message.get("entities", [])

        category = tracker.get_slot("category")
        emotion = tracker.get_slot("emotion")

        for entity in detected_entities:
            if entity.get("entity") == "category":
                category = (entity.get("value") or "").lower()
            if entity.get("entity") == "emotion":
                emotion = (entity.get("value") or "").lower()

        if not category and latest_text:
            category = self._extract_category_from_text(latest_text)

        if not emotion and latest_text:
            emotion = self._extract_emotion_from_text(latest_text)

        if category:
            category = category.lower().strip()
        if emotion:
            emotion = emotion.lower().strip()

        if not category and emotion:
            category = EMOTION_TO_CATEGORY.get(emotion)

        if category not in QUOTE_BANK:
            dispatcher.utter_message(
                text=(
                    "I can recommend quotes from Inspiration, Motivation, Success, Love, or Humor. "
                    "Tell me a category and I'll pick one for you."
                )
            )
            return [SlotSet("emotion", emotion), SlotSet("category", None)]

        quote = random.choice(QUOTE_BANK[category])

        if emotion:
            response = (
                f"Since you're feeling {emotion}, here's a {category} quote:\n"
                f"\"{quote}\"\n\nDid this help?"
            )
        else:
            response = f"Here's a {category} quote:\n\"{quote}\"\n\nDid this help?"

        dispatcher.utter_message(text=response)
        return [SlotSet("category", category), SlotSet("emotion", emotion)]

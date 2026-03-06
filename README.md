## Abstract

  The Quotes Recommendation Chatbot is a conversational AI system
  built using Rasa NLU to provide users with personalized and
  meaningful quotes based on their intent, emotional state, and
  preferred category. The chatbot addresses the need for instant
  motivation, emotional reassurance, and positivity in daily
  life. It supports quote categories such as Inspiration,
  Motivation, Success, Love, and Humor, and responds through
  natural language interactions. The solution includes a custom
  action for quote recommendation, dialogue management using
  stories and rules, and deployment through a browser-based
  interface via Rasa REST API. The project demonstrates a
  complete lifecycle from problem definition and data preparation
  to training, testing, deployment, and validation.

  ## 1. Introduction

  In today’s fast-paced environment, people frequently seek quick
  emotional support and encouragement. Manual searching for
  appropriate quotes is often inefficient and time-consuming.
  This project introduces an intelligent chatbot that understands
  user messages and delivers relevant quotes instantly. The
  chatbot focuses on user engagement by adding follow-up
  interaction such as satisfaction checks after quote delivery.

  ## 2. Problem Statement

  Users need fast, context-aware motivational content, but
  existing manual methods are inconsistent and slow. A chatbot
  that understands user intent and emotions can provide
  immediate, personalized quote recommendations and improve user
  experience.

  ## 3. Objectives

  - Build a chatbot that understands natural language input.
  - Detect user intents and entities (category/emotion).
  - Recommend suitable quotes based on mood and preference.
  - Support interactive conversation flow with follow-up
    feedback.
  - Deploy chatbot through a web interface using REST API.
  - Ensure model reusability and ease of retraining.

  ## 4. Prerequisites

  - Python 3.10 (required for Rasa 3.6.20)
  - Virtual environment (venv) or Anaconda (optional alternative)
  - Libraries:
      - rasa==3.6.20
      - rasa-sdk==3.6.2
      - setuptools>=68,<76
      - sqlalchemy<2.0
  - Development tools:
      - VS Code
      - Linux/WSL terminal
      - Browser for frontend testing

  ## 5. Methodology / Workflow

  1. Define business problem and scope
  2. Gather business requirements
  3. Prepare NLU training data and conversation flows
  4. Configure Rasa NLU pipeline and policies
  5. Implement custom action for quote selection
  6. Train model and validate consistency
  7. Test chatbot in CLI and test stories
  8. Deploy using REST API and web frontend
  9. Validate deployed behavior and document results

  ## 6. System Design and Implementation

  ### 6.1 Story 1: Business Problem

  The chatbot solves delayed access to emotional support content
  by providing instant quote recommendations based on user mood
  and request type.

  ### 6.2 Story 2: Business Requirements

  - Understand user requests for quotes
  - Support categories: Inspiration, Motivation, Success, Love,
    Humor
  - Map emotional terms to suitable quote categories
  - Provide relevant response with conversational follow-up
  - Allow web-based usage through browser

  ### 6.3 Story 3: Literature Survey

  - Rule-based bots are deterministic but limited in flexibility.
  - Intent-based NLU systems improve conversational relevance.
  - Rasa provides open-source customization for domain-driven
    assistants.
  - Emotion-aware conversation improves engagement and user
    satisfaction.

  ### 6.4 Story 4: Social/Business Impact

  - Promotes positivity and emotional reassurance
  - Improves accessibility to motivational content
  - Useful for education, productivity, wellness, and self-help
    contexts
  - Can be extended into enterprise or wellness assistant
    solutions

  ### 6.5 Story 5: Install Rasa and Dependencies

  python3.10 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt

  ### 6.6 Story 6: Setting Up the Rasa Project

  Configured key files:

  - config.yml (pipeline/policies/assistant_id)
  - domain.yml (intents/entities/slots/responses/actions)
  - data/nlu.yml, data/stories.yml, data/rules.yml
  - actions/actions.py for personalized quote logic
  - credentials.yml and endpoints.yml for REST + custom actions

  ### 6.7 Story 7: Data Collection and Training Format

  - Intent examples and entity annotations in nlu.yml
  - Synonyms and lookup values for robust category detection
  - Conversation logic via stories and rules in YAML format

  ### 6.8 Story 8: Bot Responses and Interaction Design

  - Response templates added in domain.yml
  - Action returns quotes based on category/emotion
  - Follow-up: “Did this help?” improves interaction quality

  ### 6.9 Story 9: Model Training

  rasa train

  Produces reusable model artifacts in models/.

  ### 6.10 Story 10: Model Storage and Reusability

  - Trained model files stored in models/
  - New training required only when data/config changes
  - Model files can be reused for deployment environments

  ## 7. Testing and Validation

  ### 7.1 Story 1: Testing Using rasa shell

  rasa shell

  Validated response quality for mood/category queries.

  ### 7.2 Story 2: Testing Using Test Stories

  rasa test

  Verified conversation paths from tests/test_stories.yml.

  ### 7.3 Story 3: Deployment Using Web Interface

  Run:

  1. rasa run actions
  2. rasa run --enable-api --cors "*"
  3. python3 -m http.server 8000 --directory frontend
     Then access http://localhost:8000.

  ### 7.4 Story 4: Validation of Deployed Chatbot

  - REST smoke test executed successfully (make smoke)
  - Validated end-to-end quote recommendation via browser UI
  - Confirmed custom action execution and follow-up behavior

  ## 8. Results

  The chatbot successfully:

  - Detected intents and emotional cues
  - Recommended category-appropriate quotes
  - Maintained conversational flow with follow-up questions
  - Worked through both CLI and web interface
  - Passed deployment smoke test through REST webhook

  ## 9. Screenshots (To Include in Final Submission)

  1. Project folder structure
  2. Successful dependency installation
  3. rasa train output
  4. Running action server terminal
  5. Running Rasa API server terminal
  6. Browser chat interface with sample conversation
  7. Smoke test success output

  ## 10. Challenges and Fixes

  - Python compatibility issues with Rasa fixed by moving to
    Python 3.10
  - PEP 668 “externally managed” issue fixed via virtual
    environment usage
  - pkg_resources error fixed by adding setuptools
  - SQLAlchemy warning handled via sqlalchemy<2.0 pinning

  ## 11. Future Enhancements

  - Add large external quote dataset/database integration
  - Multi-language support
  - User-specific recommendation history
  - Sentiment scoring for improved personalization
  - Cloud deployment with monitoring and analytics

  ## 12. Conclusion

  The Quotes Recommendation Chatbot demonstrates a complete and
  practical conversational AI solution built with Rasa NLU. It
  addresses a real user need for quick emotional support and
  motivational content through context-aware responses. The
  project is modular, deployable, and extensible, making it
  suitable as both an academic project and a base for real-world
  applications.
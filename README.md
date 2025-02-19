## agents.json

    ✅ Discover and integrate APIs autonomously.
    ✅ Negotiate authentication and permissions without human setup.
    ✅ Execute multi-step workflows across services (e.g., book a tour, schedule a ride, send a payment).
    ✅ Handle failures intelligently, escalating when needed (e.g., calling an agent if API booking fails).

## 2.18
testing langchain agent with zillow api
- the test is in test-langchain.py

- the agent is using the following tools:
    - search_apartments
    - get_property_details
    - book_tour
    - schedule_ride
    - send_payment

- the agent is using the following llm:
    - gpt-4o-mini

- the agent is using the following memory:
    - ConversationBufferMemory

- the agent is using the following agent:
    - zero-shot-react-description

- the agent is using the following tools:
    - search_apartments
    - get_property_details
    - book_tour
    - schedule_ride
    - send_payment


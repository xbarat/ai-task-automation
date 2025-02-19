from dotenv import load_dotenv
load_dotenv()

from langchain.agents import initialize_agent, Tool
from langchain.tools import tool
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
import requests

# 🏠 Define an apartment search tool
@tool
def search_apartments(query: str) -> str:
    """Search for apartments. Input should be in format 'city, max_price'.
    Example: 'New York, 4500'"""
    try:
        city, max_price = [x.strip() for x in query.split(',')]
        max_price = int(''.join(filter(str.isdigit, max_price)))
        
        print(f"Searching apartments in {city} under ${max_price}...")
        apartments = [
            {"name": "Luxury 1BR", "price": 4300, "location": "Manhattan", "url": "https://zillow.com/listing1"},
            {"name": "Cozy Studio", "price": 4000, "location": "Brooklyn", "url": "https://zillow.com/listing2"}
        ]
        
        # Filter apartments based on price
        available_apts = [apt for apt in apartments if apt['price'] <= max_price]
        
        if not available_apts:
            return f"No apartments found in {city} under ${max_price}"
        
        # Format results
        results = []
        for apt in available_apts:
            results.append(f"- {apt['name']} in {apt['location']} for ${apt['price']} ({apt['url']})")
        
        return "\n".join(results)
    except Exception as e:
        return f"Error: Please provide input in format 'city, max_price'. Example: 'New York, 4500'"

# 📌 Define memory to store shortlisted apartments
memory = ConversationBufferMemory(memory_key="apartment_search", return_messages=True)

# 🤖 Initialize LangChain Agent
llm = ChatOpenAI(model_name="gpt-4", temperature=0)
tools = [search_apartments]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    memory=memory,
    verbose=True
)

# 🔎 Run the agent
response = agent.run("Find me an apartment in New York under $4500")
print("\nFinal Response:", response)

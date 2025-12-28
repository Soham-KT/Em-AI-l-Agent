from langchain_google_community import GmailToolkit
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

toolkit = GmailToolkit()
tools = toolkit.get_tools()
llm = ChatOllama(model='llama3.1')


agent = create_agent(llm, tools)

example_query = "Draft an email to fake@fake.com thanking them for coffee."

events = agent.stream(
    {"messages": [("user", example_query)]},
    stream_mode="values",
)
for event in events:
    event["messages"][-1].pretty_print()
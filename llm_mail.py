from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_google_community import GmailToolkit
from langchain.agents import create_agent
from pydantic import BaseModel, Field
import re

model = ChatOllama(model='llama3.1')

class Email(BaseModel):
    subject: str = Field(description='Subject of the Email')
    body: str = Field(description='Body of the Email')


def get_subject_and_body(topic: str) -> tuple:
    template = '''
    You are a helpful Email sending assistant. Your job is to write a mail for the following topic : {topic}.
    The mail should have a good subject and an appropriate body.
    Both the subject and the body should be the output.
    In the end, email should ALWAYS be signed by "Soham Kothari"
    '''

    prompt = PromptTemplate(
        template=template,
        input_variables=['topic']
    )

    structured_model = model.with_structured_output(Email)

    chain = prompt | structured_model

    res = chain.invoke({'topic': topic})

    body = res.body.encode('utf-8').decode('unicode_escape')

    return (res.subject, body)

def send_mail(topic: str) -> None:
    mail = get_subject_and_body(topic)

    gmail_tools = GmailToolkit().get_tools()

    gmail_agent = create_agent(
        model=model,
        tools=gmail_tools,
        system_prompt="""
You are a Gmail assistant.

You will receive:
- an ACTION: DRAFT or SEND
- email details

Rules:
- If ACTION is DRAFT → create a Gmail draft ONLY
- If ACTION is SEND → send the Gmail to the specified Gmail ID
- Do NOT modify subject or body
- Use the subject and body given 
- Do NOT ask questions
- The format of Body should not change. That includes the all the characters, unicode characters, symbols, etc
"""
)
    gmail_query = f"Topic:{topic}\nSubject: {mail[0]}\nBody: {mail[1]}. Do not change the subject and body provided"

    events = gmail_agent.stream(
        {"messages": [("user", gmail_query)]},
        stream_mode="values"
    )

    for event in events:
        event["messages"][-1].pretty_print()


if __name__ == '__main__':
    res = send_mail('write a mail to john doe, his mail: johndoe@fake.com. Discussing about explaining black holes')
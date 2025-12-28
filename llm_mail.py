from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_agent
from pydantic import BaseModel, Field

class Email(BaseModel):
    subject: str = Field(description='Subject of the Email')
    body: str = Field(description='Body of the Email')


def get_subject_and_body(topic: str) -> tuple:

    model = ChatOllama(model='llama3.1')

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

    return (res.subject, res.body)

if __name__ == '__main__':
    res = get_subject_and_body('write a mail to john doe about explaining black holes')
    print(res[0])
    print(res[1])
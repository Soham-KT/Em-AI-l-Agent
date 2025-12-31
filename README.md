# Em(AI)l Agent

Em(AI)l Agent is a Python-based AI agent that leverages Large Language Models (LLMs) to automatically draft and send emails. It is controlled via a simple Telegram bot interface, allowing users to send complex email requests using natural language.

## How It Works

The agent operates through a two-step process:

1.  **Content Generation:** When a user provides a topic or instruction via the Telegram bot, the agent first uses a local LLM (via `Ollama` and `langchain`) to generate an appropriate subject and body for the email. This process is guided by a prompt template that ensures the email is well-structured and signed correctly.

2.  **Action Execution:** The generated subject and body are then passed to a second LangChain agent equipped with `GmailToolkit`. This agent interprets the user's initial command (e.g., "send" or "draft") and the recipient's details to perform the final action: either sending the email directly or saving it as a draft in your Gmail account.

## Features

*   **Natural Language Commands:** Draft or send emails by describing your request in plain English.
*   **Telegram Bot Integration:** Easy-to-use interface through a Telegram bot.
*   **Local LLM Powered:** Uses Ollama with models like Llama 3.1 for privacy and cost-effectiveness.
*   **Gmail Integration:** Securely interacts with your Gmail account to send emails and create drafts using the `GmailToolkit`.
*   **Structured Output:** Employs Pydantic models to ensure reliable generation of email subjects and bodies from the LLM.

## Setup and Installation

### Prerequisites

*   Python 3.8+
*   [Ollama](https://ollama.com/) installed and running.
*   The Llama 3.1 model pulled in Ollama: `ollama pull llama3.1`
*   Telegram API credentials (API ID, API Hash) and a Bot Token.
*   Google Cloud Project with the Gmail API enabled. You will need to create OAuth 2.0 credentials and download the `credentials.json` file.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Soham-KT/Em-AI-l-Agent.git
    cd Em-AI-l-Agent
    ```

2.  **Set up Gmail API Credentials:**
    *   Follow the instructions from the [Google API Python Quickstart](https://developers.google.com/gmail/api/quickstart/python) to enable the Gmail API and download your `credentials.json` file.
    *   Place the `credentials.json` file in the root directory of this project.
    *   The first time you run the application, you will be prompted to authorize access to your Gmail account through a browser window. A `token.json` file will be created to store your credentials for future runs.

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables:**
    Create a `.env` file in the root directory and add your Telegram credentials:
    ```env
    TELEGRAM_API=<YOUR_TELEGRAM_API_ID>
    TELEGRAM_HASH=<YOUR_TELEGRAM_API_HASH>
    TELEGRAM_BOT_TOKEN=<YOUR_TELEGRAM_BOT_TOKEN>
    ```

## Usage

1.  **Start Ollama:** Make sure the Ollama service is running on your machine.

2.  **Run the application:**
    ```bash
    python main.py
    ```
    The Telegram bot will start and connect to your account.

3.  **Interact with the bot:**
    Open Telegram and start a conversation with your bot. You can use the following commands:
    *   `/start`: Initializes the conversation with the bot.
    *   `/help`: Provides instructions and the prompt format.
    *   `/info`: Gives a brief description of the bot.

4.  **Send or Draft an Email:**
    To instruct the agent, send a message following the format provided by the `/help` command. The agent will parse your request, generate the content, and perform the requested action.

    **Example Prompts:**
    *   `Send an email to John Doe, their email: johndoe@fake.com. The topic is a discussion about explaining black holes.`
    *   `Draft an email to contact@company.com requesting a project update.`

The bot will confirm once the task is completed.

## File Breakdown

*   `main.py`: The entry point of the application. It runs the Telethon client for the Telegram bot, handles commands, and passes user requests to the email agent.
*   `llm_mail.py`: Contains the core logic for the email agent. It defines functions to generate email content using an LLM and to create and invoke the Gmail agent for sending/drafting.
*   `requirements.txt`: Lists all the necessary Python packages for the project.
*   `test.py`: A simple script for testing the Gmail agent functionality independently of the Telegram bot.
*   `LICENSE`: The Apache 2.0 license for the project.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

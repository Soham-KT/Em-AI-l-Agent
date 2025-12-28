import nest_asyncio
import logging
import asyncio
from telethon import TelegramClient, events
from dotenv import load_dotenv
import os
from llm_mail import send_mail

load_dotenv()

nest_asyncio.apply()
logging.basicConfig(level=logging.INFO)

client = TelegramClient('bot', api_id=os.getenv('TELEGRAM_API'), api_hash=os.getenv('TELEGRAM_HASH'))


async def main():
    await client.start(bot_token=os.getenv('TELEGRAM_BOT_TOKEN'))

    @client.on(events.NewMessage(pattern='/start'))
    async def start_handler(event):
        await event.respond("Hello, My name is Gmail AI Agent. It's my job to send / draft a mail to the person you specify")
        logging.info(f'start command received from {event.sender_id}')

    @client.on(events.NewMessage(pattern='/help'))
    async def help_handler(event):
        help_text = "here are the commands you can use:\n/start - start the bot\n/help - get help information\n/info - get information about the bot\nHere is the template you should give the prompt in: Send / Draft an email to 'name', their email: 'email'. 'topic'."

        await event.respond(help_text)
        logging.info(f'help command recieved from {event.sender_id}')

    
    @client.on(events.NewMessage(pattern='/info'))
    async def info_handler(event):
        await event.respond('This ai mail agent is created in python with ChatOllama langchain')
        logging.info(f'info command recieved from {event.sender_id}')

    @client.on(events.NewMessage)
    async def keyword_describer(event):
        message = event.text.lower()
        if message in ['/start', '/help', '/info']:
            return

        # ---------------------------------------------------------------------------------------------------------------------
        send_mail(message)

        await event.respond('Task completed.')

        logging.info(f'message received from {event.sender_id}: {event.text}')

    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())

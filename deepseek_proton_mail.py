import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from pydantic import SecretStr

# Load environment variables
load_dotenv()

async def send_proton_email():
    # Configure browser with security settings
    browser = Browser(config=BrowserConfig(
        headless=False,
        disable_security=False
    ))

    # Configure DeepSeek model according to working reddit example
    llm = ChatOpenAI(
        base_url='https://api.deepseek.com/v1',
        model='deepseek-chat',
        api_key=SecretStr(os.getenv('DEEPSEEK_API_KEY')),
        temperature=0.0  # Match successful reddit config
    )

    # Get credentials from environment
    email = os.getenv('PROTON_MAIL_EMAIL')
    password = os.getenv('PROTON_MAIL_PASSWORD')

    agent = Agent(
        task=(
            "1. Go to mail.proton.me\n"
            "2. Click 'Sign in'\n"
            f"3. Enter email: {email}\n"
            f"4. Enter password: {password}\n"
            "5. Click 'New message'\n"
            f"6. Send email to {os.getenv('PROTON_MAIL_RECIPIENT')} with subject 'I love you' and body 'This message was sent automatically with DeepSeek'"
        ),
        llm=llm,
        browser=browser,
        use_vision=False  # Disable vision as in working reddit example
    )

    result = await agent.run()
    print("Email sending result:", result)

if __name__ == '__main__':
    asyncio.run(send_proton_email()) 
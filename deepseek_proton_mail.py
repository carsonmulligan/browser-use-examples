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

    # Configure DeepSeek model
    llm = ChatOpenAI(
        base_url='https://api.deepseek.com/v1',
        model='deepseek-chat',
        api_key=SecretStr(os.getenv('DEEPSEEK_API_KEY'))
    )

    # Get credentials from environment
    email = os.getenv('PROTON_MAIL_EMAIL')
    password = os.getenv('PROTON_MAIL_PASSWORD')

    agent = Agent(
        task=(
            f"1. Navigate to mail.proton.me\n"
            f"2. Click 'Sign in' button\n"
            f"3. In email field input: {email}\n"
            f"4. In password field input: {password}\n"
            f"5. Click 'Sign in' button\n"
            f"6. Click 'New message' button\n"
            f"7. In To field enter: profiles.co@gmail.com\n"
            f"8. In Subject field enter: DeepSeek Automated Test\n"
            f"9. In body type: Hello World from DeepSeek R1\n"
            f"10. Click 'Send' and verify confirmation"
        ),
        llm=llm,
        browser=browser,
        use_vision=True
    )

    result = await agent.run()
    print("Email sending result:", result)

if __name__ == '__main__':
    asyncio.run(send_proton_email()) 
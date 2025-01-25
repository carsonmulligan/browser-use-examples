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

    # Configure DeepSeek model with proper API settings
    llm = ChatOpenAI(
        base_url='https://api.deepseek.com/v1',
        model='deepseek-chat',
        api_key=SecretStr(os.getenv('DEEPSEEK_API_KEY')),
        temperature=0.3  # Added for better stability
    )

    # Get credentials from environment
    email = os.getenv('PROTON_MAIL_EMAIL')
    password = os.getenv('PROTON_MAIL_PASSWORD')

    agent = Agent(
        task=(
            f"1. Navigate to mail.proton.me\n"
            f"2. Find and click the 'Sign in' button\n"
            f"3. In email field, carefully type: {email}\n"
            f"4. In password field, carefully type: {password}\n"
            f"5. Click 'Sign in' and wait for login\n"
            f"6. Locate and click 'New message' button\n"
            f"7. In 'To' field, enter: profiles.co@gmail.com\n"
            f"8. In 'Subject', write: DeepSeek Test\n"
            f"9. In body, write: Hello from DeepSeek R1\n"
            f"10. Review all fields\n"
            f"11. Click 'Send' and confirm delivery"
        ),
        llm=llm,
        browser=browser,
        use_vision=True,
        max_actions_per_step=3  # Added for better reliability
    )

    result = await agent.run()
    print("Email sending result:", result)

if __name__ == '__main__':
    asyncio.run(send_proton_email()) 
import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig
from playwright.async_api import BrowserContext

# Load environment variables
load_dotenv()

# Get environment variables
api_key = os.getenv('DEEPSEEK_API_KEY')
proton_email = os.getenv('PROTONMAIL_EMAIL')
proton_password = os.getenv('PROTONMAIL_PASSWORD')
recipient_email = "profiles.co@gmail.com"

if not all([api_key, proton_email, proton_password]):
    raise ValueError('Missing required environment variables in .env file')

async def send_perplexity_summary():
    # Configure DeepSeek model
    llm = ChatOpenAI(
        base_url='https://api.deepseek.com/v1',
        model='deepseek-chat',
        api_key=SecretStr(api_key),
    )

    # Create proper browser configuration
    context_config = BrowserContextConfig(
        wait_for_network_idle_page_load_time=3.0,
        minimum_wait_page_load_time=1.0
    )
    
    browser_config = BrowserConfig(
        new_context_config=context_config,
        headless=False  # Ensure browser is visible
    )
    
    async with Browser(config=browser_config) as browser:
        # Create agent with browser context
        agent = Agent(
            task=(
                f"1. Go to perplexity.ai\n"
                f"2. Search: 'Latest updates on the US border security situation'\n"
                f"3. Extract key findings and sources\n"
                f"4. Summarize results in 3 bullet points with sources\n"
                f"5. Open new tab and go to mail.proton.me\n"
                f"6. On login page:\n"
                f"   a. Click email input field\n"
                f"   b. Type: {proton_email}\n"
                f"   c. Click password input field\n"
                f"   d. Type: {proton_password}\n"
                f"   e. Click 'Sign in' button\n"
                f"7. After login, click 'Compose' button\n"
                f"8. In recipient field: profiles.co@gmail.com\n"
                f"9. Subject: 'US Border Situation Update - Perplexity Findings'\n"
                f"10. In email body:\n"
                f"    a. Paste the summary\n"
                f"    b. Add source links\n"
                f"11. Click 'Send' button"
            ),
            llm=llm,
            use_vision=False,
            max_actions_per_step=5,
            browser=browser
        )

        result = await agent.run()
        print("Task completed:", result)

if __name__ == '__main__':
    asyncio.run(send_perplexity_summary()) 
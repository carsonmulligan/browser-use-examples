import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from browser_use import Agent

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

    # Create agent with enhanced instructions
    agent = Agent(
        task=(
            "1. Go to perplexity.ai\n"
            "2. Search: 'Latest updates on the US border security situation'\n"
            "3. Extract key findings and sources\n"
            "4. Summarize results in 3 bullet points with sources\n"
            "5. Open new tab and go to mail.proton.me\n"
            "6. On login page:\n"
            "   a. Click email input field\n"
            "   b. Type: " + proton_email + "\n"
            "   c. Click password input field\n"
            "   d. Type: " + proton_password + "\n"
            "   e. Click 'Sign in' button\n"
            "7. After login, click 'Compose' button\n"
            "8. In recipient field: profiles.co@gmail.com\n"
            "9. Subject: 'US Border Situation Update - Perplexity Findings'\n"
            "10. In email body:\n"
            "    a. Paste the summary\n"
            "    b. Add source links\n"
            "11. Click 'Send' button\n"
            "12. Verify confirmation message appears"
        ),
        llm=llm,
        use_vision=False,
        max_actions_per_step=5,  # Increased for complex steps
        page_load_timeout=30  # Added timeout for email client loading
    )

    # Execute the task
    result = await agent.run()
    print("Task completed:", result)

if __name__ == '__main__':
    asyncio.run(send_perplexity_summary()) 
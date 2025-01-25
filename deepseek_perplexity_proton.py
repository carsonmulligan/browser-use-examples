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

    # Create agent with multi-step instructions
    agent = Agent(
        task=(
            "1. Go to perplexity.ai\n"
            "2. Search: 'Latest updates on the US border security situation'\n"
            "3. Extract key findings and sources\n"
            "4. Summarize results in 3 bullet points with sources\n"
            "5. Go to mail.proton.me\n"
            "6. Login using email and password from environment\n"
            "7. Compose new email to profiles.co@gmail.com\n"
            "8. Subject: 'US Border Situation Update - Perplexity Findings'\n"
            "9. Body: Include summary and source links\n"
            "10. Send email"
        ),
        llm=llm,
        use_vision=False,
        max_actions_per_step=3,
        inject_credentials={
            'proton_email': proton_email,
            'proton_password': proton_password
        }
    )

    # Execute the task
    result = await agent.run()
    print("Task completed:", result)

if __name__ == '__main__':
    asyncio.run(send_perplexity_summary()) 
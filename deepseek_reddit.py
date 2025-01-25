import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from browser_use import Agent

# Load environment variables
load_dotenv()

# Get DeepSeek API key from environment
api_key = os.getenv('DEEPSEEK_API_KEY')
if not api_key:
    raise ValueError('DEEPSEEK_API_KEY is not set in .env file')

async def write_to_google_sheets():
    # Configure the DeepSeek model
    llm = ChatOpenAI(
        base_url='https://api.deepseek.com/v1',
        model='deepseek-chat',
        api_key=SecretStr(api_key),
    )

    # Create browser-use agent with detailed instructions
    agent = Agent(
        task=(
            "1. Go to reddit.com\n"
            "2. search chinese language learning\n"
        ),
        llm=llm,
        use_vision=False,  # Disable vision for faster execution
        max_actions_per_step=2  # Control action pace
    )

    # Execute the task
    result = await agent.run()
    print("Task result:", result)

if __name__ == '__main__':
    asyncio.run(write_to_google_sheets()) 
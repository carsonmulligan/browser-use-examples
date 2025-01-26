import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent

load_dotenv()

async def youtube_automation():
    llm = ChatOpenAI(
        base_url='https://api.deepseek.com/v1',
        model='deepseek-chat',
        api_key=os.getenv('DEEPSEEK_API_KEY'),
        temperature=0.1
    )

    agent = Agent(
        task=(
            "1. Go to youtube.com\n"
            "2. Search for 'pacific war in color documentary'\n"
            "3. Click first video result\n"
            "4. Verify video playback starts"
        ),
        llm=llm,
        browser=False,  # Use default browser config
        use_vision=False,
        max_actions_per_step=2
    )

    result = await agent.run()
    print("YouTube automation result:", result)

if __name__ == "__main__":
    asyncio.run(youtube_automation()) 
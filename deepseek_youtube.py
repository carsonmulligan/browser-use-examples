import asyncio
from browser_use import Agent, Browser, BrowserConfig
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

async def youtube_automation():
    agent = Agent(
        task=(
            "1. Navigate to youtube.com\n"
            "2. Accept cookies if prompted\n"
            "3. Search for 'pacific war in color documentary'\n"
            "4. Click filter button\n"
            "5. Select 'Long' duration filter\n"
            "6. Click first video result\n"
            "7. Wait for video to start playing"
        ),
        llm=ChatOpenAI(
            base_url='https://api.deepseek.com/v1',
            model='deepseek-chat',
            api_key=os.getenv('DEEPSEEK_API_KEY'),
            temperature=0.1
        ),
        browser=Browser(
            config=BrowserConfig(
                headless=False,
                chrome_options=[
                    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                ],
                window_size=(1280, 720)
            )
        ),
        action_delay=1.5,
        page_load_timeout=30
    )
    
    result = await agent.run()
    print("Youtube automation result:", result)

if __name__ == "__main__":
    asyncio.run(youtube_automation()) 
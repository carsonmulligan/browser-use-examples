import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from browser_use import Agent, Browser, BrowserConfig

# Load environment variables
load_dotenv()

# Get DeepSeek API key from environment
api_key = os.getenv('DEEPSEEK_API_KEY')
if not api_key:
    raise ValueError('DEEPSEEK_API_KEY is not set in .env file')

async def search_congress_bills():
    # Configure the DeepSeek model
    llm = ChatOpenAI(
        base_url='https://api.deepseek.com/v1',
        model='deepseek-chat',
        api_key=SecretStr(api_key),
    )

    # Create visible browser instance
    browser = Browser(config=BrowserConfig(
        headless=False  # Control browser visibility here
    ))

    # Create browser-use agent with legislative search instructions
    agent = Agent(
        task=(
            "1. Go to https://www.congress.gov\n"
            "2. In the search bar, type 'Tom Tiffany' and press Enter\n"
            "3. On the results page, filter by 'Legislation' using the left sidebar filters\n"
            "4. Under 'Sponsor', select 'Tom Tiffany (R-WI)'\n"
            "5. Wait for the filtered results to load\n"
            "6. For each bill in the results list:\n"
            "   a. Click on the bill title\n"
            "   b. On the bill details page, find the PDF download button\n"
            "   c. Click the PDF download button\n"
            "   d. Return to the search results page\n"
            "7. Continue until all bills are processed\n"
            "8. Verify all PDFs have downloaded successfully"
        ),
        llm=llm,
        browser=browser,  # Pass the configured browser instance
        use_vision=False,
        max_actions_per_step=2
    )

    # Execute the task
    result = await agent.run()
    print("Legislative search result:", result)
    
    # Clean up
    await browser.close()

if __name__ == '__main__':
    asyncio.run(search_congress_bills()) 
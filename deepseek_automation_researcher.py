import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from browser_use import Agent, Browser, BrowserContext

# Load environment variables
load_dotenv()

async def automation_research_report():
    # Configure DeepSeek model
    llm = ChatOpenAI(
        base_url='https://api.deepseek.com/v1',
        model='deepseek-chat',
        api_key=SecretStr(os.getenv('DEEPSEEK_API_KEY'))
    )

    # Initialize browser with visible window
    browser = Browser()
    context = BrowserContext(
        browser=browser,
        config={
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "headless": False
        }
    )

    # Create research and email agent
    agent = Agent(
        task=(
            "PHASE 1: RESEARCH\n"
            "1. Navigate to https://www.perplexity.ai\n"
            "2. Search: 'Best practices for using browser-use python library for web automation'\n"
            "3. Wait for full results load\n"
            "4. Extract key insights and methodologies\n"
            "5. Save important points to memory\n\n"
            
            "PHASE 2: ANALYSIS\n"
            "6. Generate 5 essential questions based on:\n"
            "   a. Central themes\n"
            "   b. Key methodologies\n"  
            "   c. Important technical details\n"
            "   d. Author perspectives\n"
            "   e. Implementation strategies\n\n"
            
            "7. Answer each question comprehensively\n\n"
            
            "PHASE 3: EMAIL COMPOSITION\n"
            "8. Go to https://mail.proton.me/login\n"
            "9. Input email: $PROTONMAIL_EMAIL\n"
            "10. Input password: $PROTONMAIL_PASSWORD\n"
            "11. Click login\n"
            "12. Compose new email to profiles.co@gmail.com\n"
            "13. Subject: 'Browser-Use Automation Report - {today's date}'\n"
            "14. Body structure:\n"
            "    ---BEGIN REPORT---\n"
            "    RESEARCH SUMMARY:\n"
            "    {key insights from Phase 1}\n\n"
            "    CRITICAL ANALYSIS:\n"
            "    Q1: [Generated Question 1]\n"
            "    A1: [Detailed Answer 1]\n"
            "    ...\n"
            "    Q5: [Generated Question 5]\n"
            "    A5: [Detailed Answer 5]\n"
            "    ---END REPORT---\n"
            "15. Attach any relevant files\n"
            "16. Send email\n"
            "17. Verify successful send"
        ),
        llm=llm,
        browser_context=context,
        use_vision=True,
        max_actions_per_step=3
    )

    # Execute the full workflow
    result = await agent.run(max_steps=25)
    print("Automation Report Result:", result)
    
    # Clean up resources
    await context.close()
    await browser.close()

if __name__ == '__main__':
    asyncio.run(automation_research_report()) 
import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent

# Load environment variables
load_dotenv()

# Retrieve Proton Mail credentials from environment
proton_email = os.getenv('PROTON_MAIL_EMAIL')
proton_password = os.getenv('PROTON_MAIL_PASSWORD')

if not proton_email or not proton_password:
    raise ValueError('PROTON_MAIL_EMAIL and PROTON_MAIL_PASSWORD must be set in .env')

async def send_proton_email():
    # Configure the OpenAI model (GPT-4o recommended for best performance)
    llm = ChatOpenAI(model="gpt-4o")

    # Create browser-use agent with detailed email sending instructions
    agent = Agent(
        task=(
            "1. Go to mail.proton.me\n"
            "2. Click 'Sign in' and log in with email and password\n"
            "3. Click 'New message' button\n"
            "4. In compose window:\n"
            "   - To: profiles.co@gmail.com\n"
            "   - Subject: Automated Test Email\n"
            "   - Body: Hello World from Browser-Use\n"
            "5. Click 'Send' button\n"
            "6. Verify email sent confirmation appears"
        ),
        llm=llm,
        use_vision=True,  # Enable vision for better UI interaction
        browser_config={
            'headless': False,  # Show browser window for debugging
            'disable_security': False  # Keep security enabled for Proton Mail
        }
    )

    # Execute the task
    result = await agent.run()
    print("Email sending result:", result)

if __name__ == '__main__':
    asyncio.run(send_proton_email()) 
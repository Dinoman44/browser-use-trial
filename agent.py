import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent, BrowserSession
from browser_use.llm import ChatAzureOpenAI

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatAzureOpenAI(model="gpt-4.1-agents"),
    )
    await agent.run()

asyncio.run(main())
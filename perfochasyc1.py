import asyncio
import aiohttp
from timer import timer

och_payload_url = 'https://tp_spec.deta.dev/api/v1/och_socrates_UK_payload'
headers = {'Content-Type': 'application/xml','x-api-key': '7ah5W8NQ.228oD7coJ9j8oh8LWMgNZy-m9vsVvfcey'}

async def fetch(session, och_payload_url):
    async with session.get(och_payload_url,ssl=False,headers=headers) as response:
        json_response = response
        print(json_response)

async def main():
    async with aiohttp.ClientSession(trust_env=True) as session:
        tasks = [fetch(session, och_payload_url) for _ in range(10)]
        await asyncio.gather(*tasks)

@timer(1, 1)
def func():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    
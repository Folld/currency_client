from client import CloudPaymentsClient
import asyncio

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = CloudPaymentsClient()
    loop.run_until_complete(client.test())

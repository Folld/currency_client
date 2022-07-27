from client import CloudPaymentsClient
import asyncio

from client.schemas import CultureName

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = CloudPaymentsClient()
    loop.run_until_complete(client.charge(100, '126.9.8.5.', 'aboba', culture_name=CultureName.russian))


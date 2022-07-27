from client import CloudPaymentsClient
import asyncio

from client.schemas import Currency

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = CloudPaymentsClient()
    loop.run_until_complete(client.token_charge(amount=100.10, token='token', account_id='123', currency=Currency.rub))


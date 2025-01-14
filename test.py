import asyncio
from aioflashforge import FlashforgeClient

if __name__ == "__main__":
    # Serial number and printer id needed
    client = FlashforgeClient("192.168.1.30", "SNMQLD9A02894", "d5c41335")
    details = asyncio.run(client.details())
    print(details)
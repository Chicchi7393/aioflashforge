# aioflashforge

An async REST API wrapper for Flashforge 3D printers written in Python.

It isn't yet finished, and I still have to test it with my printer

## Supported printers
- Flashforge Adventurer 5M (pro?)

## Usage

```py
import asyncio
from aioflashforge import FlashforgeClient

if __name__ == "__main__":
    # Serial number and printer id needed
    client = FlashforgeClient("192.168.1.xx", "A1A1A1A1A1A1A", "ffffffff")
    details = asyncio.run(client.details())
    print(details)
```

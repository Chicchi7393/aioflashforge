import asyncio
import json
from typing import Optional, Mapping, Dict, Union
import re

import aiohttp
from aiohttp import ClientResponse
from aiohttp.web_response import Response

from aioflashforge.exceptions import AddressNotValidException, SerialNotValidException, PrinterIdNotValidException, \
    PortNotValidException, GenericApiException
from aioflashforge.regex import IP_REGEX, SERIAL_REGEX, CHECK_CODE_REGEX
from aioflashforge.responses.DetailsRes import RootDetailsRes


class FlashforgeClient:
    def __init__(
            self,
            ip: str,
            serial_number: str,
            printer_id: str,
            *,
            port: int = 8898,
    ):
        if re.search(IP_REGEX, ip) is not None:
            self.ip = ip
        else:
            raise AddressNotValidException("The provided IP Address is not valid")

        if re.search(SERIAL_REGEX, serial_number) is not None:
            self.serial_number = serial_number
        else:
            raise SerialNotValidException("The provided Serial Number is not valid")

        if re.search(CHECK_CODE_REGEX, printer_id) is not None:
            self.printer_id = printer_id
        else:
            raise PrinterIdNotValidException("The provided Printer ID is not valid")

        if 65535 >= port >= 1:
            self.port = port
        else:
            raise PortNotValidException("The provided Port is not valid")

        product_res = asyncio.run(self._request("product"))
        if product_res["code"] != 0:
            raise GenericApiException(f"The request to the printer failed, got {product_res["message"]}")

    async def details(self) -> RootDetailsRes:
        details_res = await self._request("detail")
        details_body = RootDetailsRes.from_dict(details_res)
        return details_body

    async def _request(self,
                       path: str,
                       *, params: Optional[Mapping[str, str]] = None) -> Union[Dict[str, any], bytes]:
        path = path if path.endswith('/') else path + '/'
        payload = {
            "serialNumber": self.serial_number,
            "checkCode": self.printer_id,
        }

        if params is not None:
            payload.update(params)

        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'http://{self.ip}:{self.port}/{path}',
                    json=payload,
            ) as response:
                read_data = await response.content.read()
                content = read_data
                try:
                    content = json.loads(content)
                except (json.JSONDecodeError, UnicodeDecodeError) as e:
                    # this is not JSON
                    if not isinstance(e, UnicodeDecodeError):
                        content = read_data.decode()

                return content

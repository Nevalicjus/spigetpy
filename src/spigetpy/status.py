from .utils import spiget_request

__all__ = [
    "status"
]

async def status():
    return await spiget_request(type = "get", url = "status")

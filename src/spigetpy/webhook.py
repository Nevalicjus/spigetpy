from .utils import spiget_request

__all__ = [
    "delete",
    "events",
    "register",
    "status"
]

async def delete(webhook_id: str, secret: str):
    return await spiget_request(type = "delete", url = f"webhook/delete/{id}/{secret}")

async def events():
    return await spiget_request(type = "get", url = "webhook/events")

async def register(url: str, events: list):
    params = {}
    params["url"] = url
    params["events"] = events
    return await spiget_request(type = "post", url = "webhook/register", params = params)

async def status(webhook_id: str):
    return await spiget_request(type = "get", url = f"webhook/status/{id}")

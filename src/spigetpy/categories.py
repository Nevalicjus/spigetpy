from .utils import spiget_request

__all__ = [
    "list",
    "details",
    "resources"
]

async def list(size: int = None, page: int = None, sort: str = None, fields: str = None):
    params = {}
    if size != None:
        params["size"] = size
    if page != None:
        params["page"] = page
    if sort != None:
        if (sort[0:1] not in ["+", ["-"]]) or (sort[1:] not in ["Last Update", "Submission Date", "Rating", "Downloads", "Title"]):
            return "Err: Invalid sort options"
        params["sort"] = sort
    if fields != None:
        params["fields"] = fields
    return await spiget_request(type = "get", url = "categories", params = params)

async def details(category_id: int):
    return await spiget_request(type = "get", url = f"categories/{category_id}")

async def resources(category_id: int, size: int = None, page: int = None, sort: str = None, fields: str = None):
    params = {}
    if size != None:
        params["size"] = size
    if page != None:
        params["page"] = page
    if sort != None:
        if (sort[0:1] not in ["+", ["-"]]) or (sort[1:] not in ["Last Update", "Submission Date", "Rating", "Downloads", "Title"]):
            return "Err: Invalid sort options"
        params["sort"] = sort
    if fields != None:
        params["fields"] = fields
    return await spiget_request(type = "get", url = f"categories/{category_id}/resources", params = params)

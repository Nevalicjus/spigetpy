from .utils import spiget_request

__all__ = [
    "resource",
    "author"
]

async def resource(query: str, size: int = None, page: int = None, sort: str = None, fields: str = None):
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
    return await spiget_request(type = "get", url = f"search/resources/{query}", params = params)

async def author(query: str, size: int = None, page: int = None, sort: str = None, fields: str = None):
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
    return await spiget_request(type = "get", url = f"search/authors/{query}", params = params)

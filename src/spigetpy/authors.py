from .utils import spiget_request

__all__ = [
    "list",
    "details",
    "resources",
    "reviews",
    "search"
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
    return await spiget_request(type = "get", url = "authors", params = params)

async def details(author_id: int):
    return await spiget_request(type = "get", url = f"authors/{author_id}")

async def resources(author_id: int, size: int = None, page: int = None, sort: str = None, fields: str = None):
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
    return await spiget_request(type = "get", url = f"authors/{author_id}/resources", params = params)

async def reviews(author_id: int, size: int = None, page: int = None, sort: str = None, fields: str = None):
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
    return await spiget_request(type = "get", url = f"authors/{author_id}/reviews", params = params)

async def search(query: str, size: int = None, page: int = None, sort: str = None, fields: str = None):
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

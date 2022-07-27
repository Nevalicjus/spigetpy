from .utils import spiget_request

__all__ = [
    "list",
    "list_version",
    "list_free",
    "list_new",
    "list_premium",
    "details",
    "author",
    "download",
    "reviews",
    "updates",
    "updates_latest",
    "versions",
    "version_latest",
    "version",
    "version_download",
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
    return await spiget_request(type = "get", url = "resources", params = params)

async def list_version(version: str, method: str = None, size: int = None, page: int = None, sort: str = None, fields: str = None):
    params = {}
    if method not in ["any", "all"]:
        return "Err: Invalid method option"
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
    return await spiget_request(type = "get", url = f"resources/for/{version}", params = params)

async def list_free(size: int = None, page: int = None, sort: str = None, fields: str = None):
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
    return await spiget_request(type = "get", url = "resources/free", params = params)

async def list_new(size: int = None, page: int = None, sort: str = None, fields: str = None):
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
    return await spiget_request(type = "get", url = "resources/new", params = params)

async def list_premium(size: int = None, page: int = None, sort: str = None, fields: str = None):
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
    return await spiget_request(type = "get", url = "resources/premium", params = params)

async def details(resource_id: int):
    return await spiget_request(type = "get", url = f"resources/{resource_id}")

async def author(resource_id: int):
    return await spiget_request(type = "get", url = f"resources/{resource_id}/author")

async def download(resource_id: int):
    return await spiget_request(type = "get", url = f"resources/{resource_id}/download")

async def reviews(resource_id: int, size: int = None, page: int = None, sort: str = None, fields: str = None):
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
    return await spiget_request(type = "get", url = f"resources/{resource_id}/reviews", params = params)

async def updates(resource_id: int, size: int = None, page: int = None, sort: str = None, fields: str = None):
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
    return await spiget_request(type = "get", url = f"resources/{resource_id}/updates", params = params)

async def updates_latest(resource_id: int, size: int = None, page: int = None, sort: str = None, fields: str = None):
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
    return await spiget_request(type = "get", url = f"resources/{resource_id}/updates/latest", params = params)

async def versions(resource_id: int, size: int = None, page: int = None, sort: str = None, fields: str = None):
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
    return await spiget_request(type = "get", url = f"resources/{resource_id}/versions", params = params)

async def version_latest(resource_id: int):
    return await spiget_request(type = "get", url = f"resources/{resource_id}/versions/latest")

async def version(resource_id: int, version_id: int):
    return await spiget_request(type = "get", url = f"resources/{resource_id}/versions/{version_id}")

async def version_download(resource_id: int, version_id: int):
    return await spiget_request(type = "get", url = f"resources/{resource_id}/versions/{version_id}/download")

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
    return await spiget_request(type = "get", url = f"search/resources/{query}", params = params)

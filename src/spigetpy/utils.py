import requests

__all__ = [
    "spiget_request"
]

async def spiget_request(type: str, url: str, headers: dict = None, params: dict = None):
    base_url = "https://api.spiget.org/v2/"

    base_headers = {
        "user-agent": "spigetpy/0.1"
    }
    if headers != None:
        base_headers.update(headers)
    if params == None:
        params = {}
    try:
        r = requests.request(method = type, url = f"{base_url}{url}", headers = headers, params = params)
    except requests.exceptions.HTTPError:
        return "Err: requests.HTTPError; An HTTP error occurred"
    except requests.exceptions.URLRequired:
        return "Err: requests.URLRequired; A valid URL is required to make a request"
    except requests.exceptions.TooManyRedirects:
        return "Err: requests.TooManyRedirects; Too many redirects"
    except requests.exceptions.ConnectTimeout:
        return "Err: requests.ConnectTimeout; The request timed out while trying to connect to the remote server"
    except requests.exceptions.ConnectionError:
        return "Err: requests.ConnectionError; A Connection error occurred"
    except requests.exceptions.ReadTimeout:
        return "Err: requests.ReadTimeout; The server did not send any data in the allotted amount of time"
    except requests.exceptions.RequestException:
        return "Err: requests.RequestException; There was an ambiguous exception that occurred while handling your request"
    except:
        return "Err: Unknown; An unknown error has occured"
    #except requests.Timeout:
    #    return "Err: requests.Timeout; The request timed out."
    return r.json()

import httpx
from keboola.component import CommonInterface

from src import config


def get_request(url) -> httpx.Response:
    try:
        response = httpx.get(url)
        response.raise_for_status()
        return response
    except httpx.HTTPError as e:
        print(f"Error fetching data from {url}: {e}")
        return None


def main():
    cfg = config.Config()

    if resp := get_request(cfg.endpoint):
        print(resp.request.url, resp.status_code)

    ci = CommonInterface()

    print("User parameters:", ci.configuration.parameters)
    print("Data folder path:", ci.data_folder_path)


main()

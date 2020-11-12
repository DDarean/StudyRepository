import requests

def gen_from_utls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content),resp.status_code,resp.url

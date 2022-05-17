import urllib


def build_url(base_url, path, params) -> str:
    url_parts = list(urllib.parse.urlparse(base_url))
    url_parts[2] = path
    url_parts[4] = urllib.parse.urlencode(params)
    return urllib.parse.urlunparse(url_parts)

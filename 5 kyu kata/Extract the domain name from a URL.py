import re
def domain_name(url):
    res = re.split("://|\.", url)

    if "http" in url and "www" in url:
        return res[2]
    elif "http" in url or "www" in url:
        return res[1]
    else:
        return res[0]

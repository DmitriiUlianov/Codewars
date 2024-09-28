def generate_hashtag(s):
    res = s.split()
    res = [i.lower().capitalize() for i in res]
    res = ''.join(res)
    return "#" + res if len(res) < 140 and len(res) > 0 else False

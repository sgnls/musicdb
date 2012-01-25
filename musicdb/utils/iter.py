def chunk(it, size):
    return map(None, *([iter(it)] * size))

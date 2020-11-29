def get_urls():
    urls = []
    with open('urls.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line.startswith('#'):
                urls.append(line)

    return urls

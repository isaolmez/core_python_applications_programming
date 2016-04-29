from urllib import urlretrieve


def firstNonBlank(lines):
    for line in lines:
        if not line.strip():
            continue
        else:
            return line


def openURL(webPage):
    f = open(webPage)  # Using "file" interface. This acts like an adapter
    lines = f.readlines()
    print firstNonBlank(lines)
    lines.reverse()
    print firstNonBlank(lines)


def download(url='http://www.google.com', process=openURL):
    try:
        retval = urlretrieve(url)[0]
    except IOError, e:
        retval = None

    if retval:
        return process(retval)


if __name__ == "__main__":
    download()

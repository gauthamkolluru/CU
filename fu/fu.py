
def rf(fn, ra=0, binary=False):
    """
    rf  :   Read File
    fn  :   File Name
    ra  :   Read File As
    """
    with open(fn, "rb" if binary else "r") as fp:
        if not binary:
            if ra == 1:
                return fp.readline()
            elif ra == 2:
                return fp.readlines()
        return fp.read()


def wf(fn, fd, wa=0, binary=False):
    """
    wf  :   Write File
    fn  :   File Name
    fd  :   File Data
    wa  :   Write File As
    """
    with open(fn, "wb" if binary else "w") as fp:

        if wa == 1 or isinstance(fd, list) and not binary:
            return fp.writelines()

        return fp.write()


if __name__ == "__main__":
    print(rf("C:\\utils\\fu\\rough.json"))
    print(rf("C:\\utils\\fu\\rough.json", ra=1))
    print(rf("C:\\utils\\fu\\rough.json", ra=2))

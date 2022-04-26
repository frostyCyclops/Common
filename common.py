def seek_to(fs, pattern):
    """Searches a given binary stream for the given pattern returning an int pointer to just after the found position.

    Args:
        fs (binary stream): Binary I/O to the file about to be read.
        pattern (bytes): The pattern to be searched for.

    Returns:
        int: A pointer to the location right after the found pattern.  Or will return None if the binary stream reaches
        the end of the file.

    """
    size = len(pattern)
    try:
        current = fs.read(size)
        while current != pattern:
            if not len(current) or len(current) != size:
                raise EOFError
            fs.seek(1 - size, 1)
            current = fs.read(size)
        return fs.tell()
    except EOFError:
        return None

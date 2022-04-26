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


def get_current_zulu():
    """Gets current time in zulu format.

    Returns:
        str: formatted string of the current zulu time.

    """
    return datetime.datetime.utcnow().isoformat(timespec='seconds')


def find_files(path, file_type):
    """Will search a given file path recursively for all files with the given extension.

    Args:
        path (str): File path to the search directory.  Will search this directory and all subdirectories recursively.
        file_type (str): Pattern to search.  Must be an extension without the dot.

    Returns:
        list: list of strings representing paths to the found files.  Or an empty list if nothing is found.

    """
    if os.path.isdir(path):
        return glob.glob(os.path.join(path, '**', '*' + file_type), recursive=True)
    elif os.path.splitext(path)[1] == file_type:
        return [path]
    else:
        return []


def print_message(msg, mode='info'):
    """Standardized print message for the program.

    Args:
        msg (str): The message to be printed.
        mode (str): The type of message to be outputted to the user.  Defaults to an info message.

    """
    if mode == 'error':
        print(('[!] ' + msg), file=sys.stderr)
    elif mode == 'warning':
        print(('[?] ' + msg), file=sys.stderr)
    else:
        print(('[#] ' + msg))


def get_geofetch_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return sys.path[0]


def get_file_name(path, extension=False):
    """Given a file path will split/splitext the name of the file.

    Example:
        from '/Documents/test.txt' it returns 'test'.

    Args:
        path (str): File path or file.
        extension (bool): If true the return will include the files extension.  Defaults to False.

    Returns:
        str: A string of the file name from the path given.

    """
    if extension:
        return os.path.split(path)[1]
    else:
        return os.path.splitext(os.path.split(path)[1])[0]


def test_float(num, default=None):
    try:
        return float(num)
    except ValueError:
        return default
    except TypeError:
        return default


def hash_file(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()


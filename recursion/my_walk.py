import os

# function assumes path it gets is a directory
def my_walk(path):
    dirs = []
    files = []
    for e in os.listdir(path):
        if os.path.isdir(os.path.join(path, e)):
            dirs.append(e)
        else:
            files.append(e)
    yield (path, dirs, files)
    if dirs:
        for e in my_walk(os.path.join(path, dirs.pop())):
            yield e

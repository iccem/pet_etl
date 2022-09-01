import os

def upload(file):
    path_archive = os.path.join('archive', file + '.backup')
    os.rename(file, path_archive)

import os


def get_secrets(item):
    return os.environ[item].encode('utf-8')

VERSION = (2, 0, 0)
__version__ = VERSION


def get_version():
    return ".".join(VERSION)


default_app_config = 'django_hstore.apps.HStoreConfig'

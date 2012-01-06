from django.contrib.gis.db.backends.postgis import *
from django.contrib.gis.db.backends.postgis.base import DatabaseWrapper as PostgisDatabaseWrapper
from .operations import PatchedOperations


class DatabaseWrapper(PostgisDatabaseWrapper):
    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.ops = PatchedOperations(self)

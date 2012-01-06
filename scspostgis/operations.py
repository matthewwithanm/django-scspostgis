from django.contrib.gis.db.backends.postgis.operations import PostGISOperations
from .adapter import PatchedAdapter


class PatchedOperations(PostGISOperations):
    Adapter = PatchedAdapter
    Adaptor = Adapter

"""
Subclass of PostGISAdapter that fixes issues with escaping.
See https://code.djangoproject.com/ticket/16778

"""

from psycopg2 import Binary
from django.contrib.gis.db.backends.postgis.adapter import PostGISAdapter


class PatchedAdapter(PostGISAdapter):
    def __init__(self, *args, **kwargs):
        super(PatchedAdapter, self).__init__(*args, **kwargs)
        self._adapter = Binary(self.ewkb) 

    def prepare(self, conn):
        # Pass the connection to the adapter: this allows escaping the binary
        # in the style required by the server's standard_conforming_string setting.
        self._adapter.prepare(conn)

    def getquoted(self):
        "Returns a properly quoted string for use in PostgreSQL/PostGIS."
        # psycopg will figure out whether to use E'\\000' or '\000'
        return 'ST_GeomFromEWKB(%s)' % self._adapter.getquoted()

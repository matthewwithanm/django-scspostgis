A bug in Django 1.3's PostGIS adapter makes it unusable when
`standard_conforming_string` is enabled, which is the default for PostgreSQL
9.1.

[A patch][0] is available, but those not inclined to run a patched version of
Django can use this package instead. Just install it and then update your
database settings:

	DATABASES = {
	    'default': {
	        'ENGINE': 'scspostgis',
	        ...
	    }
	}

If you're using [South][1], you'll also need the following setting:

	SOUTH_DATABASE_ADAPTERS = {
	    'default': 'south.db.postgresql_psycopg2',
	}

If you upgrade to Django 1.4, you should uninstall `scspostgis` and use the
standard 'django.contrib.gis.db.backends.postgis' engine.


[0]: https://code.djangoproject.com/ticket/16778
[1]: http://south.aeracode.org

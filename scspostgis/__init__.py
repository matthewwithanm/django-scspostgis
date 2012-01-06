from django import VERSION as v

if v[0] > 1 or v[0] == 1 and v[1] > 3:
    print 'WARNING: Versions of Django > 1.3 do not require scspostgis. You' \
            ' should uninstall it and use the standard' \
            ' \'django.contrib.gis.db.backends.postgis\' engine.'

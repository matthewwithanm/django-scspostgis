import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.rst')

setup(
    name='django-scspostgis',
    version='1.0',
    description='A PostGIS db backend that works with standard_conforming_strings.',
    long_description=README,

    author='Matthew Dapena-Tretter',
    author_email='m@tthewwithanm.com',
    packages=[
        'scspostgis',
    ],
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

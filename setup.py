import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.markdown')

setup(
    name='django-scspostgis',
    version='0.1',
    description='A PostGIS db backend that works with standard_conforming_strings.',
    long_description=README,

    author='Matthew Tretter',
    author_email='matthew@exanimo.com',
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

from os.path import join, dirname

from setuptools import setup


setup(
    name='rebranch-django-sms-ru',
    version=0.1,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author='Rebranch',
    package_data={},
    dependency_links=[u'https://github.com/rebranch/rebranch-sms-ru.git#egg=rebranch-sms-ru'],
    install_requires=[u'requests',],
    url='https://github.com/rebranch/rebranch-django-sms-ru.git'
)
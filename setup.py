from os.path import join, dirname

from setuptools import setup


setup(
    name='rebranch_django_sms_ru',
    version=0.1,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author='Rebranch',
    package_data={},
    install_requires=[u'requests'],
    dependency_links=[u'https://github.com/rebranch/rebranch-sms-ru.git#egg=rebranch_sms_ru'],
    url='https://github.com/rebranch/rebranch-django-sms-ru.git'
)
from os.path import join, dirname

from setuptools import setup


setup(
    name='rebranch_sms_ru',
    version=0.1,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author='Rebranch',
    package_data={},
    install_requires=[u'requests'],
    url='https://Franz_ru@bitbucket.org/Franz_ru/rebranch-deployment.git'
)
from setuptools import setup

setup(
    name='BookManger',
    packages=['BookManager'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
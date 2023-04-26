import os

from setuptools import setup, find_namespace_packages


try:
    with open(
        os.path.join(os.path.dirname(__file__), 'VERSION')
    ) as version_file:
        VERSION = version_file.read().strip()
except:
    VERSION = '0.0.1'


setup(
    name="formatting_utils",
    version=VERSION,
    author="ClinCard Labs",
    author_email="clincard@greenphire.com",
    description="A utility",
    long_description_content_type="text/markdown",
    # url="https://github.com/Greenphire/ClinCardAutomatedSync",
    packages=find_namespace_packages(include=['mynamespace.*']),
    install_requires=[
        'requests==2.27.1'
    ]
)

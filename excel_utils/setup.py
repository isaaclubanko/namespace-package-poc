import os

from setuptools import setup, find_namespace_packages


try:
    with open(
        os.path.join(os.path.dirname(__file__), 'VERSION')
    ) as version_file:
        VERSION = version_file.read().strip()
except:
    VERSION = '0.0.8'


setup(
    name="excel_utils",
    version=VERSION,
    author="ClinCard Labs",
    author_email="clincard@greenphire.com",
    description="A utility",
    long_description_content_type="text/markdown",
    packages=find_namespace_packages(include=['namespace_excel.*']),
    zip_safe=False,
    install_requires=[
        'openpyxl==3.0.10',
        'pandas==1.3.5'
    ]
)

# setup.py

from setuptools import setup, find_packages
import os

VERSION = '0.2'
DESCRIPTION = 'Extracts visual table data from powerbi report'
LONG_DESCRIPTION = 'A package that exports the visual table data into csv'

setup(
    name='pbi_vizdata',
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    py_modules = ['render_pbi_report','get_visual_data'],
    packages=find_packages(),
    keywords=['python', 'powerbi','powerbiclient'],
    install_requires=[
        'os',
        'time',
        'pandas',
        'shutil',
        're',
        'powerbiclient'
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Powerbi Developers, Data analyst, Gen AI developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
    author = "Nitin Satish",
    zip_safe=False
)

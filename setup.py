
import sys
from os import path

import setuptools

if sys.version_info < (3, 0):
    sys.exit('Sorry, Python < 3.0 is not supported')

description = "A django survey app, based on and compatible with "
"\"django-survey\". You will be able to migrate your data from an ancient "
"version of django-survey, but it has been ported to python 3 and you can "
"export results as CSV or PDF using your native language."


def add_package(package_list, package):
    package = package.replace("\n", "").split("#")[0]
    if package:
        package_list.append(package)


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

with open("requirements.txt", "r") as fh:
    require = fh.readlines()
require = [x.strip() for x in require]

with open("requirements_dev.txt", "r") as fh:
    extras_require = fh.readlines()
# Remove the first two line (-r requirements.txt and a blank line)
extras_require = {'dev': [x.strip() for x in extras_require[2:]]}

setuptools.setup(
    name="django-survey-and-report",
    version="1.3.1",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Pierre SASSOULAS",
    author_email="pierre.sassoulas@gmail.com",
    license="AGPL",
    url="https://github.com/Pierre-Sassoulas/django-survey",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Natural Language :: French",
        "Natural Language :: Japanese",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        "Framework :: Django",
    ],
    install_requires=require,
    extras_require=extras_require,
)

#!/usr/bin/env python3
import os
import re
import shutil
import sys
from io import open

from setuptools import find_packages, setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

# This check and everything above must remain compatible with Python 2.7.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        """
==========================
Unsupported Python version
==========================

This version of DynaPortal requires Python {}.{}, but you're trying
to install it on Python {}.{}.

This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:

    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install dynaportal

This will install the latest version of DynaPortal which works on
your version of Python.
""".format(
            *(REQUIRED_PYTHON + CURRENT_PYTHON)
        )
    )
    sys.exit(1)


def read(f):
    with open(f, "r", encoding="utf-8") as file:
        return file.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    print(os.path.join(package, "__init__.py"))
    init_py = open(os.path.join(package, "__init__.py")).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version("dynaportal")


if sys.argv[-1] == "publish":
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    if os.system("twine check dist/*"):
        print("twine check failed. Packages might be outdated.")
        print("Try using `pip install -U twine wheel`.\nExiting.")
        sys.exit()
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    shutil.rmtree("dist")
    shutil.rmtree("build")
    shutil.rmtree("dynaportal.egg-info")
    sys.exit()


setup(
    name="dynaportal",
    version=version,
    url="https://github.com/loghmanb/dynaportal",
    license="BSD",
    description="Dynamic portal for Django",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Loghman Barari",
    author_email="loghmanb@gmail.com",  # SEE NOTE BELOW (*)
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=["django>=3.0", 'backports.zoneinfo;python_version<"3.9"'],
    package_data={"dynaportal": ["templates/dynaportal/**", "static/**"]},
    python_requires=">=3.6",
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP",
    ],
    project_urls={
        "Source": "https://github.com/loghmanb/dynaportal",
    },
)

# (*) Please direct queries to the discussion group, rather than to me directly
#     Doing so helps ensure your question is helpful to other users.
#     Queries directly to my email are likely to receive a canned response.
#
#     Many thanks for your understanding.

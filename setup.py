# ----------------------------------------------------------------------
# setup.py -- v20 setup script
#
# Copyright (C) 2016, OANDA Corporation.
# ----------------------------------------------------------------------

import os
import codecs

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


def main():
    # setup dictionary
    setup_options = {
        "name": "v20",
        "version": "3.0.25.0",
        "description": "OANDA v20 bindings for Python",
        "long_description": read("README.rst"),
        "long_description_content_type": "text/x-rst",
        "author": "OANDA Corporation",
        "author_email": "api@oanda.com",
        "url": "https://github.com/oanda/v20-python",
        "project_urls": {
            "Bug Tracker": "https://github.com/oanda/v20-python/issues",
            "Documentation": "http://developer.oanda.com/rest-live-v20/introduction",
            "Source Code": "https://github.com/oanda/v20-python",
        },
        "license": "MIT",
        "install_requires": ["requests", "ujson", "PyYAML"],
        "packages": ["v20"],
        "data_files": [("", ["LICENSE", "ChangeLog"])],
        "platforms": ["any"],
        "zip_safe": True,
        "classifiers": [
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.13",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.10",
            "Topic :: Software Development",
            "Topic :: Software Development :: Libraries",
            "Topic :: Utilities",
        ],
    }

    # Run the setup
    setup(**setup_options)


if __name__ == "__main__":
    main()

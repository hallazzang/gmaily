import os
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gmaily",
    version="0.0.3",
    description="Unofficial Gmail python client with pythonic API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hallazzang/gmaily",
    author="Hanjun Kim",
    author_email="hallazzang@gmail.com",
    license="MIT",
    python_requires=">=3.5",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Communications :: Email",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

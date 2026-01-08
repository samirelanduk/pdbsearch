from setuptools import setup

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="pdbsearch",
    version="0.5.0",
    description="A library for searching the RCSB PDB database",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://pdbsearch.samireland.com",
    author="Sam Ireland",
    author_email="mail@samireland.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    keywords="chemistry bioinformatics proteins biochemistry molecules PDB MMCIF",
    packages=["pdbsearch"],
    python_requires="!=2.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "pdbsearch=pdbsearch.__main__:main",
        ],
    },
)

from setuptools import setup, find_packages

setup(
    name="ebay_data_db",
    version="1.0.0",
    author="Vardaan Kapoor",
    author_email="vardaan123454321@gmail.com",
    description="A Python package for managing and querying eBay auction data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ervardaan/ebay_data_db",
    packages=find_packages(exclude=["tests", "data", "scripts"]),
    include_package_data=True,
    install_requires=[
        "pandas",
        "jupyter"
        "sqlite3",  # Add other dependencies here, e.g., pandas, numpy
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "run_parser=ebay_data_db.parser:main",  # Adjust main function call as needed
        ],
    },
)

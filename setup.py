from setuptools import setup, find_packages

setup(
    name="csv2sql",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "sqlalchemy",
        "click",
    ],
    extras_require={
        "mysql": ["mysqlclient"],
        "postgresql": ["psycopg2-binary"],
        "sqlite": [],
        "oracle": ["cx_Oracle"],
        "mssql": ["pyodbc"],
    },
    entry_points={
        "console_scripts": [
            "csv2sql=csv2sql.cli:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="Convert CSV files to SQL create table and insert statements",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/csv2sql",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 
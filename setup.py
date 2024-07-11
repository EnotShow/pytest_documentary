from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pytest_documentary",
    long_description=long_description,
    long_description_content_type='text/markdown',
    version="0.1.0",
    description="A simple pytest plugin to generate test documentation",
    packages=["pytest_documentary"],
    entry_points={
        "pytest11": [
            "pytest_documentary = pytest_documentary.plugin"
        ],
    },
    install_requires=[
        "pytest",
        "pandas",
        "openpyxl",
    ],
    classifiers=["Framework :: Pytest"],
)

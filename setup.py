from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e."

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [r.strip() for r in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

setup(
    name="TunaDocs",
    version="0.1.0",
    author="Maftuna",
    author_email="tunchik2408@gmail.com",
    description="AI-based document summarizer and visualizer for academic papers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/maftuna2408/TunaDocs",
    project_urls={
        "Source": "https://github.com/maftuna2408/TunaDocs",
    },
    packages=find_packages(where="source"),
    package_dir={"": "source"},
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.10,<3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

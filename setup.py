from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = file.read().splitlines()
        # Remove "-e ." if present
        requirements = [req for req in requirements if req.strip() != "-e ."]
    return requirements

setup(
    name="sensor",
    version="0.0.1",
    author="utkarsh",
    author_email="teamutkarsh22@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),  # <- this works now
)

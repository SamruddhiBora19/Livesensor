from setuptools import find_packages, setup
from typing import List

def get_requiements() -> list[str]:

    requirements_list:list[str]=[]
    return requirements_list


setup(
    name="sensor",
    version="0.0.1",
    author="samruddhi",
    packages=find_packages(),
    install_requires=get_requiements()
 )
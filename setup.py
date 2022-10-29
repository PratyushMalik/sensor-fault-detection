from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    
    return requirement_list


setup(
    name="sensor",
    version="0.0.1",
    author="malik",
    author_email="pratyush0410@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
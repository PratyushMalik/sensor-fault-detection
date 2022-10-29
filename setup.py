from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    HYPHEN_E_DOT = "-e ."
    with open("requirements.txt") as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
    
    return requirement_list


setup(
    name="sensor",
    version="0.0.1",
    author="malik",
    author_email="pratyush0410@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
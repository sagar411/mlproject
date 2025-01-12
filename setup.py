# setup.py is used to package 
# Python projects, define metadata, and specify 
# dependencies. It allows your project to be 
# installed as a package and used in pipelines or other environments.
from typing import List
from setuptools import find_packages,setup



def get_requirements(file_path:str)-> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","")for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")


setup(
    name="mlproject",
    version='0.0.1',
    author="sagar",
    author_email="sagar.sunar411@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),
    )





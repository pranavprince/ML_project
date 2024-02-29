from setuptools import setup, find_packages
from typing import List
hypen_e_dot='-e .'
def get_packages_installed(filename:str)->List[str]:

    requirements=[]
    with open(filename) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements

setup(
    name='ML_project',
    version='0.0.1',
    author='Pranav_Prince',
    author_email='pranavprince06@gmail.com',
    packages=find_packages(),
    install_requires=get_packages_installed('requirements.txt')
)
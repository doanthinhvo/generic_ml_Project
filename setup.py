from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(filename:str)->List[str]:
    '''
    this function will return the list of requirements
    :'''
    requirements = []
    with open (filename, 'r') as file_obj:
        for line in file_obj.readlines():
            if HYPEN_E_DOT in line:
                continue
            requirements.append(line.strip())
    return requirements
setup(
    name='ml_project',
    version='0.0.1',
    author='DTV',
    author_email='blvrxdnthnhv@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    )
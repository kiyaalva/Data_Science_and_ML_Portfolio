from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    this fucntion will return the required packages in list format
    '''
    hypen = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if hypen in requirements:
            requirements.remove(hypen)
    return requirements


setup(
name= 'Machine Learning Porject 1',
version = '0.0.1',
author = 'Kiran Shridhar Alva',
author_email = 'kiran.salva@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
    )
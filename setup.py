from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will returnhe list of requirments
    '''
    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('/n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        


setup(
name = 'MLproject',
version = '0.0.1',
author = 'Himanshu',
author_email='soni.himanshu2627@gmail.com',
package = find_packages(),
install_requires=get_requirements('requirements.txt')
)

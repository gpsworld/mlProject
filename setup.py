from setuptools import find_packages, setup
from typing import List
hyphen_e_dot = "-e ."  # for local development with edit
def get_requirments(file_path:str)->List[str]:
  '''
  this function will return the list of requirments
  '''
  requirments =[]
  with open(file_path) as file_obj:
    requirments=file_obj.readlines()
    requirments = [req.replace("\n", " ") for req in requirments]

    if hyphen_e_dot in requirments:
      requirments.remove(hyphen_e_dot)
  return requirments


setup(
name = 'mlproject',
version = '0.0.1',
author = 'gpsworld',
author_email= 'gpsworld03@gmail.com',
packages=find_packages(),
isntall_requires = get_requirments('requirements.txt')

)
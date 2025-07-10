'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    #this function will return list of requirements
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from files
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty line and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file is not found")

    return requirement_lst
#Setup at last of project
# setup(
#     name="Network Security",
#     version="0.0.1",
#     author="Jay",
#     author_email="shashwatxiia1415@gmail.com",
#     packages=find_packages(),
#     install_requires=get_requirements()
# )

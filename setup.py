from setuptools import find_packages, setup

req_list=[]
def requirements(file_name):
    with open(file_name,"r") as file :
        for line in file:
            req_list.append(line.strip())
    return req_list

setup(
    name="Movie Recommendation",
    version="0.0.1",
    author="Chirag Jain",
    author_email="cjain16202@gmail.com",
    packages=find_packages(),
    install_requires=requirements("requirement.txt")
)
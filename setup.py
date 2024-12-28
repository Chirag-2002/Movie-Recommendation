from setuptools import find_packages, setup



setup(
    name="Movie Recommendation",
    version="0.0.1",
    author="Chirag Jain",
    author_email="cjain16202@gmail.com",
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn']
)
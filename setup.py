from setuptools import setup, find_packages

setup(
    author='Group 5',
    description='CLV prediction',
    name='clv',  # package name
    version='0.1.0',
    packages=find_packages(include=['clv','clv.*']),
    
)
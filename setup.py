from setuptools import setup, find_packages

setup(
    author='Group 5',
    url='https://github.com/yeranosyanvahan/ma_group_project',
    description='CLV prediction',
    name='SocraCLV',
    version='0.9.9',
    packages=find_packages(include=['clv','clv.*']),
)
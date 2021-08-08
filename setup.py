from setuptools import setup, find_packages

setup(
   name='origami',
   version='1.0',
   author='EAFA0',
   author_email='TobiichiOrigami.d@gmail.com',
   packages=find_packages(exclude=("example", "example.*")) 
)
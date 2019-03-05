from setuptools import setup

with open('DESCRIPTION.txt') as file:
    long_description = file.read()


setup(name='change_case_object',
      version='1.0.0',
      description='Change case of dictionary keys',
      long_description=long_description,
      url='https://github.com/ashutoshcipher/change_case_object',
      author='Ashutosh Gupta',
      author_email='ashutoshgupta118@gmail.com',
      license='MIT',
      install_requires=[],
      keywords='dictionary keys case change'
      )
from setuptools import setup

setup(name='packages',
      version='1.1',
      description='Python module for Jönköping University Librarys various helper packages',
      url='https://github.com/JonkopingUniversityLibrary/python_packages',
      author='Gustav Lindqvist',
      author_email='gustav.lindqvist@ju.se',
      license='MIT',
      packages=[
          'logger',
          'config_loader',
      ],
      zip_safe=False)

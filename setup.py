from setuptools import setup,find_packages

setup(name="census-income",
      version="0.0.1",
      author="Deepika",
      author_email="deepikapatil2022@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )
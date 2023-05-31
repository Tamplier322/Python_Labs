from setuptools import setup, find_packages


setup(
    name="ShishcovSerializer",
    version="1.0",
    description="module for python serialization(JSON, XML)",
    url="https://github.com/Tamplier322/Python_Labs/tree/Lab3",
    author="Shishcov Slava",
    author_email="slavashishcov1@mail.ru",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["Serializers"],
    include_package_data=True
)
from setuptools import setup, find_packages

setup(
    name="BBH_SIM",
    version="0.1",
    description="Binary Black Hole Simulation Package",
    author="Mohamed Elashri",
    author_email="bbh@elashri.com",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
    ],
)

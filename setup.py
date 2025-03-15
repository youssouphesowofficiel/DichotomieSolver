from setuptools import setup, find_packages

setup(
    name="dichotomieSolver",
    version="1.0.0",
    description="Solveur numérique par dichotomie",
    author="Youssouphe Sow",
    author_email="youssouphesow1111@gmail.com",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "dichotomie=dichotomiesolver.cli:main",
        ],
    },
)

from setuptools import setup

setup(
    name='nounseed',
    version='1.0',
    description='A package for generating and storing project ideas',
    author='psibir',
    packages=['nounseed'],
    install_requires=[
        'argparse',
        'Pathlib'
    ],
    entry_points={
        'console_scripts': [
            'nounseed = nounseed.nounseed:main'
        ]
    }
)
from setuptools import setup, find_packages

setup(
    name='my_package',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pyspark==3.4.0',
        'py4j==0.10.9.7'
    ],
    entry_points={
        'console_scripts': [
            'my_script=my_package.src.main:main'
        ]
    }
)

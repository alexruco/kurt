# setup.py
from setuptools import setup, find_packages

setup(
    name='kurt',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'hellen @ git+https://github.com/alexruco/hellen.git#egg=hellen',
        'virginia @ git+https://github.com/someuser/virginia.git#egg=virginia',
        'dourado @ git+https://github.com/alexruco/dourado.git#egg=dourado'
    ],
    entry_points={
        'console_scripts': [
            'kurt=kurt.main:main'
        ],
    },
    author='Alex Ruco',
    author_email='alex@ruco.pt',
    description='A module for processing web links using hellen, virginia, and dourado',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/alexruco/kurt',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

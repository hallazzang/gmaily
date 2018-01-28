import os
from setuptools import setup

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def get_long_description(path):
    with open(os.path.join(BASE_PATH, path)) as f:
        return f.read()

setup(
    name='gmaily',
    version='0.0.2',
    url='https://github.com/hallazzang/gmaily',
    license='MIT',
    author='Hanjun Kim',
    author_email='hallazzang@gmail.com',
    description='Pythonic Gmail client',
    long_description=get_long_description('README.rst'),
    py_modules=['gmaily'],
    python_requires='>=3',
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

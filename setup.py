from setuptools import setup
pip install -e .
from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/MarcRatkovic/module',
    author='Marc Ratkovic',
    author_email='marc.ratkovic@gmail.com',

    py_modules=['my_pip_package'],
)

from distutils.core import setup

setup(name='ExamplePackage',
      version='1.0',
      description='An example package to test before putting in actual modules',
      author='Nick Zhu',
      author_email='nz3424@princeton.edu',
      url='https://github.com/MarcRatkovic/module',
      packages=['distutils', 'distutils.command'],
     )
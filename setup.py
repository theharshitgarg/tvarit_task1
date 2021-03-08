
from setuptools import setup, find_packages
from commandline_parser.config import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='commandline_parser',
    version=VERSION,
    description='This app is custom adder for tvarit company',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Harshit Garg',
    author_email='harshitgagrmnit@gmail.com',
    url='https://github.com/mathagician/customadder',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'addition': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        addition = commandline_parser.app:main
    """,
    setup_requires=['pytest-runner', 'wheel'],
    tests_require=['pytest'],
)


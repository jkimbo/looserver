import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
make_abs = lambda fn: os.path.join(here, fn)


def get_requirments(filename):
    with open(filename, 'r') as file_handle:
        requirements = []
        for requirement in file_handle:
            requirement = requirement.strip()

            # skip blank lines and comments
            if not requirement or requirement.startswith('#'):
                continue
            requirements.append(requirement)
    return requirements


requirements = get_requirments(make_abs('requirements.txt'))


setup(
    name='looserver',
    packages=find_packages(exclude=['tests', 'tests.*']),
    version='0.0.1',
    author='onefinestay',
    author_email='engineering@onefinestay.com',
    url='https://github.com/onefinestay/looserver',
    install_requires=requirements,
    license='Apache License, Version 2.0',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    description='Check your loo status',
    long_description=open(make_abs('README.rst')).read(),
    include_package_data=True,
    zip_safe=False,
    entry_points='''
        [console_scripts]
        looserver=looserver.scripts:cli
    ''',
)

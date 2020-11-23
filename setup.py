import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

setup(
    name='sylk_parser',
    version='0.5',
    description='Basic SLK (sylk) to CSV parser',
    long_description=README,
    long_description_content_type='text/rst',
    license='GPLv3',
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Intended Audience :: Developers',
    ],
    author='Majerti',
    author_email='equipe@majerti.fr',
    url='https://github.com/majerteam/sylk_parser',
    keywords='parser csv slk sylk',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

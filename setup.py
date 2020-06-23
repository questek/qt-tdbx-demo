from distutils.core import setup

import setuptools

setup(
    name='qt_tdbx',
    version='0.1.0',
    author='QuesTek Innovations LLC',
    author_email='cniu@questek.com',
    description="QuesTek's package for CALPHAD UQ with TDBX format",
    url='https://github.com/questek/qt-tdbx-demo',
    install_requires=[
        'pandas',
        'sympy',
        'tc_python'
    ],
    packages=setuptools.find_packages(),
    license='apache-2.0'
)

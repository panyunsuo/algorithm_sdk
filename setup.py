"""
@File    :   setup.py.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/7/14 16:24
------------
@Model Name:   安装命令:python setup.py install
"""
from setuptools import find_packages, setup

setup(
    name="algorithm_sdk",
    version="1.2.0",
    description="idphoto",
    long_description="algorithm sdk",
    license="MIT Licence",
    author="panso",
    author_email="panrs@venpoo.com",
    packages=find_packages(where='.', exclude=(), include=('*',)),
    include_package_data=True,
    platforms="any",
    install_requires=['requests']
    )

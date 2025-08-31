from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import os

from setuptools import setup, find_packages

# 更新依赖项，确保包含 recbole 作为依赖
install_requires = [
    'recbole>=1.0.0',  # 添加 recbole 作为依赖
    'numpy>=1.17.2', 
    'torch>=1.7.0', 
    'scipy>=1.6.0',  # 移除了固定版本，使用 >=
    'pandas>=1.0.5', 
    'tqdm>=4.48.2',
    'colorlog>=4.7.2',  # 移除了固定版本
    'colorama>=0.4.4',  # 移除了固定版本
    'scikit_learn>=0.23.2', 
    'pyyaml>=5.1.0', 
    'matplotlib>=3.1.3'
]

setup_requires = []

extras_require = {
    'hyperopt': ['hyperopt>=0.2.4']
}

classifiers = ["License :: OSI Approved :: MIT License"]

# 更新描述
long_description = 'RecBole-CDR is a cross-domain recommendation extension for RecBole, ' \
                   'developed based on Python and PyTorch. It provides a unified framework ' \
                   'for cross-domain recommendation algorithms. ' \
                   'View RecBole-CDR GitHub page for more information: ' \
                   'https://github.com/RUCAIBox/RecBole-CDR'

# Readthedocs requires Sphinx extensions to be specified as part of
# install_requires in order to build properly.
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    install_requires.extend(setup_requires)

setup(
    name='recbole_cdr',  # 修改包名
    version='0.1.0',  # 设置适当的版本号
    description='A cross-domain recommendation extension for RecBole',  # 更新描述
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/RUCAIBox/RecBole-CDR',  # 更新URL
    author='RecBoleTeam',  # 可以保留或更新作者信息
    author_email='recbole@outlook.com',  # 可以保留或更新邮箱
    packages=[
        package for package in find_packages()
        if package.startswith('recbole_cdr')  # 修改为查找 recbole_cdr 开头的包
    ],
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=setup_requires,
    extras_require=extras_require,
    zip_safe=False,
    classifiers=classifiers,
)

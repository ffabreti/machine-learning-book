# coding: utf-8

#ERRATA: needed to rename python file so that you don't get
#        a circular reference error from import below

import sys
from python_environment_check import check_packages

sys.path.insert(0, '..')

d = {
    'numpy': '1.21.2',
    'scipy': '1.7.0',
    'matplotlib': '3.4.3',
    'sklearn': '1.0',
    'pandas': '1.3.2'
}
check_packages(d)

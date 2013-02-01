# -*- Mode: Python -*-

#SHRAPNEL = '/Users/rushing/src/shrapnel/shrapnel'
SHRAPNEL = ''

import sys

if not SHRAPNEL:
    sys.stderr.write (
        "\nPlease set the value of SHRAPNEL at the top of setup.py\n"
        )
    sys.exit (-1)

#from distribute_setup import use_setuptools
#use_setuptools()
from setuptools import setup

try:
    from Cython.Distutils import build_ext
    from Cython.Distutils.extension import Extension
except ImportError:
    sys.stderr.write (
        '\nThe Cython compiler is required to build Shrapnel.\n'
        '  Try "pip install cython"\n'
        '  *or* "easy_install cython"\n'
        )
    sys.exit (-1)

# these are needed by _coro.pxd
compile_time_env = {
    'COMPILE_LZO' : False,
    'COMPILE_LZ4' : False,
    }

import os
PJ = os.path.join

cython_include_dirs = [
    SHRAPNEL,
    PJ (SHRAPNEL, 'pyrex'),
    ]

server_ext = Extension (
    'echo_server',
    ['echo_server.pyx'],
    cython_include_dirs=cython_include_dirs,
    cython_compile_time_env = compile_time_env,
    )

setup (
    name              = 'pure_cython_server',
    version           = '0.1',
    author            = 'Sam Rushing',
    description       = "Shrapnel Server Demo in Cython",
    license           = "Simplified BSD",
    keywords          = "cython shrapnel",
    install_requires  = ['coro'],
    dependency_links  = ['http://github.com/ironport/shrapnel.git#egg=shrapnel'],
    zip_safe          = False,
    ext_modules = [server_ext],
    cmdclass={'build_ext': build_ext},
    )

This is a sample application showing how to build a 'pure cython' extension module for shrapnel.
It implements an echo server.

To build:

1) edit the location of your shrapnel distribution in setup.py
2) python setup.py build_ext --inplace
3) python run.py

To test:
$ telnet localhost 9000
type some stuff
type some stuff
^]quit<return>


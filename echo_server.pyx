# -*- Mode: Python -*-

import coro
cimport coro._coro as _coro

cdef class echo_server:
    cdef public int port
    cdef public _coro.sock s
    def __init__ (self, int port):
        self.port = port
        self.s = _coro.sock (_coro.AF_INET, _coro.SOCK_STREAM)

    def go (self):
        cdef _coro.sock conn
        self.s.bind (('127.0.0.1', self.port))
        self.s.listen (5)
        while 1:
            conn, addr = self.s.accept()
            coro.spawn (self.serve, conn, addr)

    def serve (self, _coro.sock conn, addr):
        cdef bytes block
        while 1:
            block = conn.recv (8000)
            if not block:
                break
            else:
                conn.send (block)

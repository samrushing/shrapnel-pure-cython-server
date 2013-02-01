# -*- Mode: Python -*-

import coro
import echo_server

port = 9000
coro.write_stderr ('starting echo server on port %d\n' % (port,))
server = echo_server.echo_server (port)
coro.spawn (server.go)
coro.write_stderr ('starting event loop\n')
coro.event_loop()
coro.write_stderr ('exited event loop\n')

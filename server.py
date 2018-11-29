import socketserver
import sys
import problem
import flag

class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        clear = True
        self.request.sendall(b'-' * 64 + b'\n')
        result = problem.handler(self.request)
        self.request.sendall(b'-' * 64 + b'\n')
        if result is False:
            self.request.sendall(b'Bye.\n')
            clear = False

        if clear:
            self.request.sendall(b'Congratulations! \n')
            self.request.sendall(flag.FLAG)
            self.request.sendall(b'\n')

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def main(argv):
    host, port = 'localhost', 8000

    if len(argv) == 2:
        port = int(argv[1])
    elif len(argv) >= 3:
        host, port = argv[1], int(argv[2])

    sys.stderr.write('Listening {}:{}\n'.format(host, port))
    server = ThreadedTCPServer((host, port), RequestHandler)
    server.allow_reuse_address = True
    server.serve_forever()

if __name__ == '__main__':
    main(sys.argv)

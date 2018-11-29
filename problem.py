import flag
from binascii import hexlify

def handler(req):
    req.sendall(b'Please your answer. \n\n')
    r = bytes(req.recv(256).decode('ascii').strip('\n').strip('\r'), 'ascii')
    if r == bytes('{}'.format('test'), 'ascii'):
        return True

    return False

if __name__ == '__main__':
    import sys
    handler(sys.stdin.buffer, sys.stdout.buffer)

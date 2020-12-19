from sys import stdout, stdin

stdout.buffer.write(stdin.buffer.read(-1))

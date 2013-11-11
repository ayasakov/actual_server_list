from distutils.core import setup
from subprocess import Popen, PIPE
import argparse

def check_pep8():
    print Popen("pep8 web/", shell=True, stdin=PIPE, stdout=PIPE).stdout.read()

def init_argparser():
    parser = argparse.ArgumentParser(description='Argument for setup.py')
    parser.add_argument('pep8', help='Check pep8', default=None, nargs='*')
    parser.add_argument('unittest', help='Run test', default=None, nargs='*')
    return parser.parse_args()

def tests():
    pass

args = init_argparser()

if args.pep8 and args.unittest is None:
    setup(name='checkList',
          version='1.0',
          py_modules=['listServers'])
else:
    if args.pep8 is not None:
        check_pep8()
    if args.unittest is not None:
        tests()
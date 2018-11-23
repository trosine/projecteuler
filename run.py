#!/usr/bin/env python
"""Initial test of an all encompasing Euler command."""

import argparse
import importlib
import inspect
import timeit


def get_args():
    """Get arguments from command line"""
    parser = argparse.ArgumentParser(description='Run euler problem')
    parser.add_argument('problem', type=int, help='Problem number to run')
    parser.add_argument('args', nargs='*', help='Arguments to problem.main()')
    parser.add_argument(
        '-i',
        '--iter',
        type=int,
        dest='iteration',
        default=1,
        help='Iteration of the problem to run',
        )
    return parser.parse_args()


def run_module(func, args):
    """returns a callable function to be used with timeit"""
    def new_func():
        """Decorated function"""
        if inspect.getargspec(func)[0]:
            func(args)
        else:
            func()
    return new_func


def main():
    """Process stuff"""
    args = get_args()
    module_format = 'problems.e{problem:04d}_{iteration:02d}'
    module_name = module_format.format(**args.__dict__)
    mod = importlib.import_module(module_name)
    timer = timeit.timeit(run_module(mod.main, args.args), number=1)
    print 'SPEED = %0.3f' % timer


if __name__ == '__main__':
    main()

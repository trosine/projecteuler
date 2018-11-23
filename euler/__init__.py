"""Common tools for working with Euler problems"""

import inspect


class Resource(file):
    """Open an Euler resource data file"""

    def __init__(self, filename, mode='r', problem=None):
        if problem is None:
            frame = inspect.stack()[1]
            caller_module = inspect.getmodule(frame[0])
            problem = caller_module.PROBLEM
        if not isinstance(problem, int):
            raise TypeError('problem must be an integer')
        filepath = 'resources/p%03d_%s' % (problem, filename)
        super(Resource, self).__init__(filepath, mode)

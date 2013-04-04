class Verbosity(object):
    """Set the verbosity, and implement a print function dependent on the value.
    """ 
    def __init__(self, verbose):
        def do_print(*args):
            """Print the arguments."""
            for arg in args:
                print arg,
            print

        def do_nothing(*args):
            pass
        
        if verbose:
            self.oseprint = do_print
        else:   
            self.oseprint = do_nothing


__all__ = ['ls',
           'grep',
           'cat',
           'pwd',
           'df',
           'du',]

from subprocess import Popen, PIPE, STDOUT

def command_factory(x):
    def command(*args,**kwargs):
        printOutput = True
        if 'printOutput' in kwargs:
            printOutput = kwargs['printOutput']
        cmd =  x.__name__ + " " + " ".join(map(str,args))
        output = Popen( cmd,
                shell=True,
                stdout=PIPE,
                stderr=STDOUT).communicate()[0]
        if printOutput:
            print output
            return None
        else:
            return output
    return command

@command_factory
def ls(): pass

@command_factory
def grep(): pass

@command_factory
def cat(): pass

@command_factory
def pwd(): pass

@command_factory
def df(): pass

@command_factory
def du(): pass

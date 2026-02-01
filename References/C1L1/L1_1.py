import sys

class redirection(object):

    input = None
    output = None

    def __init__(self, in_obj, out_obj):
        self.input = in_obj
        self.output = out_obj

    def readline(self):
        res = self.input.readline()
        self.output.write(res)
        return res
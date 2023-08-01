import backend.sistema_de_tipos as tables
from antlr4.error.ErrorListener import ErrorListener
from .help import *

class CustomErrorListener(ErrorListener):
    def __init__(self):
        self.ERRORS = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        new_error = tables.Error("Error", line, column,msg)
        self.ERRORS.append(new_error)

class Error:
    def __init__(self):
        self.ERRORS = []
        
    def error(self,message, line=None):

        if line is not None:
            new_error = tables.Error("Error", line, "",message)
            self.ERRORS.append(new_error)
        else:
            new_error = tables.Error("Error", "", "",message)
            self.ERRORS.append(new_error)
    
        #exit(3)


def indx(arr: list, element) -> int:
    try:
        return arr.index(element)
    except ValueError:
        return -1
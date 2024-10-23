import sys
import os

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()   # by _,_,exc_tb trying to access third element of tuple and named it as exc_tb
    filename=exc_tb.tb_frame.f_code.co_filename
    error_message="error occurred and the file name is [{0}] at linenumber [{1}] and error is [{2}] ".format(filename,exc_tb.tb_lineno,str(error))
    return error_message


class SensorException(Exception):    #exception(built_in python) class is inherited

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)

        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):    #converts exception in readable format
        return self.error_message
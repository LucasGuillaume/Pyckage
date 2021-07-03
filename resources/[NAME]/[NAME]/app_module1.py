import logging
import os

def appfunction_of_module1(loglevel, progress_bar,resources):
    logging.info('[INFO] Welcome in [NAME]')
    logging.debug('[DEBUG] Now in appfunction_of_module1() : {}'.format(appfunction_of_module1))
    logging.debug('[DEBUG] loglevel : {}, progress_bar : {}, resources located in {}'.format(loglevel,progress_bar,resources))
    return

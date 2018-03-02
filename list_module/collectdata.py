import csv
import numpy as np
import pandas as pd
def collectdata(x):
    """
        returns 2 lists of time and voltage
        
        :param self: list to be determined and used later
        :type self: list
        
        :return: a list
        :rtype: list
    """
    try:
        import logging
    except ImportError:
        print("Could not import logging module")
        return
    else:
        logging.basicConfig(filename='example.log', level=logging.DEBUG,
                            filemode='w')
    if type(x) is not str:
        logging.error('Watch out!The input should be the name of the csv')
        raise TypeError('TypeError with the input')
    
    with open(x) as f:
        df = pd.read_csv(x, names = ["time", "voltage"])
        logging.info("Returning pandas with time and voltage")
        time = df.time
        time = time.tolist()
        voltage = df.voltage
        voltage = voltage.tolist()
        logging.info("Returning 2 lists of time and voltage")
    
    return time,voltage
        
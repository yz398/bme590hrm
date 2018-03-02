import numpy as np


def time_beats(x, f):
    """
    find the time series for a beat
    the first value of each row is the valid number of the time series

    :param x: the input include information about peak index
    :param f: the input include information for all time
    :raises ImportError:  if the module not found
    :raises TypeError:  if the input is not a list or the input includes string
    :raises ValueError: if the input includes string

    :returns: return a tuple include minimum and maximum of the list
    :rtype: numpy array
    """
    try:
        import logging
    except ImportError:
        print("Could not import logging module")
        return
    else:
        logging.basicConfig(filename='example.log', level=logging.DEBUG,
                            filemode='w')
    if type(x) is not list:
        logging.error('Watch out!The input should be list')
        raise TypeError('TypeError with the inputx')
    if type(f) is not list:
        logging.error('Watch out!The input should be list')
        raise TypeError('TypeError with the inputf')
    if not x:
        logging.warning("Empty list x given")
        return None
    if not f:
        logging.warning("Empty list f given")
        return None
    for val in x:
        try:
            num = float(val)
        except ValueError:
            logging.debug("Type is not able to be cast to float")
            raise ValueError()
        except TypeError as err:
            logging.debug("Erroneous type encountered: {}".format(type(err)))
            raise TypeError()
        else:
            if num == float('inf') or num == float('-inf'):
                raise ValueError()
    nn = len(x)
    interval = []
    for i in range(nn-1):
        interval.append(x[i+1]-x[i])
    l = max(interval)
    temp = np.zeros(shape=(nn-1, l), dtype=float)
    for i in range(nn-1):
        temp[i][0] = x[i+1]-x[i]
        for j in range(int(temp[i][0])-1):
            temp[i][j+1] = f[x[i]+j]
    logging.info("Returning numpy array include time series")
    return temp

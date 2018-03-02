import numpy as np


def detect_peak(x):
    """
    find the peaks of the list of voltages and 
    return peaks value and indexes

    :param x: the input should be a list
    :raises ImportError:  if the module not found
    :raises TypeError:  if the input is not a list or the input includes string
    :raises ValueError: if the input includes string

    :returns: return a tuple include minimum and maximum of the list
    :rtype: (float,float)
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
        raise TypeError('TypeError with the input')
    if not x:
        logging.warning("Empty list given")
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
    detect_value = []
    detect_index = []
    for i in range(len(x)):
        if i == 0 and x[i] >= x[i+1] and x[i] >= x[i+2] and x[i] >0:
            detect_value.append(x[i])
            detect_index.append(i)
        elif i == len(x)-1 and x[i] >= x[i-1] and x[i] >= x[i-2] and x[i] >0:
            detect_value.append(x[i])
            detect_index.append(i)
        elif i <(len(x)-1) and x[i] >= x[i-1] and x[i] >= x[i+1] and x[i] >0:
            detect_value.append(x[i])
            detect_index.append(i)
    interval = []
    for i in range(len(detect_index)-1):
        inter = detect_index[i+1]-detect_index[i]
        if inter >0:
            interval.append(inter)
    detect_v1 = []
    detect_i1 = []
    for i in range(len(interval)):
        if interval[i] < 0.5*np.median(interval):
            if detect_value[i] < detect_value[i+1]:
                detect_v1.append(detect_value[i+1])
                detect_i1.append(detect_index[i+1])
            else:
                detect_v1.append(detect_value[i])
                detect_i1.append(detect_index[i])
        else:
            detect_v1.append(detect_value[i])
            detect_i1.append(detect_index[i])
    if detect_v1[len(detect_v1)-1] != detect_value[len(interval)]:
        detect_v1.append(detect_value[len(interval)])
        detect_i1.append(detect_index[len(interval)])
    detect_i1 = set(detect_i1)
    detect_i1 = list(detect_i1)
    detect_i1.sort()
    peak = [detect_v1, detect_i1]
    logging.info("Returning peak value and indexes") 
    return peak

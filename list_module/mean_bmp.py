def mean_bpm(interval, time):
    """
    find the duration for the sample

    :param x: the input should be a list of peaks
    :raises ImportError:  if the module not found
    :raises TypeError:  if the input is not a list or the input includes string
    :raises ValueError: if the input includes string

    :returns: return a tuple include minimum and maximum of the list
    :rtype: float
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
    period = 60
    num = beats(interval)
    t = duration(time)
    mean_min_bpm = period*num/t
    logging.info("Returning estimate bmp per minute")
    return mean_min_bpm

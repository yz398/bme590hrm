def mean_bpm(x,f):
    """
    find the number of beats per minute

    :param x: the input should be a list of peaks
    :param f: the input should be a list of time
    :raises ImportError:  if the module not found
    :raises TypeError:  if the input is not a list or the input includes string
    :raises ValueError: if the input includes string

    :returns: return the estimate number
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
    period = 60
    num = beats(x)
    t = duration(f)
    mean_min_bpm = period*num/t
    logging.info("Returning estimate bmp per minute")
    return mean_min_bpm
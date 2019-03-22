import dateutil.parser



def check_time_format(time):
    try:
        print("set from time: {0}".format(time))
        dateutil.parser.parse(time)
        return time
    except Exception as e:
        print("from_time could not be parsed: {0}".format(str(e)))
        raise e
    return

def time_to_array(time):
    time_array = [None] * 4

    time_array[0] = (time.minute / 10) % 10
    time_array[1] = time.minute % 10
    time_array[2] = (time.sescond / 10) % 10
    time_array[3] = time.second % 10

    return time_array
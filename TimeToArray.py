
def time_to_array(time):
    time_array = [None] * 4

    time_array[0] = (time.hour // 10) % 10
    time_array[1] = time.hour % 10
    time_array[2] = (time.minute // 10) % 10
    time_array[3] = time.minute % 10

    return time_array
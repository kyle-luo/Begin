# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

def measure(m):
    if m == 'kb':
        return 2 ** 10      # one kilobit
    elif m == 'kB':
        return 2 ** 10 * 8  # one kilobyte
    elif m == 'Mb':
        return 2 ** 20      # one megabit
    elif m == 'MB':
        return 2 ** 20 * 8  # one megabyte
    elif m == 'Gb':
        return 2 ** 30      # one gigabit
    elif m == 'GB':
        return 2 ** 30 * 8  # one gigabyte
    elif m == 'Tb':
        return 2 ** 40      # one terabit
    elif m == 'TB':
        return 2 ** 40 * 8  # one terabyte
    else:
        return 0


def convert_seconds(tsec):
    string = ''
    hour = int(tsec / 3600)
    min = int(tsec / 60) % 60
    sec = tsec % 60
    if hour != 1:
        string += str(hour) + ' hours, '
    else:
        string += str(hour) + ' hour, '
    if min != 1:
        string += str(min) + ' minutes, '
    else:
        string += str(min) + ' minute, '
    if sec != 1:
        string += str(sec) + ' seconds'
    else:
        string += str(sec) + ' second'

    return string


def download_time(tds, tdm, ds, dm):

    dsize = tds * measure(tdm)
    dspeed = ds * measure(dm)
    seconds = dsize * 1.0 / dspeed
    return convert_seconds(seconds)



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')


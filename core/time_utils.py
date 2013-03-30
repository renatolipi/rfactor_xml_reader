#coding:utf-8

from datetime import timedelta


def timelist_from_seconds(given_time):
    tdelta_format = timedelta(seconds=given_time)
    tdelta_string = str(tdelta_format)
    time_list = tdelta_string.split(':')
    time_list[2] = str(float(time_list[2])).replace('.', '"')
    return time_list


def prettify_laptime(seconds):
    time_list = timelist_from_seconds(seconds)
    return "{}'{}".format(time_list[1], time_list[2])


def prettify_racetime(seconds):
    time_list = timelist_from_seconds(seconds)
    if int(time_list[0]) < 1:
        return prettify_laptime(seconds)

    return "{}h{}'{}".format(time_list[0],
                             time_list[1],
                             time_list[2])

if __name__ == '__main__':
    print 'laptime format: ', prettify_laptime(81.678)
    print 'racetime formats:'
    print prettify_racetime(2081.678)
    print prettify_racetime(9081.678)
    print prettify_racetime(86081.678)
    print "WARNING: it won't work above 24h"

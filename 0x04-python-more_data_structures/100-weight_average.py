#!/usr/bin/python3
def weight_average(my_list=[]):
    """ returns a weight average of all integers int tuple (<score>, <weight>)"""
    if not my_list:
        return 0

    score_weight = 0
    sum_weight = 0

    for tup in my_list:
        score_weight += tup[0] * tup[1]
        sum_weight += tup[1]

    return (score_weight / sum_weight)

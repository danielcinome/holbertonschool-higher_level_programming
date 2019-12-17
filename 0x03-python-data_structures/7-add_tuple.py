#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_tma = (0, 0)
    if len(tuple_b) == 0:
        tuple_tmb = (0, 0)
    if len(tuple_a) == 1:
        tuple_tma = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        tuple_tmb = (tuple_b[0], 0)
    if len(tuple_a) >= 2:
        tuple_tma = (tuple_a[0], tuple_a[1])
    if len(tuple_b) >= 2:
        tuple_tmb = (tuple_b[0], tuple_b[1])
    tuple_new = (tuple_tma[0] + tuple_tmb[0], tuple_tma[1] + tuple_tmb[1])
    return tuple_new

#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2017
# Glenn P. Downing
# ---------------------------


# ------
# caches
# ------
cycle_length_cache = {}

meta_cache = {
    1:1,
    2:2,
    3:3,
    6:6,
    7:7,
    9:9,
    18:18,
    19:19,
    25:25,
    27:27,
    54:54,
    55:55,
    73:73,
    97:97,
    129:129,
    171:171,
    231:231,
    235:235,
    313:313,
    327:327,
    649:649,
    654:654,
    655:655,
    667:667,
    703:703,
    871:871,
    1161:1161,
    2223:2223,
    2322:2322,
    2323:2323,
    2463:2463,
    2919:2919,
    3711:3711,
    6171:6171,
    10971:10971,
    13255:13255,
    17647:17647,
    17673:17673,
    23529:23529,
    26623:26623,
    34239:34239,
    35497:35497,
    35655:35655,
    52527:52527,
    77031:77031,
    106239:106239,
    142587:142587,
    156159:156159,
    216367:216367,
    230631:230631,
    410011:410011,
    511935:511935,
    626331:626331,
    837799:837799,
    1117065:1117065,
    1126015:1126015,
    1501353:1501353,
    1564063:1564063,
    1723519:1723519,
    2298025:2298025,
    3064033:3064033,
    3542887:3542887,
    3732423:3732423,
    5000000:3732423
}

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read an int from r
    r a reader
    return the int
    """
    n = int(r.readline())
    assert n > 0
    return n

# ------------
# collatz_eval
# ------------

def collatz_eval (n) :
    """
    n the end of the range [1, n], inclusive
    return the value that produces the max cycle length of the range [1, n]
    """
    assert n > 0
    
    #Uses the hard-coded meta cache
    for key in sorted(meta_cache, reverse = True):
        if n >= key and n <= 5000000: #meta cache only relevant if n > 5000000
            return meta_cache.get(key)
        else:
            m = int((n/2) + 1)

    assert m > 0
    global cycle_length_cache
    curr_max_cyc_len = 0
    curr_best = 1

    for i in range(m, n+1):
        if i in cycle_length_cache:
            x = cycle_length_cache.get(i)
        else:
            x = cycle_length(i)
            cycle_length_cache[i] = x
        if x >= curr_max_cyc_len:
            curr_max_cyc_len = x
            curr_best = i
    assert curr_best > 0
    return curr_best
# -------------
# collatz_print
# -------------

def collatz_print (w, m) :
    """
    print an int to w
    w a writer
    m the max cycle length
    """
    assert m > 0
    w.write(str(m) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    t = int(r.readline())
    for _ in range(t) :
        n = collatz_read(r)
        m = collatz_eval(n)
        collatz_print(w, m)

# ------------------------
# cycle_length, from class
# ------------------------

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

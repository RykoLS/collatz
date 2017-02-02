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
    16:9,
    32:27,
    64:55,
    128:97,
    256:235,
    512:327,
    1024:871,
    2048:1161,
    4096:3711,
    8192:6171,
    16384:13255,
    32768:26623,
    65536:52527,
    131072:106239,
    262144:230631,
    524288:511935,
    1048576:837799,
    2097152:1723519,
    4194304:3732423,
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
    
    global cycle_length_cache
    curr_max_cyc_len = 0
    curr_best = 1

    for key in sorted(meta_cache, reverse = True):
        if n == key:
            return meta_cache.get(n)
        elif n > key:
            m = meta_cache.get(key)
            break
        else:
            m = int((n/2) + 1)
    assert m > 0
    for i in range(m, n+1):
        if i in cycle_length_cache:
            x = cycle_length_cache.get(i)
        else:
            x = cycle_length(i)
            cycle_length_cache[i] = x
        #print(i)
        #print(cycle_length_cache[i])
        if x >= curr_max_cyc_len:
            curr_max_cyc_len = x
            curr_best = i
    assert curr_best > 0
    #print(cycle_length_cache)
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

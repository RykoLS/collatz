#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2017
# Glenn P. Downing
# ---------------------------
lazy_cache = {}
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
    # <your code>
    assert n > 0
    if n in lazy_cache:
        print(lazy_cache)
        return lazy_cache.get(n)
    curr_max_cyc_len = 0
    curr_best = 1
    for i in range(1, n+1):
        x = cycle_length(i)
        if x >= curr_max_cyc_len:
            curr_max_cyc_len = x
            curr_best = i

    #<your code>
    """
    assert n > 0
    m = n
    assert m > 0
    return m
    """
    assert curr_best > 0
    lazy_cache[n] = curr_best
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

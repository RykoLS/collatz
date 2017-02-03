#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2017
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        r = StringIO("10\n")
        n = collatz_read(r)
        self.assertEqual(n, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        m = collatz_eval(10)
        self.assertEqual(m, 9)  # Check later

    def test_eval_2(self):
        m = collatz_eval(15)
        self.assertEqual(m, 9)  # Check later

    def test_eval_3(self):
        m = collatz_eval(20)
        self.assertEqual(m, 19)  # Check later

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 10)
        self.assertEqual(w.getvalue(), "10\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("101\n4637992\n2643843\n5000000\n3707088\n607131\n1390690\n3197802\n305584\n2462386\n1165154\n791667\n4102166\n813671\n1453903\n2354851\n1662166\n3055901\n3647063\n3026431\n3184051\n362009\n3197455\n844662\n2681371\n3540092\n4045224\n4040242\n4834752\n1336086\n2175741\n113590\n3341795\n3217906\n997932\n4749613\n4207575\n4854217\n385763\n1141542\n2294157\n4967449\n2301470\n2709927\n1165482\n3037117\n2857493\n772327\n3206084\n1435364\n296689\n1271081\n1309053\n987098\n1396311\n4888922\n358265\n341148\n2701283\n450521\n2659341\n3076451\n4931968\n1874633\n1422279\n3175064\n4150650\n2629766\n1295383\n1341901\n3699781\n4756041\n3536758\n2219368\n3962950\n4924416\n4372754\n711033\n1504143\n3529497\n1055462\n327034\n2232116\n989748\n4380995\n3007404\n1353258\n814324\n491242\n3281077\n4126405\n4598842\n1572619\n4495097\n1672891\n1532593\n3878981\n3899797\n3348878\n606968\n2958697\n911594\n")
        w = StringIO()
        collatz_solve(r, w)
        print(w.getvalue())
        #self.assertEqual(w.getvalue(), "9\n9\n19\n")
# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    main()

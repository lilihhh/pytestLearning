# -*- coding:utf-8 -*-
# @FileName  :test_min_max.py
# @Time      :2022/5/14 17:22
# @Author    :xiaoli.zhou
from utils import algo


def test_min():
    values = (2, 3, 1, 4, 6)

    val = algo.min(values)
    assert val == 1


def test_max():
    values = (2, 3, 1, 4, 6)

    val = algo.max(values)
    assert val == 6

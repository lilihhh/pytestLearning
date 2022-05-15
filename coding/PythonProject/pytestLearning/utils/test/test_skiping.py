# -*- coding:utf-8 -*-
# @FileName  :test_skiping.py
# @Time      :2022/5/14 17:23
# @Author    :xiaoli.zhou
from utils import algo
import pytest


@pytest.mark.skip
def test_min():
    values = (2, 3, 1, 4, 6)

    val = algo.min(values)
    assert val == 1


def test_max():
    values = (2, 3, 1, 4, 6)

    val = algo.max(values)
    assert val == 6

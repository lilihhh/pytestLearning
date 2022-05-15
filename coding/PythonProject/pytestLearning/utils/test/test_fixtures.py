# -*- coding:utf-8 -*-
# @FileName  :test_fixtures.py
# @Time      :2022/5/14 21:57
# @Author    :xiaoli.zhou
from utils import algo
import pytest


# @property属性化标签
# class Testcase:
#     @property
#     def data(self,):
#
#         return [3, 2, 1, 5, -3, 2, 0, -2, 11, 9]
#
#
# def test_sel_sort():
#     d = Testcase()
#     data = d.data
#
#     sorted_vals = algo.sel_sort(data)
#     assert sorted_vals == sorted(data)


# 以下pytest 夹具用法
@pytest.fixture
def data():
    return [3, 2, 1, 5, -3, 2, 0, -2, 11, 9]


def test_sel_sort(data):
    sorted_vals = algo.sel_sort(data)
    assert sorted_vals == sorted(data)

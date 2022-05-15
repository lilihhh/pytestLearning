# -*- coding:utf-8 -*-
# @FileName  :test_allure.py
# @Time      :2022/5/14 23:01
# @Author    :xiaoli.zhou
import pytest


def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')

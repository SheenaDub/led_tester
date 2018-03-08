#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""

import sys
sys.path.append('.')

import pytest
from click.testing import CliRunner
from led_tester import led_tester
from led_tester import cli
from led_tester import utils


def test_command_line_interface():
    """Test the CLI."""
    ifile = "./data/input_assign3.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None


def test_read_file():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'turn on 2,2 through 7,7\n']
    
    
    
# def test_parsing():
#     ledTesterTest=led_tester(10)
#     ledTesterTest.apply('turn on 0,0 through 9,9')
#     assert ledTesterTest.count==100
#     # if command is 'turn on 0,0 through 9,9
#     assert cmd == "turn on"
#     assert x1, x2, y1, y2 == 0,0,9,9
    
    
    
    
    
    
    
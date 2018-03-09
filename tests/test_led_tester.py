#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""

import sys
sys.path.append('.')

import pytest
from click.testing import CliRunner

from led_tester.utils import *


def test_command_line_interface():
    """Test the CLI."""
    ifile = "./data/input_assign3.txt"
    N, instructions = myparser(ifile)
    assert N is not None
 
 
def test_read_file():
    ifile = "./data/test_data.txt"
    info= myparser(ifile)
    N=info[0]
    instructions=info[1]
    assert N == 10
    assert instructions[0] == ['turn on', '0', '0', '9','9']
    assert instructions[1] == ['turn off', '0', '0', '9','9']
    assert instructions[4] == ['turn on', '2', '2', '7','7']
     
     
def test_instructions_details():
    ifile = "./data/test_data.txt"
    info= myparser(ifile)
    N=info[0]
    instructions=info[1]
    # check cmd and num1 from first line of instructions has been read right
    cmd=instructions[0][0]
    num1=instructions[0][1]
    assert cmd=='turn on'
    assert num1=='0'
  
     
def test_instantiation():
    # this tests object has been created and 
    #prints it out to see if correct no of rows/columns are there
    lighttest=LightTester(3)
    lighttest.printlights()
    assert lighttest!=None
     
def test_typos_converted_to_empty_strings():
    ifile = "./data/typos_galore.txt"
    info= myparser(ifile)
    N=info[0]
    instructions=info[1]
    print(info)
    assert N==5
    assert instructions[0][0]==''
    assert instructions[2][0]==''
     
     
def test_apply_and_count_work():
    ifile = "./data/smalltest.txt"
    info= myparser(ifile)
    N=info[0]
    instructions=info[1]
    test=LightTester(N)
    test.apply(instructions)
    assert test.count()==24
     
     
def test_apply_works_with_typos():
    ifile = "./data/typos_galore.txt"
    info= myparser(ifile)
    N=info[0]
    instructions=info[1]
    test2=LightTester(N)
    test2.apply(instructions)
    assert test2.count()==1
    
    
def test_works_with_bigger_file():
    ifile = "./data/input_assign3.txt"
    info= myparser(ifile)
    N=info[0]
    instructions=info[1]
    test3=LightTester(N)
    test3.apply(instructions)
    assert test3.count()==400410
    
    
    
def test_works_with_out_of_range_numbers():
    pass
    
    
    
    
    
    
#! /usr/bin/python3.5
import pip
try:
    from brainfuck import NiceInterpreter
except ImportError:
    pip.main("install", "brainfuck")
import sys
x = NiceInterpreter()
x.setChars()
x.execute(sys.argv[1])

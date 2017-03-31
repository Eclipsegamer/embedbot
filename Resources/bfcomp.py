#! /usr/bin/python3.5
try:
    from brainfuck import NiceInterpreter
except ImportError:
    import pip
    pip.main(["install", "brainfuck"])
    del pip
import sys
x = NiceInterpreter()
x.setChars()
x.execute(sys.argv[1])

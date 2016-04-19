import logging
logging.log(logging.WARNING, "This is a warning log.")

## First profiler written in pure Python. Slowest
import profile
profile.Stats()

## Second profiler written in C
import hotshot

## Latest profiler written in C
import cProfile
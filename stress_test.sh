#!/bin/bash

python -m cProfile -s cumtime tests/stress_tests/stress_test.py

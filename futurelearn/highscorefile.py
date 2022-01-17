#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 07:09:39 2021

@author: richardhardy
"""

import matplotlib.pyplot as plot

print("Loading high scores")
scores = []
names = []

try:
    with open("highscores.txt", "r") as f:
        for line in f:
            line = line.strip("\n")
            line = line.split(" ")
            names.append(line[0])
            scores.append(int(line[1]))
except FileNotFoundError:
    print("No high scores file found")

plot.bar(names, scores)
plot.show()

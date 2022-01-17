#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:44:41 2021

@author: richardhardy
"""

import csv
with open('ages.csv', newline= '') as csvfile:
    favourites = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in favourites:
        print(row)
        print(type(row[0]), type(row[1]))

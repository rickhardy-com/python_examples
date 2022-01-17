#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:35:33 2021

@author: richardhardy
"""

import csv
with open('foods.csv') as csvfile:
    favourites = csv.reader(csvfile, delimiter=',')
    for row in favourites:
        print(row)

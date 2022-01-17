#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:42:59 2021

@author: richardhardy
"""

import csv
name = "Portia"
food = "Steak"
with open('foods.csv', mode="a") as csvfile:
    favourites = csv.writer(csvfile, delimiter=',')
    favourites.writerow([name,food])

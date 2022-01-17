#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 22:15:37 2021

@author: richardhardy
"""

import json

with open("neil.json", "r") as f:
    data2 = json.load(f)

print(data2)
age = data2 ["Age"]
print (data2 ["Hobbies"])
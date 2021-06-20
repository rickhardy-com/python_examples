#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 16:43:32 2021

@author: richardhardy
"""

error_val = True
while error_val == True:
    salary_value = input ('Enter Salary ')
    print (salary_value)
    try: 
        salary_float = float (salary_value)
        error_val = False
    except: 
        print ('salary is not numeric, try again')
        error_val = True

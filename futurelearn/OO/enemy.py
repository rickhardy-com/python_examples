#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:02:30 2022

@author: richardhardy
"""

from Character_fl import Character


class Enemy(Character):
        def __init__(self, char_name, char_description):
            super().__init__(char_name, char_description)
            self.weakness = None
        # weakness is set by the sub class
        def set_weakness (self, weakness_in):
            print (1)
            self.weakness = weakness_in
            print ('1', self, 'inweak',weakness_in)
            
        def get_weakness (self):
            print (self.weakness)
        
        def fight(self, combat_item):
            if combat_item == self.weakness:
                print("You fend " + self.name + " off with the " + combat_item )
                return True
            else:
                print(self.name + " crushes you, puny adventurer")
                return False
            
            
            
            

'''
dave = Enemy("Dave", "A smelly zombie")
print (dave)

#set in the superclass
dave.set_description("Enemy Dave big bulging eyes")

dave.set_weakness ('elephant')
dave.set_conversation('Hello, nice Weather ... Aargh')
dave.describe()

print (dave.get_description())
print (dave.get_weakness())

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)
'''


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 12:12:02 2022

@author: richardhardy
"""

class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.food = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
    # sets the description in the superclass!
    def set_description(self, char_description):
        self.description = char_description 
        
    def get_description(self):
         print (self.description)
        
    def set_food(self, food):
        self.food = food
        
    def get_food(self):
         print (self.food)


    # sets the description in the superclass!
    def set_name (self, name):
        self.name = name 
        
    def get_name(self):
         print (self.name)
        


            



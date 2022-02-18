#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 04:31:12 2022

@author: richardhardy
"""



class Room(object):
    location = None
    number_of_rooms = 0
    def __init__(self,name, roomtype,description,location):
        location = None
        Room.number_of_rooms += 1
        self.name = name
        self.roomtype = roomtype
        self.description = description
        self.location = location
        self.linked_rooms = {}
        self.character = None
    def set_description(self, room_description):
        self.description = room_description
    def get_description(self):
        return self.description
    def set_character(self, character):
        self.character = character
    def get_character(self):
        return self.character
    def describe(self):
        print(self.name,  self.description )
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def print_name(self):
        print( self.name )
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked rooms :" + repr(self.linked_rooms) )
        
    def link_room2(self, room_to_link, direction):
        direction_pairs= {'East':'West',
                          'West':'East',
                          'North':'South',
                          'South':'North',
                          'Up':'Down',
                          'Down':'Up',
                          }
        self.linked_rooms[direction] = room_to_link
        room_to_link.linked_rooms[direction_pairs[direction]] = self
        
        #print( self.name + " linked rooms :" + repr(self.linked_rooms) )
        
    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)
    def get_room_details (self):
        print('----------------------------')
        print (self.get_name())
        print (self.get_description())
        self.get_details()

    def get_room_info(self):
        print('\n~~~~~~~~~~~~~~~~~~~~~~ ')
        print (self.get_name())
        for key, val in self.linked_rooms.items():
            print('The {} is {}'.format(val.get_name(), key))
        print('~~~~~~~~~~~~~~~~~~~~~~ \n')
        
    def get_room_info2(self):
        print('\n----------------------------')
        print (self.get_name())
        
        print (self.linked_rooms.items()) #print the dictionary
        
        print (self.linked_rooms) # print the dictionary as a list 
        
        #iterate through the list and print each of the pairs        
        for key in self.linked_rooms:
            print(key, '->', self.linked_rooms[key].name)
                    
        print('---------------------------- \n')
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

        
    

class Kitchen(Room):
    def __init__(self, name, location, description, cooking_type):
            self.cooking_type = cooking_type
            super().__init__(name, 'kitchen', description, location)
        
class FunctionRoom(Room):
    def __init__(self, name, location, description, main_function):
            self.main_function = main_function
            super().__init__( name, 'functionRoom', description, location, )
        
class House():
    def __init__(self,location):
        self.address = location
        
'''

directions = ['North','South','East','West','Up','Down'  ] 

dining_room = FunctionRoom ("diningroom",'5 Elm Terrace','large room with big table','catering')

ballroom = FunctionRoom("ballroom",'5 Elm Terrace','large room with grand piano','dancing')
      
main_kitchen = Kitchen ('main_kitchen', '5 Elm Terrace', 'modern kitchen', 'gas')




dave = Enemy("Dave", "A smelly zombie")
dave.set_weakness ('elephant')
dave.set_conversation('Hello, nice Weather ... Aargh')
dining_room.set_character (dave)
print ('dave type', type(dave))
print (dining_room.get_character().name)

#ballroom = Room("ballroom",'5 Elm Terrace')


print (main_kitchen.cooking_type)
print (main_kitchen.location)

print (type(main_kitchen))
main_kitchen.set_description("A dank and dirty room buzzing with flies")

print (main_kitchen.get_description())
main_kitchen.describe()

main_kitchen.link_room2(dining_room, 'South', )
#dining_room.link_room(main_kitchen, 'North', )

dining_room.link_room(ballroom, 'East', )
ballroom.link_room(dining_room, 'West', )

ballroom.get_room_details()

dining_room.get_room_info2()

ballroom.get_room_info()

current_room = main_kitchen          


while True:		
    print("\n")  
       
    current_room.get_details()   
    inhabitant = current_room.get_character ()
    #print ('habitant', inhabitant)
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")   
    if command in directions: 
        current_room = current_room.move(command) 
    elif command == 'Talk':
        print ('Who To? ')
    elif command == 'Fight':
        print('ok lets go')    '''
    





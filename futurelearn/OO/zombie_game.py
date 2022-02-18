
from room import FunctionRoom, Kitchen, Room
from enemy import Enemy

#room creation

dining_room = FunctionRoom ("diningroom",'5 Elm Terrace','large room with big table','catering')

ballroom = FunctionRoom("ballroom",'5 Elm Terrace','large room with grand piano','dancing')
      
main_kitchen = Kitchen ('main_kitchen', '5 Elm Terrace', 'modern kitchen', 'gas')

print("There are " + str(Room.number_of_rooms) + " rooms to explore.")

#room linking

main_kitchen.link_room2(dining_room, 'South', )

dining_room.link_room2(ballroom, 'East', )


# create characters
dave = Enemy("Dave", "A smelly zombie")

moomin_troll = Enemy ("Moomy", "Looks a bit like a cartoon Hippo")


# set up characters

moomin_troll.set_food('babies')

dave.set_weakness ('elephant')
moomin_troll.set_weakness ('olives')

dave.set_conversation('Hello, nice Weather ... Aargh')
moomin_troll.set_conversation('Boo!')

# locate characters

dining_room.set_character (dave)

dining_room.set_character (moomin_troll)

# set possible directions

directions = ['North','South','East','West','Up','Down'  ]  

current_room = main_kitchen          

while True:		
    print("\n")  
       
    current_room.get_details()   
    current_room.describe()
    #inhabitant = current_room.get_character ()
    #print ('habitant', inhabitant)
    if current_room.get_character () is not None:
        current_room.get_character ().describe()
    command = input("> ")  
    print (command)
    if command in directions: 
        current_room = current_room.move(command) 
    elif command == 'Talk':
        question = input ('What do you want to say?  ')
        reply = current_room.get_character().talk ()
           
    elif command == 'Fight':
        weapon = input('fight with what? > ')
        print('ok lets go')  
        result = current_room.get_character().fight (weapon)
        if result :
            current_room.set_character(None)
        else:
            print ("Bye!")
            break
        
    elif command == 'exit':
        print ("leave game")
        break
    
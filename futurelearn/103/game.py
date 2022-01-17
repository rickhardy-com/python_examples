#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 08:34:17 2021

@author: richardhardy
"""

import sqlite3
from random import randint
from time import time


def create(name, cores, cpu_speed, ram, cost):
    insert_sql = "INSERT INTO computer(name, cores, cpu_speed, ram, cost) VALUES ('{}', {},{},{},{} )".format(name, cores, cpu_speed, ram, cost)

    conn.execute(insert_sql)

    conn.commit()

def read(name):
    select_sql = "SELECT * FROM computer WHERE name = '{}'".format(name)

    result = conn.execute(select_sql)

    return result.fetchone()

def update(name, cores, cpu_speed, ram, cost):
    
    
    
    
    update_sql = "UPDATE computer SET cores = {}, cpu_speed = {}, ram = {}, cost = {} WHERE name = '{}'".format(cores, cpu_speed, ram, cost, name)

    conn.execute(update_sql)
    conn.commit()
    
    
    
def delete(name):    
    delete_sql = "DELETE FROM computer WHERE name = '{}'".format(name)
    conn.execute(delete_sql)
    conn.commit()
    
def delete_none():    
    delete_sql = "DELETE FROM result"#" WHERE winner = 'None'"
    print (delete_sql)
    conn.execute(delete_sql)
    conn.commit()

def read_all_cards():
    result = conn.execute("SELECT * FROM computer")
    return result.fetchall()

def insert_picked(name):
    insert_sql = "INSERT INTO picked(name, time) VALUES ('{}', {})".format(name, time())
    conn.execute(insert_sql)
    conn.commit()
 
     
def insert_result (card, winner):    
    #checks for an incomplete result and returns the first card from that line
    check_for_incomplete_result = "SELECT max(card1), count (*) FROM result WHERE card2 = 'None'"
    first_card = conn.execute(check_for_incomplete_result)
    count_incomplete = first_card.fetchone() 
    # in the case where there is no incomplete result then insert a new line with only card 1 filled, INSERT
    if count_incomplete == 0: 
        insert_sql =  "INSERT INTO result(card1, card2, winner) VALUES ('{}', '{}', '{}')".format(card, None, None)  
        conn.execute(insert_sql)
        conn.commit
    # in the case where there is an incomplete result fill in the rest of this line, UPDATE
    else: 
        winning_card = card if winner == 'y' else count_incomplete[0]    
        update_sql = "UPDATE result SET card2 = '{}', winner = '{}' where card2 = 'None' ".format(card, winning_card)
        conn.execute(update_sql)
        conn.commit()
    
def pick_card():
    cards = read_all_cards()

    last_picked_card = read_last_picked()

    random_card = cards[randint(0, len(cards) - 1)]

    while random_card[0] == last_picked_card[0]:
        random_card = cards[randint(0, len(cards) - 1)]

    insert_picked(random_card[0])
    return random_card


def read_last_picked():
    result = conn.execute("SELECT * FROM picked ORDER BY time DESC")
    return result.fetchone()


conn = sqlite3.connect("computer_cards.db")
result = conn.execute("SELECT * FROM computer")
computers = result.fetchall()
delete_none()



player = input("Are you player (1) or (2) >")

choosing_player = "1"

for round in range(4):

    input("Press enter to pick a card when both players are ready >")
    card = pick_card()
    card_text = "{}, cores={}, speed={}GHz, RAM={}MB, cost={}$".format(card[0], card[1], card[2], card[3], card[4])
    card_name = "{}".format(card[0])
    print(card_text)
    print (card_name)
    

    print("Player " + choosing_player + " picks.")

    winner = input("Did you win? (Y)es, (N)o, (D)raw >").lower()
    if winner == "y":
        choosing_player = player
    elif winner == "n":
        choosing_player = "2" if player == "1" else "1"
    insert_result (card_name, winner)
    
    

delete ('My computer')



card = pick_card()
print(card)

    
    

import random

import pymongo

from pymongo import MongoClient

cin = MongoClient()

db = cin.my_game_database

users = db.users

player_hp = 500

enemy_hp = 1000

time = 0

coins = 100

process = True

Spells = ('1.Curer', '2.Small Shield', '3.Big Shield', '4.Grenade', '5.C4', '6.Bomb')

while process == True:

    option = input("What do you want to do?\n1.Attack\n2.Spell\n")

    if option == str(1):
        time = time + 1

        enemy_hp = enemy_hp + random.randint(1, 30)

        player_attack = random.randint(100, 200)

        enemy_attack = random.randint(50, 100)

        attack = player_hp - enemy_attack

        if attack < 0:
            attack = 0

            print("Enemy attacked for " + str(enemy_attack))

            print("Player HP now equals to " + str(attack))

            print("The enemy has defeated you!")

            exit()

        print("Enemy attacked for " + str(enemy_attack))

        print("Player HP now equals to " + str(attack))

        player_hp = attack

        attacks = enemy_hp - player_attack

        if attacks < 0:
            attacks = 0

            print("Player attacked for " + str(player_attack))

            print("Enemy HP now equals to " + str(attacks))

            print("Well Done!! You defeated the enemy. In " + str(time) + " goes")

            user1 = ({"Turns": time})

            user_id = users.insert(user1).inserted_id

            exit()

        print("Player attacked for " + str(player_attack))

        print("Enemy HP now equals to " + str(attacks))

        enemy_hp = attacks

    if option == str(2):
        time = time + 1

        choice = input("What spell do you want to use?\n1.Curer COST: 15\n2.Small Shield COST: 10\n3.Big "

                       "Shield COST: 25\n4.Grenade COST: 15\n5.C4 COST: 30\n6.Bomb COST: 10\n")

        if choice == str(1):

            player_hp = player_hp + 100

            if player_hp < 0:
                player_hp = 0

                print("The enemy defeated you!!")

                exit()

            print("Players HP now is " + str(player_hp))

            coins = coins - 15

            print("You have " + str(coins) + " coins left")

        if choice == str(2):

            player_hp = player_hp + 50

            if player_hp < 0:
                player_hp = 0

                print("The enemy defeated you!!")

                exit()

            print("Players HP now is " + str(player_hp))

            coins = coins - 10

            print("You have " + str(coins) + " coins left")

        if choice == str(3):

            player_hp = player_hp + 200

            if player_hp < 0:
                player_hp = 0

                print("The enemy defeated you!!")

                exit()

            print("Players HP now is " + str(player_hp))

            coins = coins - 25

            print("You have " + str(coins) + " coins left")

        if choice == str(4):

            enemy_hp = enemy_hp - 100

            if enemy_hp < 0:
                enemy_hp = 0

                print("The enemy defeated you!!")

                exit()

            print("Enemies HP now is " + str(enemy_hp))

            coins = coins - 15

            print("You have " + str(coins) + " coins left")

        if choice == str(5):

            enemy_hp = enemy_hp - 200

            if enemy_hp < 0:
                enemy_hp = 0

                print("Well Done!! You've defeated your enemy")

                exit()

            print("Enemies HP now is " + str(enemy_hp))

            coins = coins - 30

            print("You have " + str(coins) + " coins left")

        if choice == str(6):

            enemy_hp = enemy_hp - 25

            if enemy_hp < 0:
                enemy_hp = 0

                print("Well Done!! You've defeated your enemy")

                exit()

            print("Enemies HP now is " + str(enemy_hp))

            coins = coins - 10

            print("You have " + str(coins) + " coins left")

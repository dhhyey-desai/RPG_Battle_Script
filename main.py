import random


class colour:

    PINK = '\033[95m'

    BLUE = '\033[94m'

    GREEN = '\033[92m'

    YELLOW = '\033[93m'

    FAIL = '\033[91m'

    END = '\033[0m'

    BOLD = '\033[1m'

    UNDERLINE = '\033[4m'


player_hp = 500

bar_hp = 25

enemy_hp = 1000

bar1_hp = 50

time = 0

coins = 100

process = True

bar = (colour.GREEN + colour.BOLD + "█" * bar_hp + colour.END + colour.BOLD + " Player HP" + colour.END)

print(bar)

bar1 = (colour.FAIL + colour.BOLD + "█" * bar1_hp + colour.END + colour.BOLD + " Enemy HP" + colour.END)

print(bar1)

while process == True:

    enemy_spell = random.randint(1, 9)

    if enemy_spell == 1:

        enemy_hp = enemy_hp + 200

        print(colour.FAIL + "The enemy just healed for 200 HP.\nEnemy HP now equals to " + str(enemy_hp) + colour.END)

        bar1_hp_now = enemy_hp / 20

        bars = round(bar1_hp_now)

        bar1 = (colour.FAIL + colour.BOLD + "█" * bars + " Enemy HP" + colour.END)

        print(bar1)

    if enemy_spell == 2:
        enemy_hp = enemy_hp + 400

        print(colour.FAIL + "The enemy just healed for 400 HP.\nEnemy HP now equals to " + str(enemy_hp) + colour.END)

        bar1_hp_now = enemy_hp / 20

        bars = round(bar1_hp_now)

        bar1 = (colour.FAIL + colour.BOLD + "█" * bars + " Enemy HP" + colour.END)

        print(bar1)

    if enemy_spell == 3:

        enemy_hp = enemy_hp + 50

        print(colour.FAIL + "The enemy just healed for 50 HP.\nEnemy HP now equals to " + str(enemy_hp) + colour.END)

        bar1_hp_now = enemy_hp / 20

        bars = round(bar1_hp_now)

        bar1 = (colour.FAIL + colour.BOLD + "█" * bars + " Enemy HP" + colour.END)

        print(bar1)

    if enemy_hp < 0:

        enemy_hp = 0

        print("Well Done!! You defeated the enemy. In " + str(time) + " attacks.")

        exit()

    option = input(colour.BOLD + "What do you want to do?\n" + colour.BLUE + "1.Attack\n2.Spell\n" + colour.END)

    if option == str(1):

        if enemy_hp < 0:

            enemy_hp = 0

            print("Well Done!! You defeated the enemy. In " + str(time) + " attacks.")

            exit()

        time = time + 1

        enemy_hp = enemy_hp + random.randint(1, 30)

        player_attack = random.randint(100, 200)

        enemy_attack = random.randint(50, 100)

        attack = player_hp - enemy_attack

        if attack < 0:

            attack = 0

            print(colour.FAIL + colour.BOLD + "Enemy attacked for " + str(enemy_attack) + colour.END)

            print(colour.GREEN + colour.BOLD + "Player HP now equals to " + str(attack) + colour.END)

            print(colour.FAIL + colour.BOLD + "The enemy has defeated you!" + colour.END)

            exit()

        print(colour.FAIL + colour.BOLD + "Enemy attacked for " + str(enemy_attack) + colour.END)

        print(colour.GREEN + colour.BOLD + "Player HP now equals to " + str(attack) + colour.END)

        player_hp = attack

        attacks = enemy_hp - player_attack

        if attacks < 0:

            attacks = 0

            print(colour.GREEN + colour.BOLD + "Player attacked for " + str(player_attack) + colour.END)

            print(colour.FAIL + colour.BOLD + "Enemy HP now equals to " + str(attacks) + colour.END + colour.END)

            print(colour.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colour.END)

            exit()

        print(colour.GREEN + colour.BOLD + "Player attacked for " + str(player_attack) + colour.END)

        print(colour.FAIL + colour.BOLD + "Enemy HP now equals to " + str(attacks) + colour.END + colour.END)

        enemy_hp = attacks

        bar_hp_now = attack/20

        bars = round(bar_hp_now)

        bar1_hp_now = attacks/20

        bars1 = round(bar1_hp_now)

        bar = (colour.GREEN + colour.BOLD + "█" * bars + " Player HP" + colour.END)

        print(bar)

        bar1 = (colour.FAIL + colour.BOLD + "█" * bars1 + "Enemy HP" + colour.END)

        print(bar1)

    if option == str(2):

        if coins < 0:

            print(colour.FAIL + "Not ENOUGH Coins" + colour.END)

            continue

        enemy_hp = enemy_hp + random.randint(1, 30)

        if enemy_hp < 0:

            enemy_hp = 0

            print(colour.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colour.END)

            exit()

        time = time + 1

        choice = input(colour.BOLD + "What spell do you want to use?" + colour.END + colour.BLUE + colour.BOLD + "\n"

                                                   "1.Curer COST: 15\n2.Small Shield CO"

                                                   "ST: 10\n3.Big " +

                       "Shield COST: 25\n4.Grenade COST: 15\n5.C4 COST: 30\n6.Bomb COST: 10\n" + colour.END)

        if choice == str(1):

            if coins < 15:

                print(colour.FAIL + "Not ENOUGH Coins" + colour.END)

                continue

            player_hp = player_hp + 100


            print(colour.GREEN + "Player HP now equals to " + str(player_hp) + colour.END)


            coins = coins - 15

            print("You have " + colour.GREEN + str(coins) + colour.END + " coins left")

            bar_hp_now = player_hp / 20

            bars = round(bar_hp_now)

            bar = (colour.GREEN + colour.BOLD + "█" * bars + " Player HP" + colour.END)

            print(bar)

        if choice == str(2):

            if coins < 10:

                print(colour.FAIL + "Not ENOUGH Coins" + colour.END)

                continue

            player_hp = player_hp + 50

            print(colour.GREEN + "Player HP now equals to " + str(player_hp) + colour.END)

            coins = coins - 10

            print("You have " + colour.GREEN + str(coins) + colour.END + " coins left")

            bar_hp_now = player_hp / 20

            bars = round(bar_hp_now)

            bar = (colour.GREEN + colour.BOLD + "█" * bars + " Player HP" + colour.END)

            print(bar)

        if choice == str(3):

            if coins < 25:

                print(colour.FAIL + "Not ENOUGH Coins" + colour.END)

                continue

            player_hp = player_hp + 200

            print(colour.GREEN + "Player HP now equals to " + str(player_hp) + colour.END)

            coins = coins - 25

            print("You have " + colour.GREEN + str(coins) + colour.END + " coins left")

            bar_hp_now = player_hp / 20

            bars = round(bar_hp_now)

            bar = (colour.GREEN + colour.BOLD + "█" * bars + " Player HP" + colour.END)

            print(bar)

        if choice == str(4):

            if coins < 15:

                print("You have " + colour.GREEN + str(coins) + colour.END + " coins left")

                continue

            enemy_hp = enemy_hp - 100

            if enemy_hp < 0:

                enemy_hp = 0

                print(colour.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colour.END)

                exit()

            print(colour.FAIL + "Enemy HP now equals to " + str(enemy_hp) + colour.END)

            coins = coins - 15

            print("You have " + colour.GREEN + str(coins) + colour.END + " coins left")

            bar1_hp_now = enemy_hp / 20

            bars = round(bar1_hp_now)

            bar1 = (colour.FAIL + colour.BOLD + "█" * bars + " Enemy HP" + colour.END)

            print(bar1)

        if choice == str(5):

            if coins < 30:

                print(colour.FAIL + "Not ENOUGH Coins" + colour.END)

                continue

            enemy_hp = enemy_hp - 200

            if enemy_hp < 0:

                enemy_hp = 0

                print(colour.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colour.END)

                exit()

            print(colour.FAIL + "Enemy HP now equals to " + str(enemy_hp) + colour.END)

            coins = coins - 30

            print("You have " + colour.GREEN + str(coins) + colour.END + " coins left")

            bar1_hp_now = enemy_hp / 20

            bars = round(bar1_hp_now)

            bar1 = (colour.FAIL + colour.BOLD + "█" * bars + " Enemy HP" + colour.END)

            print(bar1)

        if choice == str(6):

            if coins < 10:

                print(colour.FAIL + "Not ENOUGH Coins" + colour.END)

                continue

            enemy_hp = enemy_hp - 25

            if enemy_hp < 0:

                enemy_hp = 0

                print(colour.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colour.END)

                exit()

            print(colour.FAIL + "Enemy HP now equals to " + str(enemy_hp) + colour.END)

            coins = coins - 10

            print("You have " + colour.GREEN + str(coins) + colour.END + " coins left")

            bar1_hp_now = enemy_hp / 20

            bars = round(bar1_hp_now)

            bar1 = (colour.FAIL + colour.BOLD + "█" * bars + " Enemy HP" + colour.END)

            print(bar1)
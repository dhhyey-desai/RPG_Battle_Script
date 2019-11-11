import random


class colours:

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

bar = (colours.GREEN + colours.BOLD + "█" * bar_hp + colours.END + colours.BOLD + " Player HP" + colours.END)

print(bar)

bar1 = (colours.FAIL + colours.BOLD + "█" * bar1_hp + colours.END + colours.BOLD + " Enemy HP" + colours.END)

print(bar1)

while process == True:

    enemy_spell = random.randint(1, 9)

    if enemy_spell == 1:

        enemy_hp = enemy_hp + 200

        print(colours.FAIL + "The enemy just healed for 200 HP.\nEnemy HP now equals to " + str(enemy_hp) + colours.END)

        bar1_hp_now = enemy_hp / 20

        bars = round(bar1_hp_now)

        bar1 = (colours.FAIL + colours.BOLD + "█" * bars + " Enemy HP" + colours.END)

        print(bar1)

    if enemy_spell == 2:
        enemy_hp = enemy_hp + 400

        print(colours.FAIL + "The enemy just healed for 400 HP.\nEnemy HP now equals to " + str(enemy_hp) + colours.END)

        bar1_hp_now = enemy_hp / 20

        bars = round(bar1_hp_now)

        bar1 = (colours.FAIL + colours.BOLD + "█" * bars + " Enemy HP" + colours.END)

        print(bar1)

    if enemy_spell == str(6):

        enemy_hp = enemy_hp + 50

        print(colours.FAIL + "The enemy just healed for 50 HP.\nEnemy HP now equals to " + str(enemy_hp) + colours.END)

        bar1_hp_now = enemy_hp / 20

        bars = round(bar1_hp_now)

        bar1 = (colours.FAIL + colours.BOLD + "█" * bars + " Enemy HP" + colours.END)

        print(bar1)

    if enemy_hp < 0:

        enemy_hp = 0

        print("Well Done!! You defeated the enemy. In " + str(time) + " attacks.")

        exit()

    option = input(colours.BOLD + "What do you want to do?\n" + colours.BLUE + "1.Attack\n2.Spell\n" + colours.END)

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

            print(colours.FAIL + colours.BOLD + "Enemy attacked for " + str(enemy_attack) + colours.END)

            print(colours.GREEN + colours.BOLD + "Player HP now equals to " + str(attack) + colours.END)

            print(colours.FAIL + colours.BOLD + "The enemy has defeated you!" + colours.END)

            exit()

        print(colours.FAIL + colours.BOLD + "Enemy attacked for " + str(enemy_attack) + colours.END)

        print(colours.GREEN + colours.BOLD + "Player HP now equals to " + str(attack) + colours.END)

        player_hp = attack

        attacks = enemy_hp - player_attack

        if attacks < 0:

            attacks = 0

            print(colours.GREEN + colours.BOLD + "Player attacked for " + str(player_attack) + colours.END)

            print(colours.FAIL + colours.BOLD + "Enemy HP now equals to " + str(attacks) + colours.END + colours.END)

            print(colours.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colours.END)

            exit()

        print(colours.GREEN + colours.BOLD + "Player attacked for " + str(player_attack) + colours.END)

        print(colours.FAIL + colours.BOLD + "Enemy HP now equals to " + str(attacks) + colours.END + colours.END)

        enemy_hp = attacks

        bar_hp_now = attack/20

        bars = round(bar_hp_now)

        bar1_hp_now = attacks/20

        bars1 = round(bar1_hp_now)

        print(bars)

        bar = (colours.GREEN + colours.BOLD + "█" * bars + " Player HP" + colours.END)

        print(bar)

        bar1 = (colours.FAIL + colours.BOLD + "█" * bars1 + " Enemy HP" + colours.END)

        print(bar1)

    if option == str(2):

        if coins < 0:

            exit(code="Not ENOUGH Coins")

        enemy_hp = enemy_hp + random.randint(1, 30)

        if enemy_hp < 0:

            enemy_hp = 0

            print(colours.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colours.END)

            exit()

        time = time + 1

        choice = input(colours.BOLD + "What spell do you want to use?" + colours.END + colours.BLUE + colours.BOLD + "\n"

                                                   "1.Curer COST: 15\n2.Small Shield CO"

                                                   "ST: 10\n3.Big " +

                       "Shield COST: 25\n4.Grenade COST: 15\n5.C4 COST: 30\n6.Bomb COST: 10\n" + colours.END)

        if choice == str(1):

            if coins < 15:

                exit(code="Not ENOUGH Coins")


            player_hp = player_hp + 100


            print(colours.GREEN + "Player HP now equals to " + str(player_hp) + colours.END)


            coins = coins - 15

            print("You have " + str(coins) + " coins left")

            bar_hp_now = player_hp / 20

            bars = round(bar_hp_now)

            bar = (colours.GREEN + colours.BOLD + "█" * bars + " Player HP" + colours.END)

            print(bar)

        if choice == str(2):

            if coins < 10:

                exit(code="Not ENOUGH Coins")

            player_hp = player_hp + 50

            print(colours.GREEN + "Player HP now equals to " + str(player_hp) + colours.END)

            coins = coins - 10

            print("You have " + str(coins) + " coins left")

            bar_hp_now = player_hp / 20

            bars = round(bar_hp_now)

            bar = (colours.GREEN + colours.BOLD + "█" * bars + " Player HP" + colours.END)

            print(bar)

        if choice == str(3):

            if coins < 25:

                exit(code="Not ENOUGH Coins")

            player_hp = player_hp + 200

            print(colours.GREEN + "Player HP now equals to " + str(player_hp) + colours.END)

            coins = coins - 25

            print("You have " + str(coins) + " coins left")

            bar_hp_now = player_hp / 20

            bars = round(bar_hp_now)

            bar = (colours.GREEN + colours.BOLD + "█" * bars + " Player HP" + colours.END)

            print(bar)

        if choice == str(4):

            if coins < 15:

                exit(code="Not ENOUGH Coins")

            enemy_hp = enemy_hp - 100

            if enemy_hp < 0:

                enemy_hp = 0

                print(colours.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colours.END)

                exit()

            print(colours.FAIL + "Enemy HP now equals to " + str(enemy_hp) + colours.END)

            coins = coins - 15

            print("You have " + str(coins) + " coins left")

            bar1_hp_now = enemy_hp / 20

            bars = round(bar1_hp_now)

            bar1 = (colours.FAIL + colours.BOLD + "█" * bars + " Enemy HP" + colours.END)

            print(bar1)

        if choice == str(5):

            if coins < 30:

                exit(code="Not ENOUGH Coins")

            enemy_hp = enemy_hp - 200

            if enemy_hp < 0:

                enemy_hp = 0

                print(colours.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colours.END)

                exit()

            print(colours.FAIL + "Enemy HP now equals to " + str(enemy_hp) + colours.END)

            coins = coins - 30

            print("You have " + str(coins) + " coins left")

            bar1_hp_now = enemy_hp / 20

            bars = round(bar1_hp_now)

            bar1 = (colours.FAIL + colours.BOLD + "█" * bars + " Enemy HP" + colours.END)

            print(bar1)

        if choice == str(6):

            if coins < 10:

                exit(code="Not ENOUGH Coins")

            enemy_hp = enemy_hp - 25

            if enemy_hp < 0:

                enemy_hp = 0

                print(colours.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colours.END)

                exit()

            print(colours.FAIL + "Enemy HP now equals to " + str(enemy_hp) + colours.END)

            coins = coins - 10

            print("You have " + str(coins) + " coins left")

            bar1_hp_now = enemy_hp / 20

            bars = round(bar1_hp_now)

            bar1 = (colours.FAIL + colours.BOLD + "█" * bars + " Enemy HP" + colours.END)

            print(bar1)
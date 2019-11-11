import random


class colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


player_hp = 500
bar_hp = 25

enemy_hp = 1000
bar1_hp = 50

time = 0

coins = 100

process = True

bar = (colors.GREEN + colors.BOLD + "█"*bar_hp + colors.ENDC + colors.BOLD + " Player HP" + colors.ENDC)
print(bar)
bar1 = (colors.FAIL + colors.BOLD +  "█"*bar1_hp + colors.ENDC + colors.BOLD + " Enemy HP" + colors.ENDC)
print(bar1)

while process == True:
    enemy_spell = random.randint(1, 9)
    if enemy_spell == 1:
        enemy_hp = enemy_hp + 200

        print(colors.FAIL + "The enemy just healed for 200 HP.\nEnemy HP now equals to " + str(enemy_hp) + colors.ENDC)

        bar1_hp_now = enemy_hp / 20
        bars = round(bar1_hp_now)

        bar1 = (colors.FAIL + colors.BOLD + "█" * bars + " Enemy HP" + colors.ENDC)
        print(bar1)

    if enemy_spell == 2:
        enemy_hp = enemy_hp + 400

        print(colors.FAIL + "The enemy just healed for 400 HP.\nEnemy HP now equals to " + str(enemy_hp) + colors.ENDC)

        bar1_hp_now = enemy_hp / 20
        bars = round(bar1_hp_now)

        bar1 = (colors.FAIL + colors.BOLD + "█" * bars + " Enemy HP" + colors.ENDC)
        print(bar1)

    if enemy_spell == str(6):
        enemy_hp = enemy_hp + 50

        print(colors.FAIL + "The enemy just healed for 50 HP.\nEnemy HP now equals to " + str(enemy_hp) + colors.ENDC)

        bar1_hp_now = enemy_hp / 20
        bars = round(bar1_hp_now)

        bar1 = (colors.FAIL + colors.BOLD + "█" * bars + " Enemy HP" + colors.ENDC)
        print(bar1)

    if enemy_hp < 0:
        enemy_hp = 0

        print("Well Done!! You defeated the enemy. In " + str(time) + " attacks.")

        exit()

    option = input(colors.BOLD + "What do you want to do?\n" + colors.BLUE + "1.Attack\n2.Spell\n" + colors.ENDC )

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

            print(colors.FAIL + "Enemy attacked for " + str(enemy_attack) + colors.ENDC)

            print(colors.GREEN + "Player HP now equals to " + str(attack) + colors.ENDC)

            print(colors.FAIL + "The enemy has defeated you!" + colors.ENDC)

            exit()

        print(colors.FAIL + colors.BOLD + "Enemy attacked for " + str(enemy_attack) + colors.ENDC)

        print(colors.GREEN + colors.BOLD + "Player HP now equals to " + str(attack) + colors.ENDC)

        player_hp = attack

        attacks = enemy_hp - player_attack

        if attacks < 0:
            attacks = 0

            print(colors.GREEN + "Player attacked for " + str(player_attack) + colors.ENDC)

            print(colors.FAIL + "Enemy HP now equals to " + str(attacks) + colors.ENDC)

            print(colors.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colors.ENDC)

            exit()

        print(colors.GREEN + colors.BOLD + "Player attacked for " + str(player_attack) + colors.ENDC)

        print(colors.FAIL + colors.BOLD + "Enemy HP now equals to " + str(attacks) + colors.ENDC + colors.ENDC)

        enemy_hp = attacks
        bar_hp_now = attack/20
        bars = round(bar_hp_now)
        bar1_hp_now = attacks/20
        bars1 = round(bar1_hp_now)

        print(bars)

        bar = (colors.GREEN + colors.BOLD + "█" * bars + " Player HP" + colors.ENDC)
        print(bar)
        bar1 = (colors.FAIL + colors.BOLD + "█" * bars1 + " Enemy HP" + colors.ENDC)
        print(bar1)

    if option == str(2):
        if coins < 0:
            exit(code="Not ENOUGH Coins")
        enemy_hp = enemy_hp + random.randint(1, 30)
        if enemy_hp < 0:
            enemy_hp = 0

            print(colors.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colors.ENDC)

            exit()
        time = time + 1

        choice = input(colors.BOLD + "What spell do you want to use?" + colors.ENDC + colors.BLUE + colors.BOLD +  "\n"
                                                   "1.Curer COST: 15\n2.Small Shield CO"
                                                   "ST: 10\n3.Big " +
                       "Shield COST: 25\n4.Grenade COST: 15\n5.C4 COST: 30\n6.Bomb COST: 10\n" + colors.ENDC)

        if choice == str(1):
            if coins < 15:
                exit(code="Not ENOUGH Coins")

            player_hp = player_hp + 100

            print(colors.GREEN + "Player HP now equals to " + str(player_hp) + colors.ENDC)

            coins = coins - 15

            print("You have " + str(coins) + " coins left")
            bar_hp_now = player_hp / 20
            bars = round(bar_hp_now)

            bar = (colors.GREEN + colors.BOLD + "█" * bars + " Player HP" + colors.ENDC)
            print(bar)

        if choice == str(2):
            if coins < 10:
                exit(code="Not ENOUGH Coins")

            player_hp = player_hp + 50

            print(colors.GREEN + "Player HP now equals to " + str(player_hp) + colors.ENDC)

            coins = coins - 10

            print("You have " + str(coins) + " coins left")
            bar_hp_now = player_hp / 20

            bars = round(bar_hp_now)
            bar = (colors.GREEN + colors.BOLD + "█" * bars + " Player HP" + colors.ENDC)
            print(bar)

        if choice == str(3):
            if coins < 25:
                exit(code="Not ENOUGH Coins")

            player_hp = player_hp + 200

            print(colors.GREEN + "Player HP now equals to " + str(player_hp) + colors.ENDC)

            coins = coins - 25

            print("You have " + str(coins) + " coins left")
            bar_hp_now = player_hp / 20
            bars = round(bar_hp_now)

            bar = (colors.GREEN + colors.BOLD + "█" * bars + " Player HP" + colors.ENDC)
            print(bar)

        if choice == str(4):
            if coins < 15:
                exit(code="Not ENOUGH Coins")

            enemy_hp = enemy_hp - 100

            if enemy_hp < 0:
                enemy_hp = 0

                print(colors.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colors.ENDC)
                exit()

            print(colors.FAIL + "Enemy HP now equals to " + str(enemy_hp) + colors.ENDC)

            coins = coins - 15

            print("You have " + str(coins) + " coins left")

            bar1_hp_now = enemy_hp / 20
            bars = round(bar1_hp_now)

            bar1 = (colors.FAIL + colors.BOLD + "█" * bars + " Enemy HP" + colors.ENDC)
            print(bar1)

        if choice == str(5):
            if coins < 30:
                exit(code="Not ENOUGH Coins")

            enemy_hp = enemy_hp - 200

            if enemy_hp < 0:
                enemy_hp = 0

                print(colors.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colors.ENDC)

                exit()

            print(colors.FAIL + "Enemy HP now equals to " + str(enemy_hp) + colors.ENDC)

            coins = coins - 30

            print("You have " + str(coins) + " coins left")

            bar1_hp_now = enemy_hp / 20
            bars = round(bar1_hp_now)

            bar1 = (colors.FAIL + colors.BOLD + "█" * bars + " Enemy HP" + colors.ENDC)
            print(bar1)

        if choice == str(6):
            if coins < 10:
                exit(code="Not ENOUGH Coins")

            enemy_hp = enemy_hp - 25

            if enemy_hp < 0:
                enemy_hp = 0

                print(colors.GREEN + "Well Done!! You defeated the enemy. In " + str(time) + " attacks." + colors.ENDC)

                exit()

            print(colors.FAIL + "Enemy HP now equals to " + str(enemy_hp) + colors.ENDC)

            coins = coins - 10

            print("You have " + str(coins) + " coins left")

            bar1_hp_now = enemy_hp / 20
            bars = round(bar1_hp_now)

            bar1 = (colors.FAIL + colors.BOLD + "█" * bars + " Enemy HP" + colors.ENDC)
            print(bar1)
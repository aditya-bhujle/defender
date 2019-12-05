import random


class Fighter:
    def __init__(self, name, is_enemy=True, bullets=1, level=1, health=3):
        self.name = name
        self.level = level
        self.health = health
        self.move = 'none'
        self.bullets = 0
        self.is_enemy = is_enemy
        self.power_up = {
            'double_reload': False
        }

    def level_up(self):
        if self.level < 10:
            self.level += 1
            print(self.name + ' has leveled up to level ' + str(self.level) + '!')
        else:
            print(self.name + ' is already max level!')

    def hurt(self):
        self.health -= 1

        if self.health > 0:
            print('     ' + self.name + ' has ' + str(self.health) + ' health')
        else:
            print('     ' + self.name + ' has died!')

    def enemy(self, enemy_fighter):
        self.enemy = enemy_fighter

    def player_move(self, move):
        self.move = move
        self.enemy.comp_move()
        # print(self.name + ' has set its move to ' + self.move)
        if move == 'attack':
            self.attack()
        elif move == 'reload':
            self.reload()
        elif move == 'block':
            print('     ' + self.name + ' used block')
        else:
            print('Error 124 has occurred')

    def comp_move(self):
        if self.enemy.bullets == 0:
            ran = random.randint(1, 2)
            if ran == 1 or self.bullets == 0:
                self.move = 'reload'
                self.reload()
            elif ran == 2:
                self.move = 'attack'
                self.attack()
        elif self.bullets == 0:
            ran = random.randint(1, 2)
            if ran == 1:
                self.move = 'reload'
                self.reload()
            elif ran == 2:
                self.move = 'block'
                print('     ' + self.name + ' used block')
        else:
            ran = random.randint(1, 5)
            if ran == 1 or ran == 2:
                self.move = 'attack'
                self.attack()
            elif ran == 3 or ran == 4:
                self.move = 'block'
                print('     ' + self.name + ' used block')
            elif ran == 5:
                self.move = 'reload'
                self.reload()
            else:
                print('Error 999')
            # 80% chance of attacking or blocking, 20% chance of reloading

    def attack(self):
        if self.bullets > 0:
            if self.enemy.move == 'attack' or self.enemy.move == 'reload':
                print('     ' + self.name + ' has attacked ' + self.enemy.name + '!')
                self.enemy.hurt()
            elif self.enemy.move == 'block':
                print('     ' + self.name + '\'s attack has been blocked by ' + self.enemy.name + '!')
            else:
                print('Error 123 has occurred, self.enemy.move is equal to ' + self.enemy.move + ' for ' + self.name)
            self.bullets -= 1
        else:
            print('     ' + self.name + ' has no bullets and its attack failed!')

    def reload(self):
        if not self.power_up['double_reload']:
            self.bullets += 1
        else:
            self.bullets += 2

        if self.bullets == 1:
            print('     ' + self.name + ' reloaded and now has 1 bullet')
        else:
            print('     ' + self.name + ' reloaded and now has ' + str(self.bullets) + ' bullets')

        if not self.is_enemy and not self.power_up['double_reload']:
            upgrade_bullets = 0
            if self.bullets >= 5:
                upgrade_bullets = 5
            elif self.bullets >= 10:
                upgrade_bullets = 10

            if upgrade_bullets:
                print('---')
                print('     You can upgrade your fighter for ' + str(upgrade_bullets) + ' bullets')
                print('     You will ' + self.power_up)

                input_value = input('     Do you want to upgrade?').lower()
                while input_value != 'yes' and input_value != 'no':
                    input_value = input('Invalid input, please answer yes or no').lower()
                if input_value == 'yes':
                    self.bullets = 0
                    self.health += 1
                    self.power_up['double_reload'] = True
                else:
                    print('Upgrade denied')

            #print('     You will gain a health and each reload will give you 2 bullets')


class Boss(Fighter):
    def __init__(self, name, level=1):
        super().__init__(name, level=1)
        print('Prepare to DIE!! I am ' + self.name + ', Destroyer of the Light!')

    def boss_level_up(self):
        self.level += 1


input_val = input('Welcome to my game! Please enter your name!')
Player = Fighter(input_val, False)

Enemy = Fighter('Enemy')
Enemy.enemy(Player)
Player.enemy(Enemy)

while Player.health > 0 and Enemy.health > 0:
    input_val = input('Please enter your move - attack, block, or reload').lower()
    while input_val != 'attack' and input_val != 'block' and input_val != 'reload' and input_val != 'quit':
        input_val = input('Invalid input, please attack block or reload').lower()
    if input_val == 'quit':
        break
    Player.player_move(input_val)

if Player.health == 0 and Enemy.health == 0:
    print('The game is a Tie!')
elif Enemy.health == 0:
    winner = Player
    print(winner.name + ' has won the game with ' + str(winner.health) + ' health!')
elif input_val == 'quit':
    print(Enemy.name + ' has won the game by forfeit!')
else:
    winner = Enemy
    print(winner.name + ' has won the game with ' + str(winner.health) + ' health!')

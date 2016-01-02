import os
from dungeon import Dungeon
from hero import Hero
from enemy import Enemy
from spell import Spell
from weapon import Weapon

gosho = Hero('Gosho', 'PigSlayer')
gosho.equip('The sting', 35)
gosho.learn('Fireball', 20, 20, 2)


def fight_mode():
    enemy = Enemy()
    os.system('clear')
    print('<<< FIGHT MODE>>>\nYou {} have just met a monster.. FIGHT your enemy to DEATH!'.format(
        gosho.known_as()))
    input('Press "ENTER" to start the fight..')
    while gosho.is_alive() and enemy.is_alive():
        os.system('clear')
        print('<<< FIGHT MODE>>>')
        print('{} health points: {}'.format(
            gosho.known_as(), gosho.get_health()))
        print('Enemy health points: {}'.format(enemy.get_health()))
        action = input('Enter "weapon" or "spell" to attack your enemy: ')
        enemy.take_damage(gosho.attack(action))
        gosho.take_damage(enemy.attack())


class gameplay:

    def __init__(name, title, level):
        self.name = name
        self.title = title
        self.level = level



def main():
    a = Dungeon('level01.txt')
    a.spawn()
    os.system('clear')
    a.print_map()
    commands = {'s': a.move_down, 'w': a.move_up,
                'a': a.move_left, 'd': a.move_right}
    while gosho.is_alive():
        comm = input('Enter command: ')
        if comm == 'esc':
            break
        status = commands[comm]()
        if status == 'Enemy_defeated':
            fight_mode()
        os.system('clear')
        a.print_map()
        if not gosho.is_alive():
            status = 'GAME OVER'
        print('Status: {}'.format(status))


if __name__ == '__main__':
    main()

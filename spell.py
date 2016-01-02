class Spell:
    def __init__(self, name='none', damage=0, mana_cost=0, cast_range=0):
        self.__name_spell = name
        self.__damage = damage
        self.__mana_cost = mana_cost
        self.__cast_range = cast_range

    def _get_damage(self):
        return self.__damage

    def get_name_spell(self):
        return self.__name_spell

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:48:34 2026

@author: TIPQC
"""

from Character import Character

class Novice(Character):
    def basicAttack(self, character):
        character.reduceHp(self.getDamage())
        print(f"{self.getUsername()} performed Basic Attack! -{self.getDamage()}")
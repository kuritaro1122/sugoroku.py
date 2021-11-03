#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random, os, time
square = [0, 0, 25] #[Playerの位置[0], Conの位置[1], マスの総数[2]]
mapStr = ["P", "C", "_"]
def rollDice(_num): #サイコロを振る(void)
        _dice = random.randint(1, 6)
        square[_num] = square[_num] + _dice if (square[_num] + _dice) < square[2] else square[2] #進む(最大square[2])
        print mapStr[_num] + '：' + str(_dice) + "マス進んだ(現在" + str(square[_num]) + "マス)"
        _map = "Start|" #Mapの表示
        for i in range(square[2]):
                _map += mapStr[0] if i == square[0] else mapStr[1] if i == square[1] else mapStr[2]
        print _map + "|Goal " + (mapStr[0] if square[0] >= square[2] else mapStr[1] if square[1] >= square[2] else " ")
while((square[0] < square[2]) and (square[1] < square[2])):
        raw_input("\nPlayerターン(Enterでサイコロを振る)")
        for j in range(2):
                rollDice(j) #サイコロを振る
                time.sleep(1.5 - j) #少し待つ
print "\n" + ("\\\You win!!//" if square[0] >= square[2] else "You lose...")
os.system("echo '\a'") #音を鳴らす

"""
遊び方
0. P : Player, C : Computer
1. Enterを押してサイコロを振る
2. Computerより先にゴールすれば勝利

※ python2 でしか動作しません。
"""

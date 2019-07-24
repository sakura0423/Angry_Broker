#!/usr/bin/env python
# -*- coding: utf-8 -*-


##创建账户
class Account():
    def __init__(self, name):
        self.balance = 100
        self.wallet_state = 1  # 1代表未封锁
        self.sig=[]
        self.s = 0
        try:
            True
        except:
            print("This name has already existed")
        else:
            self.name = name


class Game_state():
    def __init__(self):
        self.broker = None
        self.players = []
        self.flag = 0  # 0代表还没有init game
        self.bet_min = 0
        self.bet_max = 0
        self.sender = []
        self.send_content = []
        self.send_flag = []  # 1代表传钱，0代表传数据
        self.win = {'one': None, 'two': None}
        # '00'代表player赢且broker放弃押注 ‘01’代表player牌比broker大
        # '10'代表broker赢且player放弃押注 ‘11’代表broker牌比player大
        self.fair_flag_one = 0
        self.fair_flag_two = 0
        self.bet_one = None
        self.bet_two = None




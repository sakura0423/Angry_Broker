#!/usr/bin/env python
# -*- coding: utf-8 -*-


def init_game(account, bet_max, bet_min, game_state):
	if account.balance < (bet_max * 4 + bet_min * 2):
		print("You don't have enough money")
	else:
		account.wallet_state = 0
		game_state.broker = account
		game_state.bet_max = bet_max
		game_state.bet_min = bet_min
		game_state.flag = 1
		print("You successfully launch the game")


def join_game(account, game_state):
	if game_state.flag == 0:
		print("You need to initialize a game")
	elif account.balance < game_state.bet_max + game_state.bet_min:
		print("You don't have enough money to join in the game")
	else:
		send_money(account, game_state.broker, game_state, game_state.bet_min)
		game_state.players.append(account)


def upload_sig_hash(account, sig, game_state):
	hash_sig = hash(sig)
	send_data(account.name, game_state, hash_sig)
	account.sig.append(sig)


def upload_sig_1(name, sig_1, game_state, blockchain):
	hash_1 = get_data_from_blockchain(blockchain, name, 1)  # 当前块的前一个区块
	if hash_1 == hash(sig_1):
		send_data(name, game_state, sig_1)
	


def calculate_s(account, blockchain, game_state):
	if game_state.broker.name == account.name:
		str_1 = game_state.players[0].name
		str_2 = game_state.players[1].name
	elif game_state.players[0] == account.name:
		str_1 = game_state.broker.name
		str_2 = game_state.players[1].name
	else:
		str_1 = game_state.broker.name
		str_2 = game_state.players[0].name
	sig_1 = get_data_from_blockchain(blockchain, str_1, 0)
	sig_2 = get_data_from_blockchain(blockchain, str_2, 0)
	hash_s = hash(sig_1 + sig_2 + account.sig[1])
	hash_str = str(hash_s)
	for i in hash_str:
		if i.isdigit():
			account.s = account.s + int(i)  # 待定
	account.s = account.s % 100


def upload_sig_2(name, sig_2, game_state, blockchain):
	hash_2 = get_data_from_blockchain(blockchain, name, 2)  # 当前块的向前数第5个区块
	if hash_2 == hash(sig_2):
		send_data(name, game_state, sig_2)
		if game_state.players[0].name == name:
			game_state.fair_flag_one = 1
		else:
			game_state.fair_flag_two = 1


def player_bet(account, bet_flag, game_state, amount):
	if bet_flag == 0:  # 玩家放弃押注
		send_money(account, game_state.broker, game_state, 0)
		if game_state.players[0].name == account.name:
			game_state.win['one'] = '10'
		else:
			game_state.win['two'] = '10'
		print(account.name+' give up betting')
		print()
	else:
		send_money(account, game_state.broker, game_state, amount)
		if game_state.players[0].name == account.name:
			game_state.bet_one = amount
		else:
			game_state.bet_two = amount
		print(account.name + "'s bet: ", amount)
		print()

def broker_bet(bet_flag, game_state):
	if game_state.win['one']:
		if not bet_flag[0]:  # 0表示放弃押注
			game_state.win['one'] = '00'
	if game_state.win['two']:
		if not bet_flag[1]:  # 0表示放弃押注
			game_state.win['two'] = '00'


def compare_s(s_1, s_2, s_3, game_state):
	if not game_state.win['one']:
		if s_1 >= s_2:
			game_state.win['one'] = '11'
		else:
			game_state.win['one'] = '01'
	if not game_state.win['two']:
		if s_1 >= s_3:
			game_state.win['two'] = '11'
		else:
			game_state.win['two'] = '01'


def payoff(game_state):
	if game_state.win['one'] == '01':
		amount = game_state.bet_one * 2 + game_state.bet_min
		send_money(game_state.broker, game_state.players[0], game_state, amount)
	elif game_state.win['one'] == '00':
		amount = game_state.bet_min
		send_money(game_state.broker, game_state.players[0], game_state, amount)
	if game_state.win['two'] == '01':
		amount = game_state.bet_two * 2 + game_state.bet_min
		send_money(game_state.broker, game_state.players[1], game_state, amount)
	elif game_state.win['two'] == '00':
		amount = game_state.bet_min
		send_money(game_state.broker, game_state.players[1], game_state, amount)
	game_state.broker.wallet_state = 1
	game_state.flag = 0


def send_money(sender, receiver, game_state, amount):
	game_state.sender.append(sender.name)
	game_state.send_content.append(amount)
	game_state.send_flag.append(1)
	sender.balance = sender.balance - amount
	receiver.balance = receiver.balance + amount


def send_data(name, game_state, data):
	game_state.sender.append(name)
	game_state.send_content.append(data)
	game_state.send_flag.append(0)


def get_data_from_blockchain(blockchain, name, num):
	data_get = 0
	last = blockchain.last_block()
	index = last['index']
	new_index = index - num
	block = blockchain.chain[new_index-1]
	transacations = block['transactions']
	for transacation in transacations:
		if transacation['sender'] == name:
			data_get = transacation['data']
			break
	return data_get




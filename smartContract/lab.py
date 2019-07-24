#!/usr/bin/env python
# -*- coding: utf-8 -*-
from player import *
from smart_contract import *
from blockchain import *

accounts = []
new_game_flag=1

while new_game_flag:
	print()
	blockchain = BlockChain()
	players = []
	"""
		三人游戏，创建游戏账户
	"""
	while len(players) < 3:
		str_1 = input('You want to create a new account? (Y/N):')
		if str_1 == 'Y':
			name_1 = input('Please input your account name:')
			flag = 1
			for account in accounts:
				if account.name == name_1:
					print('this name has already existed')
					print()
					flag = 0
					break
			if flag:
				accounts.append(Account(name_1))
				players.append(Account(name_1))
				print()
		
		elif str_1 == 'N':
			name_1 = input('You already have an account? Please input its name: ')
			flag = 1
			for account in accounts:
				if account.name == name_1:
					flag = 0
					print("Yes. This name has already existed")
					players.append(account)
					print()
			if flag == 1:
				print("Sorry. This name doesn't exist")
				print()
		else:
			print('Please input Y or N')
	
	"""
		指定broker
		bet_max：最大押注金额
		bet_min：最少押注金额	同时为参加游戏必须缴纳的金额
	"""
	game_state = Game_state()
	while True:
		flag = 0
		for i in range(0, 3):
			str_n = players[i].name
			str_1 = input(str_n+', do you want to be broker? Y/N:')
			if str_1 == 'Y':
				str_2 = input('Please input the max bet:')
				str_3 = input('Please input the min bet:')
				try:
					bet_max = int(str_2)
					bet_min = int(str_3)
					if bet_max<bet_min:
						print('The max bet should be bigger than the min bet')
						h=6/0
					if players[i].balance < (bet_max * 4 + bet_min * 2):
						print("You don't have enough money")
						h=6/0
					flag = 1
					break
				except:
					print('Please input the suitable number')
					print('And you lose the chance to become broker')
		if flag:
			break

	"""
		初始化游戏，加入玩家
	"""
	init_game(players[i], bet_max, bet_min, game_state)
	str_1 = []
	for i in range(0, 3):
		if not players[i].name == game_state.broker.name:
			str_1.append(players[i].name)
			join_game(players[i], game_state)
	#上传玩家加入游戏后的信息和缴纳的金额
	blockchain.new_transaction(game_state.sender[0], game_state.send_content[0], game_state.send_flag[0])
	blockchain.new_transaction(game_state.sender[1], game_state.send_content[1], game_state.send_flag[1])
	proof = blockchain.proof_of_work()
	prev_hash = blockchain.hash(blockchain.chain[-1])
	blockchain.minetoblock_c(proof, prev_hash)

	print()
	print('========================Game starts========================')
	print()

	#上传第一个签名
	print("Now you all should input the first signature. And you shouldn't tell others")
	print("The program will calculate the hash of the signature")
	print("And then put the hash at the billboard")
	print()
	print(game_state.broker.name+", please input your first signature")
	str_1 = input("Your signature_1:")
	print(game_state.players[0].name+", please input your first signature")
	str_2 = input("Your signature_1:")
	print(game_state.players[1].name+", please input your first signature")
	str_3 = input("You signature_1:")

	upload_sig_hash(game_state.broker, str_1, game_state)
	upload_sig_hash(game_state.players[0], str_2, game_state)
	upload_sig_hash(game_state.players[1], str_3, game_state)

	blockchain.new_transaction(game_state.sender[2], game_state.send_content[2], game_state.send_flag[2])
	blockchain.new_transaction(game_state.sender[3], game_state.send_content[3], game_state.send_flag[3])
	blockchain.new_transaction(game_state.sender[4], game_state.send_content[4], game_state.send_flag[4])
	proof = blockchain.proof_of_work()
	prev_hash = blockchain.hash(blockchain.chain[-1])
	blockchain.minetoblock_c(proof, prev_hash)
	print()

	#上传第二个签名
	print("Now you all should input the second signature.And you shouldn't tell others")
	print("The program will calculate the hash of the signature")
	print("And then put the hash at the billboard")
	print()
	print(game_state.broker.name+", please input your second signature")
	str_1 = input("Your signature_2:")
	print(game_state.players[0].name+", please input your second signature")
	str_2 = input("Your signature_2:")
	print(game_state.players[1].name+", please input your second signature")
	str_3 = input("You signature_2:")

	upload_sig_hash(game_state.broker, str_1, game_state)
	upload_sig_hash(game_state.players[0], str_2, game_state)
	upload_sig_hash(game_state.players[1], str_3, game_state)

	blockchain.new_transaction(game_state.sender[5], game_state.send_content[5], game_state.send_flag[5])
	blockchain.new_transaction(game_state.sender[6], game_state.send_content[6], game_state.send_flag[6])
	blockchain.new_transaction(game_state.sender[7], game_state.send_content[7], game_state.send_flag[7])
	proof = blockchain.proof_of_work()
	prev_hash = blockchain.hash(blockchain.chain[-1])
	blockchain.minetoblock_c(proof, prev_hash)

	#再次上传第一个签名，验证后发送给其他人
	print()
	print("Now you all should input the first signature.And we will show it to other people")
	print("Please ensure that you input the correct signature. And you will have 2 chances")
	print("If all wrong, the game will be over. ")
	print("And your guarantee fee will be sent to the other two people")
	print()

	print(game_state.broker.name+", please input your first signature again")
	str_1 = input("Your signature_1:")
	print(game_state.players[0].name+", please input your first signature again")
	str_2 = input("Your signature_1:")
	print(game_state.players[1].name+", please input your first signature again")
	str_3 = input("You signature_1:")

	upload_sig_1(game_state.broker.name, str_1, game_state, blockchain)
	try:
		if not len(game_state.sender) == 9:
			h=6/0
	except:
		print(game_state.broker.name+", Please input the right signature")
		str_1 = input("Your signature_1:")
		upload_sig_1(game_state.broker.name, str_1, game_state, blockchain)
	try:
		if not len(game_state.sender) == 9:
			h=6/0
	except:
		print(game_state.broker.name+", you cheated others. Game over.")
		print("And you will lose", game_state.bet_min*2,"dollar")
		send_money(game_state.broker, game_state.players[0], game_state, game_state.bet_min)
		send_money(game_state.broker, game_state.players[1], game_state, game_state.bet_min)
		blockchain.new_transaction(game_state.sender[8], game_state.send_content[8], game_state.send_flag[8])
		blockchain.new_transaction(game_state.sender[9], game_state.send_content[9], game_state.send_flag[9])
		proof = blockchain.proof_of_work()
		prev_hash = blockchain.hash(blockchain.chain[-1])
		blockchain.minetoblock_c(proof, prev_hash)
		print()
		print("broker(", game_state.broker.name, ")'s balance:", game_state.broker.balance)
		print("player_1(", game_state.players[0].name, ")'s balance:", game_state.players[0].balance)
		print("player_2(", game_state.players[1].name, ")'s balance", game_state.players[1].balance)
		exit()


	upload_sig_1(game_state.players[0].name, str_2, game_state, blockchain)
	try:
		if not len(game_state.sender) == 10:
			h=6/0
	except:
		print(game_state.players[0].name+", Please input the right signature")
		str_2 = input("Your signature_1:")
		upload_sig_1(game_state.players[0].name, str_2, game_state, blockchain)
	try:
		if not len(game_state.sender) == 10:
			h=6/0
	except:
		print(ame_state.players[0].name+", you cheated others. Game over.")
		print("And you will lose ", game_state.bet_min," dollar")
		send_money(game_state.players[0], game_state.broker, game_state, game_state.bet_min/2)
		send_money(game_state.players[0], game_state.players[1], game_state, game_state.bet_min/2)
		send_money(game_state.broker, game_state.players[1], game_state, game_state.bet_min)
		blockchain.new_transaction(game_state.sender[9], game_state.send_content[9], game_state.send_flag[9])
		blockchain.new_transaction(game_state.sender[10], game_state.send_content[10], game_state.send_flag[10])
		blockchain.new_transaction(game_state.sender[11], game_state.send_content[11], game_state.send_flag[11])
		proof = blockchain.proof_of_work()
		prev_hash = blockchain.hash(blockchain.chain[-1])
		blockchain.minetoblock_c(proof, prev_hash)
		print()
		print("broker(", game_state.broker.name, ")'s balance:", game_state.broker.balance)
		print("player_1(", game_state.players[0].name, ")'s balance:", game_state.players[0].balance)
		print("player_2(", game_state.players[1].name, ")'s balance", game_state.players[1].balance)
		exit()

	upload_sig_1(game_state.players[1].name, str_3, game_state, blockchain)
	try:
		if not len(game_state.sender)==11:
			h=6/0
	except:
		print(game_state.players[1].name+", Please input the right signature")
		str_3=input("Your signature_1:")
		upload_sig_1(game_state.players[1].name, str_3, game_state, blockchain)
	try:
		if not len(game_state.sender) == 11:
			h=6/0
	except:
		print(game_state.players[1].name+", you cheated others. Game over.")
		print("And you will lose ", game_state.bet_min," dollar")
		send_money(game_state.players[1], game_state.players[0], game_state, game_state.bet_min/2)
		send_money(game_state.players[1], game_state.broker, game_state, game_state.bet_min/2)
		send_money(game_state.broker, game_state.players[0], game_state, game_state.bet_min)
		blockchain.new_transaction(game_state.sender[10], game_state.send_content[10], game_state.send_flag[10])
		blockchain.new_transaction(game_state.sender[11], game_state.send_content[11], game_state.send_flag[11])
		blockchain.new_transaction(game_state.sender[12], game_state.send_content[12], game_state.send_flag[12])
		proof = blockchain.proof_of_work()
		prev_hash = blockchain.hash(blockchain.chain[-1])
		blockchain.minetoblock_c(proof, prev_hash)
		print()
		print("broker(", game_state.broker.name, ")'s balance:", game_state.broker.balance)
		print("player_1(", game_state.players[0].name, ")'s balance:", game_state.players[0].balance)
		print("player_2(", game_state.players[1].name, ")'s balance", game_state.players[1].balance)
		exit()
		
	blockchain.new_transaction(game_state.sender[8], game_state.send_content[8], game_state.send_flag[8])
	blockchain.new_transaction(game_state.sender[9], game_state.send_content[9], game_state.send_flag[9])
	blockchain.new_transaction(game_state.sender[10], game_state.send_content[10], game_state.send_flag[10])
	proof = blockchain.proof_of_work()
	prev_hash = blockchain.hash(blockchain.chain[-1])
	blockchain.minetoblock_c(proof, prev_hash)


	#calculate the secret
	print()
	calculate_s(game_state.broker, blockchain, game_state)
	calculate_s(game_state.players[0], blockchain, game_state)
	calculate_s(game_state.players[1], blockchain, game_state)

	print("Now everyone has calculated their secret. And they will keep it secret")
	print("None of them know the others' secrets")
	print()
	print("broker(", game_state.broker.name, ")'s secret:", game_state.broker.s)
	print("player_1(", game_state.players[0].name, ")'s secret:", game_state.players[0].s)
	print("player_2(", game_state.players[1].name, ")'s secret:", game_state.players[1].s)
	
	#players input their bet
	print()
	print("Now Players should input their bet")
	print()
	str_1 = input(game_state.players[0].name+", do you want to give up betting? Y/N:")
	if str_1 == 'Y':
		bet_flag_0 = 0
		amount = 0
	else:
		bet_flag_0 = 1
		while True:
			str_2 = input("Please input your bet:")
			amount = int(str_2)
			if amount <= game_state.bet_max and amount >= game_state.bet_min:
				break
			print("The max bet is ", game_state.bet_max, ", and the min bet is ", game_state.bet_min)
			print("Ensure that your bet is between the max bet and min bet")
	player_bet(game_state.players[0], bet_flag_0, game_state, amount)
			
	str_1 = input(game_state.players[1].name+", do you want to give up betting? Y/N:")
	if str_1 == 'Y':
		bet_flag_1 = 0
		amount = 0
	else:
		bet_flag_1 = 1
		while True:
			str_2 = input("Please input your bet:")
			amount = int(str_2)
			if amount <= game_state.bet_max and amount >= game_state.bet_min:
				break
			print("The max bet is ", game_state.bet_max, ", and the min bet is ", game_state.bet_min)
			print("Ensure that your bet is between the max bet and min bet")
	player_bet(game_state.players[1], bet_flag_1, game_state, amount)

	blockchain.new_transaction(game_state.sender[11], game_state.send_content[11], game_state.send_flag[11])
	blockchain.new_transaction(game_state.sender[12], game_state.send_content[12], game_state.send_flag[12])
	proof = blockchain.proof_of_work()
	prev_hash = blockchain.hash(blockchain.chain[-1])
	blockchain.minetoblock_c(proof, prev_hash)

	# Broker input his bet
	print()
	beg_flag = []
	if game_state.bet_one:
		print(game_state.players[0].name+"'s bet is ", game_state.bet_one)
		str_1 = input("Broker, do you want to give up betting with him? Y/N:")
		if str_1 == 'Y':
			print(game_state.players[0].name+", broker gives up betting for you")
			beg_flag.append(0)
		else:
			beg_flag.append(1)
	else:
		beg_flag.append(1)
		print("Broker, "+game_state.players[0].name+" gives up betting for you")
		print()


	if game_state.bet_two:
		print(game_state.players[1].name+"'s bet is ", game_state.bet_two)
		str_1 = input("Broker, do you want to give up betting with him? Y/N:")
		if str_1 == 'Y':
			print(game_state.players[1].name+", broker gives up betting for you")
			print()
			beg_flag.append(0)
		else:
			beg_flag.append(1)
	else:
		beg_flag.append(1)
		print("Broker, "+game_state.players[1].name+" gives up betting for you")
		print()

	broker_bet(beg_flag, game_state)

	#compare s and upload signature_2
	compare_s(game_state.broker.s, game_state.players[0].s, game_state.players[1].s, game_state)

	print()
	print("Now you all should input the second signature.And we will show it to other people")
	print("Please ensure that you input the correct signature. And you will have 2 chances")
	print("If all wrong, the game will be over. ")
	print("And your guarantee fee will be sent to other people")
	print()

	print(game_state.broker.name+", please input your second signature again")
	str_1 = input("Your signature_2:")
	print(game_state.players[0].name+", please input your second signature again")
	str_2 = input("Your signature_2:")
	print(game_state.players[1].name+", please input your second signature again")
	str_3 = input("You signature_2:")

	upload_sig_2(game_state.broker.name, str_1, game_state, blockchain)
	try:
		if not len(game_state.sender)==14:
			h=6/0
	except:
		print(game_state.broker.name+", please input the right signature")
		str_1=input("Your signature_2:")
		upload_sig_2(game_state.broker.name, str_1, game_state, blockchain)
	try:
		if not len(game_state.sender)==14:
			h=6/0
	except:
		print(game_state.broker.name+", you cheated others. We have defaulted you lose the game.")
		send_data(game_state.broker.name, game_state, 00000)
		if game_state.bet_one:
			game_state.win['one']='00'
		else:
			game_state.win['one']='01'
		if game_state.bet_two:
			game_state.win['two']='00'
		else:
			game_state.win['two']='01'
		
	upload_sig_2(game_state.players[0].name, str_2, game_state, blockchain)
	try:
		if not len(game_state.sender)==15:
			h=6/0
	except:
		print(game_state.players[0].name+", please input the right signature")
		str_2=input("Your signature_2:")
		upload_sig_2(game_state.players[0].name, str_2, game_state, blockchain)
	try:
		if not len(game_state.sender)==15:
			h=6/0
	except:
		print(game_state.players[0].name+", you cheated others. We have defaulted you lose the game.")
		send_data(game_state.players[0].name, game_state, 00000)
		if game_state.bet_one:
			game_state.win['one']='10'
		else:
			game_state.win['one']='11'

	upload_sig_2(game_state.players[1].name, str_3, game_state, blockchain)
	try:
		if not len(game_state.sender)==16:
			h=6/0
	except:
		print(game_state.players[1].name+", please input the right signature")
		str_3=input("Your signature_2:")
		upload_sig_2(game_state.players[1].name, str_3, game_state, blockchain)
	try:
		if not len(game_state.sender)==16:
			h=6/0
	except:
		print(game_state.players[1].name+", you cheated others. We have defaulted you lose the game.")
		send_data(game_state.players[1].name, game_state, 00000)
		if game_state.bet_two:
			game_state.win['two']='10'
		else:
			game_state.win['two']='11'
		
	blockchain.new_transaction(game_state.sender[13], game_state.send_content[13], game_state.send_flag[13])
	blockchain.new_transaction(game_state.sender[14], game_state.send_content[14], game_state.send_flag[14])
	blockchain.new_transaction(game_state.sender[15], game_state.send_content[15], game_state.send_flag[15])
	proof = blockchain.proof_of_work()
	prev_hash = blockchain.hash(blockchain.chain[-1])
	blockchain.minetoblock_c(proof, prev_hash)

	#payoff
	payoff(game_state)
	print("broker(", game_state.broker.name, ")'s secret:", game_state.broker.s)
	print("player_1(", game_state.players[0].name, ")'s secret:", game_state.players[0].s)
	print("player_2(", game_state.players[1].name, ")'s secret:", game_state.players[1].s)
	print()
	print("broker(", game_state.broker.name, ")'s balance:", game_state.broker.balance)
	print("player_1(", game_state.players[0].name, ")'s balance:", game_state.players[0].balance)
	print("player_2(", game_state.players[1].name, ")'s balance", game_state.players[1].balance)
	print()
	str_1 = input(game_state.broker.name+", continue to play? Y/N:")
	str_2 = input(game_state.players[0].name+", continue to play? Y/N:")
	str_3 = input(game_state.players[1].name+", continue to play? Y/N:")

	if not str_1+str_2+str_3=='YYY':
		new_game_flag=0
		print("Game over")







	




				
			
	




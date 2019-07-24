from player import *
from smart_contract import *
from blockchain import *
print('start==============')
blockchain = BlockChain()

broker = Account("broker")
player_1 = Account("player_1")
player_2 = Account("player_2")

game_state = Game_state()
init_game(broker, 22, 6, game_state)
join_game(player_1, game_state)
join_game(player_2, game_state)

blockchain.new_transaction(game_state.sender[0], game_state.send_content[0], game_state.send_flag[0])
blockchain.new_transaction(game_state.sender[1], game_state.send_content[1], game_state.send_flag[1])
proof = blockchain.proof_of_work()
prev_hash = blockchain.hash(blockchain.chain[-1])
blockchain.minetoblock_c(proof, prev_hash)


upload_sig_hash(broker, 'c', game_state)
upload_sig_hash(player_1, 'e', game_state)
upload_sig_hash(player_2, 'a', game_state)


blockchain.new_transaction(game_state.sender[2], game_state.send_content[2], game_state.send_flag[2])
blockchain.new_transaction(game_state.sender[3], game_state.send_content[3], game_state.send_flag[3])
blockchain.new_transaction(game_state.sender[4], game_state.send_content[4], game_state.send_flag[4])
proof = blockchain.proof_of_work()
prev_hash = blockchain.hash(blockchain.chain[-1])
blockchain.minetoblock_c(proof, prev_hash)




upload_sig_hash(broker, 'd', game_state)
upload_sig_hash(player_1, 'b', game_state)
upload_sig_hash(player_2, 'f', game_state)

blockchain.new_transaction(game_state.sender[5], game_state.send_content[5], game_state.send_flag[5])
blockchain.new_transaction(game_state.sender[6], game_state.send_content[6], game_state.send_flag[6])
blockchain.new_transaction(game_state.sender[7], game_state.send_content[7], game_state.send_flag[7])
proof = blockchain.proof_of_work()
prev_hash = blockchain.hash(blockchain.chain[-1])
blockchain.minetoblock_c(proof, prev_hash)



upload_sig_1('broker', 'c', game_state, blockchain)
upload_sig_1('player_1', 'e', game_state, blockchain)
upload_sig_1('player_2', 'a', game_state, blockchain)

blockchain.new_transaction(game_state.sender[8], game_state.send_content[8], game_state.send_flag[8])
blockchain.new_transaction(game_state.sender[9], game_state.send_content[9], game_state.send_flag[9])
blockchain.new_transaction(game_state.sender[10], game_state.send_content[10], game_state.send_flag[10])
proof = blockchain.proof_of_work()
prev_hash = blockchain.hash(blockchain.chain[-1])
blockchain.minetoblock_c(proof, prev_hash)



calculate_s(broker, blockchain, game_state)
calculate_s(player_1, blockchain, game_state)
calculate_s(player_2, blockchain, game_state)

player_bet(player_1, 1, game_state, 15)
player_bet(player_2, 0, game_state, 0)

broker_bet([1, 1], game_state)

blockchain.new_transaction(game_state.sender[11], game_state.send_content[11], game_state.send_flag[11])
blockchain.new_transaction(game_state.sender[12], game_state.send_content[12], game_state.send_flag[12])
proof = blockchain.proof_of_work()
prev_hash = blockchain.hash(blockchain.chain[-1])
blockchain.minetoblock_c(proof, prev_hash)

compare_s(broker.s, player_1.s, player_2.s, game_state)
upload_sig_2('broker', 'd', game_state, blockchain)
upload_sig_2('player_1', 'b', game_state, blockchain)
upload_sig_2('player_2', 'f', game_state, blockchain)

blockchain.new_transaction(game_state.sender[13], game_state.send_content[13], game_state.send_flag[13])
blockchain.new_transaction(game_state.sender[14], game_state.send_content[14], game_state.send_flag[14])
blockchain.new_transaction(game_state.sender[15], game_state.send_content[15], game_state.send_flag[15])
proof = blockchain.proof_of_work()
prev_hash = blockchain.hash(blockchain.chain[-1])
blockchain.minetoblock_c(proof, prev_hash)

payoff(game_state)

print("---------------状态机部分---------------")

print("****name****")
print(broker.name)
print(player_1.name)
print(player_2.name)
print()

print("****wallet****")
print("broker's balance:" ,broker.balance)
print("player_1's balance:",player_1.balance)
print("player_2's balance",player_2.balance)
print()

print("****sig_1****")
print("broker sig_1: ", game_state.send_content[8])
print("player_1 sig_1: ", game_state.send_content[9])
print("player_2 sig_1: ", game_state.send_content[10])
print()

print("****sig_1 hash****")
print("broker sig_1 hash: ", game_state.send_content[2])
print("player_1 sig_1 hash: ", game_state.send_content[3])
print("player_2 sig_1 hash: ", game_state.send_content[4])
print()

print("****sig_2****")
print("broker sig_2: ", game_state.send_content[13])
print("player_1 sig_2: ", game_state.send_content[14])
print("player_2 sig_2: ", game_state.send_content[15])
print()

print("****sig_2 hash****")
print("broker sig_2 hash: ", game_state.send_content[5])
print("player_1 sig_2 hash: ", game_state.send_content[6])
print("player_2 sig_2 hash: ", game_state.send_content[7])
print()

print("****s****")
print("broker s: ", broker.s)
print("player_1 s: ", player_1.s)
print("player_2 s: ", player_2.s)
print()

print("****play bet_money****")
print("player_1 bet_money: ", game_state.send_content[11])
print("player_2 bet_money: ", game_state.send_content[12])
print()

print("****broker bet_money****")
player_bet(player_1, 1, game_state, 15)
player_bet(player_2, 0, game_state, 0)
print()

print("---------------block B部分---------------")
for i in blockchain.transactions:
    print(i)
    print()


print("---------------block C部分---------------")
for i in blockchain.chain:
    print(i)
    print()








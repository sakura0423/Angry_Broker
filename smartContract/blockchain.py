import hashlib
from time import time


class BlockChain:
    """
        区块链结构体
            chain:包含的区块列表  索引从1开始向后计数
            current_transactions:存储每次需要打包的交易
            transactions:存储所有交易记录
    """
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.transactions = []

        # Create the genesis block
        self.minetoblock_c(proof=100, previous_hash="")

    @staticmethod
    def hash(block):
        """
               给一个区块生成 SHA-256 值
               :param block:
               :return:
        """
        block_string = str(block).encode()
        return hashlib.sha256(block_string).hexdigest()

    def minetoblock_c(self, proof, previous_hash):
        """
        创建一个新的区块加入区块链
        :param proof: <int> 由工作证明算法生成的证明
        :param previous_hash: (Optional) <str> 前一个区块的 hash 值
        :return: <dict> 新区块
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }

        # 重置当前交易记录
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, data, flagMoneyOrData):
        """
        transactions相当于block_B
        创建一笔新的交易到下一个被挖掘的区块中
        :param sender: <str> 发送人的地址
        :param data: <int> 上传的数据
        :param flagMoneyOrData: <bool> data指的是下注金额/用户定义的数据
        :return: <int> 持有本次交易的区块索引
        """
        self.current_transactions.append({
            'sender': sender,
            'data': data,
            'flagMoneyOrData': flagMoneyOrData,
        })

        self.transactions.append({
            'sender': sender,
            'data': data,
            'flagMoneyOrData': flagMoneyOrData,
        })

    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """
        last_block = self.last_block()
        last_proof = last_block['proof']

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
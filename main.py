# Realizando importaciones
import hashlib
import json
from time import time

# Creando Clase BlockChain


class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.pendng_transactions = []

        self.new_block(
            previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.", proof=100)
# Crear un nuevo bloque

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pendng_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.pendng_transactions = []
        self.chain.append(block)

        return block
   # funcion para obtener el ultimo bloque

    @property
    def last_block(self):

        return self.chain[-1]
   # Funcion para hacer transaccion

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pendng_transactions.append(transaction)
        return self.last_block['index'] + 1
    # Generando nuestros hashes para el block

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


# Creando un nuevo blockchain y mandando dinero :D
blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
t2 = blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
t3 = blockchain.new_transaction("Satoshi", "Hal Finney", '5 BTC')
blockchain.new_block(1234)

t4 = blockchain.new_transaction("Mike", "Alice", '1 BTC')
t5 = blockchain.new_transaction("Alice", "Bob", '0.5 BTC')
t6 = blockchain.new_transaction("Bob", "Mike", '0.5 BTC')
blockchain.new_block(679)
print('Blockchain: ', blockchain.chain)

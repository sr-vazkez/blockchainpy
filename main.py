# Realizando importaciones
import hashlib
import json
from time import time

# Creando Clase BlockChain


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(
            previous_hashs="El tiempo 03/Ene/2009 Canciller al borde de un segundo rescate bancario.", proof=100)

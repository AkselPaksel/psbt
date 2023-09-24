import os
from typing import List
from bitcoin.core.script import CScript, OP_CHECKMULTISIG
from bitcoin.wallet import CBitcoinSecret
import secrets

def create_redeem_script(required_signatures: int, pub_keys):

    # Determine the required number of signatures (M)
    num_keys = len(pub_keys)
    
    # Create the redeem script dynamically
    redeem_script = CScript([required_signatures] + pub_keys + [num_keys, OP_CHECKMULTISIG])
    
    return redeem_script


def create_private_keys(numberOfKeys):
    if numberOfKeys <= 0:
        raise ValueError("numberOfKeys must be greater than 0")
    
    private_keys = []

    for _ in range(numberOfKeys):
        # Generate random bytes for private key
        secure_random_bytes = secrets.token_bytes(32)

        # Create bitcoin private key from random bytes
        private_key = CBitcoinSecret.from_secret_bytes(secure_random_bytes)

        private_keys.append(private_key)
    
    return private_keys




# # Generate three private keys
# private_key_1 = CBitcoinSecret.from_secret_bytes(secrets.token_bytes(32))
# private_key_2 = CBitcoinSecret.from_secret_bytes(secrets.token_bytes(32))
# private_key_3 = CBitcoinSecret.from_secret_bytes(secrets.token_bytes(32))

# # Derive public keys from private keys
# public_key_1 = private_key_1.pub
# public_key_2 = private_key_2.pub
# public_key_3 = private_key_3.pub

# # Create a 2-of-3 multisignature redeem script
# redeem_script = CScript([OP_CHECKMULTISIG, public_key_1, public_key_2, public_key_3, 2, OP_CHECKMULTISIG])

# # Create a Pay-to-Script-Hash (P2SH) address from the redeem script
# multisig_address = P2SHBitcoinAddress.from_redeemScript(redeem_script)

# print("Multisignature Address:", multisig_address)

# print('Public-Key 1: ' + public_key_1.hex())
# print('Public-Key 2: ' + public_key_2.hex())
# print('Public-Key 3: ' + public_key_3.hex())
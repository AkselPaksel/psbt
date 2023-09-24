""" This is a quick script for setting up a multisig adress with psbt"""

__author__ = "AkselPaksel"
__version__ = "0.1.0"
__license__ = "MIT"

import os
from typing import List
from bitcoin.wallet import CBitcoinSecret, P2SHBitcoinAddress
import unittest
from multisig import create_private_keys, create_redeem_script
from transaction import create_transaction
from utxo import get_uxos, find_utxos_for_amount

NUMBER_OF_KEYS = 3
RECIPIENT_ADRESS = ""
DESTINATION_AMOUNT = 0.01
PREV_TXS_AND_INDECES = []
SIGNER_PRIVATE_KEYS = []


def main():
    # Create given given number of private keys
    private_keys: list[CBitcoinSecret] = create_private_keys(NUMBER_OF_KEYS)

    # Create a list of public keys from the private keys
    pub_keys = [key.pub for key in private_keys]

    # Create a multisignature redeem script based on the number of private keys
    redeem_script = create_redeem_script(len(pub_keys) - 1, pub_keys) 

    # Create a Pay-to-Script-Hash (P2SH) address from the redeem script
    ps2h_address = P2SHBitcoinAddress.from_redeemScript(redeem_script)

    # Get uxos
    utxos = get_uxos()

    # Check if utxos cover transaction amount
    find_utxos_for_amount(DESTINATION_AMOUNT, utxos)

    # Create a transaction
    create_transaction(RECIPIENT_ADRESS, DESTINATION_AMOUNT, SIGNER_PRIVATE_KEYS)

    # Create a transaction
    print("redeemscript:", redeem_script.hex())
    print("Multisignature Address:", ps2h_address)









    # # Replace with your RPC username, password, and server details
    # rpc_username = "shackalackabombombom837363542"
    # rpc_password = "barrabimbarrabom123987"
    # rpc_ip = "localhost"  # Use 'localhost' if the node is running locally
    # rpc_port = 8332  # Default RPC port for Mainnet

    # # Initialize a connection to the Bitcoin Core node
    # proxy = Proxy(service_url=f"http://{rpc_username}:{rpc_password}@{rpc_ip}:{rpc_port}")

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
    

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

NUMBER_OF_KEYS = 3

def main():
    # Create given given number of private keys
    private_keys: list[CBitcoinSecret] = create_private_keys(NUMBER_OF_KEYS)

    # Create a multisignature redeem script based on the number of private keys
    redeem_script = create_redeem_script(private_keys) 

    # Create a Pay-to-Script-Hash (P2SH) address from the redeem script
    multisig_address = P2SHBitcoinAddress.from_redeemScript(redeem_script)


    # Create a transaction

    print("redeemscript:", redeem_script.hex())
    print("Multisignature Address:", multisig_address)


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
    

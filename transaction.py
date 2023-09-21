from bitcoin.core import CMutableTxOut, CMutableTxIn, CTransaction
from bitcoin.wallet import P2PKHBitcoinAddress, CBitcoinSecret
from bitcoin.core.script import CScriptWitness, SignatureHash, SIGHASH_ALL
from bitcoin.core import COutPoint, CTxInWitness
from typing import List

def create_transaction(previous_tx_id, recipient_adress):
    # Define the previous transaction output you want to spend (UTXO)
    prev_txid = previous_tx_id
    prev_tx_index = 0
    prev_tx_value = 10000000  # The value of the UTXO in satoshis

    # Create a transaction input
    txin = CMutableTxIn(COutPoint(prev_txid, prev_tx_index))

    # Create a transaction output
    destination_amount = 5000000  # Amount to send in satoshis
    txout = CMutableTxOut(destination_amount, P2PKHBitcoinAddress(recipient_adress).to_scriptPubKey())

    # Create a transaction
    tx = CTransaction([txin], [txout])

    tx

def something(redeem_script, tx: CTransaction, private_keys: List[CBitcoinSecret]):
    # Sign the transaction using participant1 and participant2's private keys
    sighash = SignatureHash(redeem_script, tx, 0, SIGHASH_ALL)
    signatures = [key.sign(sighash) + bytes([SIGHASH_ALL]) for key in private_keys]

    # Create a witness script containing the signatures and the redeem script
    witness_script = CScriptWitness([signatures, redeem_script])

    # Set the transaction's witness field
    tx.wit.vtxinwit.append(CTxInWitness(witness_script))

    # Broadcast the transaction to the network
    tx_hex = tx.serialize().hex()
    print("Signed Transaction Hex:", tx_hex)
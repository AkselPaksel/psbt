from bitcoin.core import CMutableTxOut, CMutableTxIn, CTransaction
from bitcoin.wallet import P2PKHBitcoinAddress, CBitcoinSecret
from bitcoin.core.script import CScriptWitness, SignatureHash, SIGHASH_ALL
from bitcoin.core import COutPoint, CTxInWitness, lx
from typing import List, Tuple

def create_transaction(recipient_address, destination_amount, prev_txids_and_indices):
    # Create transaction inputs
    txins = [CMutableTxIn(COutPoint(lx(txid), index)) for txid, index in prev_txids_and_indices]

    # Create a transaction output
    txout = CMutableTxOut(destination_amount, P2PKHBitcoinAddress(recipient_address).to_scriptPubKey())

    # Create a transaction
    tx = CTransaction(txins, [txout])

    return tx



def serialize_transaction(redeem_script, tx: CTransaction, private_keys: List[CBitcoinSecret]):
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
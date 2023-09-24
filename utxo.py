from bitcoin.rpc import Proxy
from bitcoin.rpc import RawProxy
# Initialize the Bitcoin proxy object

def get_uxos():
    btc_proxy = RawProxy()

    try:
        # Get the list of unspent transaction outputs (UTXOs)
        utxos = btc_proxy.listunspent()

        # Iterate through the UTXOs and print the information
        for utxo in utxos:
            print(f"TXID: {utxo['txid']}")
            print(f"Vout (Index): {utxo['vout']}")
            print(f"Amount: {utxo['amount']}")
            print(f"ScriptPubKey: {utxo['scriptPubKey']}")
            print(f"Confirmations: {utxo['confirmations']}")
            print("------")
        
        return utxos
    
    except Exception as e:
        print(f"Error occured: {e}  ")


from decimal import Decimal

def find_utxos_for_amount(target_amount, utxos):
    """
    Find the appropriate UTXOs to cover the target amount.

    Parameters:
        target_amount (Decimal): The amount to be covered.
        utxos (list): List of UTXOs available.

    Returns:
        selected_utxos (list): List of selected UTXOs.
        total_amount (Decimal): Total amount of selected UTXOs.
    """
    selected_utxos = []
    total_amount = Decimal('0.0')

    for utxo in sorted(utxos, key=lambda x: x['amount']):
        if total_amount >= target_amount:
            break
        selected_utxos.append(utxo)
        total_amount += utxo['amount']

    if total_amount < target_amount:
        raise Exception("Insufficient funds to cover the target amount.")

    return selected_utxos, total_amount

# # Sample UTXOs (replace this with the output from btc_proxy.listunspent())
# utxos = [
#     {'txid': 'txid1', 'vout': 0, 'amount': 0.005, 'scriptPubKey': 'script1', 'confirmations': 10},
#     {'txid': 'txid2', 'vout': 1, 'amount': 0.002, 'scriptPubKey': 'script2', 'confirmations': 15},
#     {'txid': 'txid3', 'vout': 0, 'amount': 0.007, 'scriptPubKey': 'script3', 'confirmations': 20},
# ]

# # Target amount
# target_amount = 0.009

# try:
#     selected_utxos, total_amount = find_utxos_for_amount(target_amount, utxos)
#     print(f"Selected UTXOs: {selected_utxos}")
#     print(f"Total Amount: {total_amount}")
# except Exception as e:
#     print(f"Error occurred: {e}")

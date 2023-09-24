from bitcoin.rpc import Proxy

proxy = Proxy()

# Fetch blockchain info
balance = proxy.getbalance()

# Print the result
print("balance:", balance)

# Replace 'your_address' with the Bitcoin address whose UTXOs you want to list
# utxos = bitcoin_proxy.listunspent(addrs=['tb1qdap0z6s8ayh9r6teq9e3rd8vlfu6kzfr8j8lrs'])

# Loop through the UTXOs and get the 'txid'
# for utxo in utxos:
#     print(utxo['txid'])

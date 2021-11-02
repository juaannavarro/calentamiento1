def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euros_value=bitcoin_amount*bitcoin_value_euros
    return euros_value

bitcoin_to_euros=25000
valor_bitcoin=bitcoinToEuros(1,bitcoin_to_euros)
print(valor_bitcoin)
if valor_bitcoin<=30000:
    print("el valor esta por debajo de 30000", valor_bitcoin)

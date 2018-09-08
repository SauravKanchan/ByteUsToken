import web3
import osa

# SHA3
seed = ''
for number in os.urandom(20):
        seed += str(number)

private_key = web3.Web3().sha3(text=seed)
private_key = private_key.hex()

object_address = web3.Account.privateKeyToAccount(private_key)
address = object_address.address

print('-'*100)
print('seed :',seed)
print('private_key :',private_key)






0x99a71bcab48cdaa69c5c2bf66601d2badf1cc42ee142f474d56cba5333647553
print('address :',address)
print('-'*100)


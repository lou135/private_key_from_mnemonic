from eth_account import Account
mnemonic_phrase=input('Your mnemonic phrase:')
def mnemonic_to_privatekey(mnemonic_phrase):
    Account.enable_unaudited_hdwallet_features()
    acct=Account.from_mnemonic(mnemonic_phrase,account_path="m/44'/60'/0'/0/0")
    return acct.key

private_key=mnemonic_to_privatekey(mnemonic_phrase)
print('Private_key:',private_key.hex())

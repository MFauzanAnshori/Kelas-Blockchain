#Mencoba encode keccak
from eth_hash.auto import keccak
preimage = keccak.new(b'Bagian-1')
print(preimage.digest())
preimage_copy = preimage.copy()
preimage.update(b'Bagian-2')
print(preimage.digest())
preimage_copy.update(b'Bagian-3')
print(preimage_copy.digest())
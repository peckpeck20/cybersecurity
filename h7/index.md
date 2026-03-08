# H7

## Applied Cryptography Summary
- Authentication, integrity, and non-repudiation are also parts of cryptography.
- A key is used in modern encryption algorithms. In certain setups, a algorithms use a different encryption key and decryption key.
- Encryption algorithms can be viewed publicly but without the key, the message cannot be decrypted.
- Symmetric algorithms - Same key for encryption and decryption.
- Asymmetric algorithms - different key for encryption and decryption.
	- Encryption key -> public key
	- Decryption key -> private
	- On paper, using quantum computing a private key could be resolved with a public key via  Shor's algorithm (factoring in polynomial time), As of now this is not possible.
- XOR - Basically a logical operator in cryptography, If the inputs are the same returns false otherwise returns true. algorithms based on this are not secure as they are relatively easy to hack by doing the following:
  - Get key length by counting coincidences
  - Shift the cipertext by the found length, esentially removing the key
  - get result

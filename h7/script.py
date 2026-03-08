'''
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
'''
#A - Convert hex to base64
import base64

def convert_hex_to_byte(hex):
    return bytes.fromhex(hex)

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
input_in_bytes = convert_hex_to_byte(hex_string)
base64_encoded = base64.b64encode(input_in_bytes).decode("ascii")
print(f'Challenge 1: {base64_encoded}')
#Challenge 1: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

#B -Fixed XOR
def fixed_xor(hex_str1, hex_str2):
    bytes1 = convert_hex_to_byte(hex_str1)
    bytes2 = convert_hex_to_byte(hex_str2)

    result_list = []
    # Pair the bytes side by side and run XOR comparison
    for b1, b2 in zip(bytes1, bytes2):
        xor_byte = b1 ^ b2
        result_list.append(xor_byte)

    # Convert the list of numbers back into a bytes object
    result_bytes = bytes(result_list)

    return result_bytes.hex()

s1 = "1c0111001f010100061a024b53535009181c"
s2 = "686974207468652062756c6c277320657965"
print(f'Challenge 2: {fixed_xor(s1, s2)}')
#Challenge 2: 746865206b696420646f6e277420706c6179

#C - Single-byte XOR cipher
single_byte_cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
magic_word = 'ETAOIN SHRDLU'

def solve_single_byte_xor(hex_cipher, magic_word):
    cipher_bytes = convert_hex_to_byte(hex_cipher)
    # set characters as lowercase and include the space character
    clean_magic_word = magic_word.lower() + " "

    def get_score(decoded_bytes):
        score = 0

        for byte in decoded_bytes:
            # Check if the character exists in the magic_word
            if chr(byte).lower() in clean_magic_word:
                score += 1
        return score

    # Track the best result
    best_score = -1
    best_key = None
    best_message = ""

    # Iterate through all 256 possible single-byte keys
    for key_candidate in range(256):
        # XOR the cipher bytes with the candidate key
        current_attempt = bytes([b ^ key_candidate for b in cipher_bytes])

        current_score = get_score(current_attempt)

        if current_score > best_score:
            best_score = current_score
            best_key = key_candidate
            best_message = current_attempt

    return best_key, best_message

single_byte_cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
magic_word = 'ETAOIN SHRDLU'
key, message = solve_single_byte_xor(single_byte_cipher, magic_word)

print('Challenge 3:')
print(f"Key Found:{key} (Character: '{chr(key)}')")
print(f"Decoded string: {message.decode()}")
#Challenge 3:
#Key Found:88 (Character: 'X')
#Decoded string:Cooking MC's like a pound of bacon

# A
import base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

input_in_bytes = bytes.fromhex(hex_string)
base64_encoded = base64.b64encode(input_in_bytes).decode("ascii")

print(base64_encoded)

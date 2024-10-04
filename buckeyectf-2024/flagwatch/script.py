# The encrypted flag as provided in the script
encrypted_flag = [62, 63, 40, 58, 39, 40, 111, 63, 52, 50, 53, 63, 104, 48, 48, 37, 3, 61, 3, 55, 57, 37, 48, 108, 59, 59, 111, 46, 33]

# The key used for XOR operation
xor_key = 92

# Decrypting the flag
decrypted_flag = ''.join(chr(value ^ xor_key) for value in encrypted_flag)

# Adding the required prefix and suffix
final_flag = decrypted_flag

print(final_flag)
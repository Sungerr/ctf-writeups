# XNOR

- Category: Crypto
- Points: 50
- Solves: 325

## Description
XNOR! It's like XOR, but it's actually the complete opposite.

[xnor.py](xnor.py)


[xnor_output.txt](xnor_output.txt)

## Solve
Reading into XNOR encryption, we kbiow that we can get the original message by simply replacing the ciphertext in its place for the encryption process. That is is we have a message M, ciphertext C, and the key K, `C = M XOR K` and `M = C XOR K`and `K = M XOR C`

Since all the tools for encryption are provided in the python file, we can simple reuse the functions with the results generated in [xnor_output.txt](xnor_output.txt).

This gives us the script

```python
def xnor_bit(a_bit, b_bit):
    if a_bit == "1" and b_bit == "1":
        return "1"
    elif a_bit == "1" and b_bit == "0":
        return "0"
    elif a_bit == "0" and b_bit == "1":
        return "0"
    elif a_bit == "0" and b_bit == "0":
        return "1"


def xnor_byte(a_byte, b_byte):
    a_bits = get_bits_from_byte(a_byte)
    b_bits = get_bits_from_byte(b_byte)

    result_bits = [xnor_bit(a_bits[i], b_bits[i]) for i in range(8)]
    result_byte = get_byte_from_bits(result_bits)
    return result_byte


def xnor_bytes(a_bytes, b_bytes):
    assert len(a_bytes) == len(b_bytes)

    return bytes([xnor_byte(a_bytes[i], b_bytes[i]) for i in range(len(a_bytes))])


def get_bits_from_byte(byte):
    return list("{:08b}".format(byte))


def get_byte_from_bits(bits):
    return int("".join(bits), 2)


def recover_key(message, encrypted_message):
    # Use XNOR to recover the key
    recovered_key = xnor_bytes(message, encrypted_message)
    return recovered_key


message = b"Blue is greener than purple for sure!"  # Original message
encrypted_message = bytes.fromhex("fe9d88f3d675d0c90d95468212b79e929efffcf281d04f0cfa6d07704118943da2af36b9f8")

# Recover the key
recovered_key = recover_key(message, encrypted_message)
print(f"Recovered Key: {recovered_key.hex()}")


def decrypt_message(encrypted_message, key):
    # Use XNOR to decrypt
    decrypted_message = xnor_bytes(encrypted_message, key)
    return decrypted_message

encrypted_flag = bytes.fromhex("de9289f08d6bcb90359f4dd70e8d95829fc8ffaf90ce5d21f96e3d635f148a68e4eb32efa4")

# Decrypt the flag
decrypted_flag = decrypt_message(encrypted_flag, recovered_key)
print(f"Decrypted Flag: {decrypted_flag.decode()}")
```

Running the script gives us

`bctf{why_xn0r_y0u_b31ng_so_3xclu51v3}`

Flag found!
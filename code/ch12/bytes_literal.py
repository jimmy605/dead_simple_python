bits = b'HELLO'

bits_escaped = b"\\A\\B\\C\\D\\E"
bits_raw = br"\A\B\C\D\E"
print(bits_raw)                  # prints b'\\A\\B\\C\\D\\E'
print(bits_escaped == bits_raw)  # prints 'True'
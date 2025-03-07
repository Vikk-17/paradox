data = [121, 103, 124, 99, 126, 81, 82, 69, 88, 117, 90, 95, 80, 80, 70, 79, 87]
key = 42
flag = ''.join(chr(c ^ key) for c in data)
print(flag)  # SMVIT{xor_puzzle}


"""
data = [121, 103, 124, 99, 126, 81, 82, 69, 88, 117, 90, 95, 80, 80, 70, 79, 87]
key = 42
"""

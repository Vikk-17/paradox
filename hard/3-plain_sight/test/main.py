secret = [83, 77, 86, 73, 84, 123, 72, 105, 100, 100, 101, 110, 95, 105, 110, 95, 112, 108, 97, 105, 110, 95, 115, 105, 103, 104, 116, 125]
flag = ''.join([chr(num) for num in secret])
print(flag)  # SMVIT{Hidden_in_plain_sight}

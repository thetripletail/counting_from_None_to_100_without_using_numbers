print(int(any(str(None))))  # 3
print(len(str(complex(bool(None)))))  # 4   in 50
print(len(bin(bool(None))))  # 3
print(len(str(None)))  # 2  in 6, 20, 52
print(len(str(bool(None))))  # 3    in 7, 10, 53
print(len(ascii(str(None))))  # 3  in 46, 54, 60
print(len(ascii(str(bool(None)))))  # 4   in 21, 55
print(len(min(dir(None))))  # 3
print(len(min(dir(Exception(None)))))  # 4
print(len(ascii(min(dir(None)))))    # 4  in 45
print(len(str(range(int(bool(None))))))  # 5
print(len(set(str(type(tuple(str(None)))))))  # 6
print(len(str(type(int(bool(None))))))  # 5 in 65, 66
print(len(hex(id(None))))  # 3 in 16, 62, 88, 91
print(len(str(id(None))))  # 3  in 63
print(len(ascii(hex(id(None)))))  # 4   in 67, 80, 85
print(max(range(len(str(type(None))))))  # 5    in 16, 71, 82
print(len(str(type(None))))  # 3    in 17, 62, 75, 86, 90
print(len(str(type(Exception(None)))))  # 4
print(len(str(list(str(None)))))  # 4   in 22, 83
print(sum(range(len(ascii(str(bool(None)))))))  # 6 in 87
print(len(ascii(str(list(str(None))))))  # 5
print(len(str(type(iter(list(str(None)))))))  # 6
print(max(range(len(dir(None)))))  # 4 in 99
print(len(dir(None)))  # 2 in 24
print(len(str(bytearray(len(bin(bool(None)))))))   # 6
print(len(dir(enumerate(str(None)))))   # 4
print(len(dir(iter(str(None)))))   # 4
print(len(set(str(dir(None)))))    # 4
print(len(str(list(ascii(str(None))))))     # 5 in 29
print(len(set(str(dir(str(None))))))    # 5
print(ord(min(str(type(None)))))    # 4  in 31
print(len(dir(Exception(None))))    # 3
print(len(str(bytearray(len(str(bool(None)))))))    # 6
print(len(dir(tuple(str(None)))))   # 4
print(len(ascii(str(bytearray(len(str(None)))))))   # 6
print(max(range(len(str(bytearray(len(ascii(str(None)))))))))   # 8
print(len(str(bytearray(len(ascii(str(None)))))))   # 6 in 37
print(max(range(len(str(enumerate(str(None)))))))   # 6
print(len(str(enumerate(str(None)))))  # 4  in 39
print(ord(next(reversed(str(tuple(str(None)))))))   # 6
print(max(range(len(dir(complex(bool(None)))))))    # 6
print(len(dir(complex(bool(None)))))    # 4 in 42
print(len(str(iter(list(str(None))))))  # 5
print(sum(range(len(ascii(min(dir(None)))))))    # 6
print(len(ascii(str(bytearray(len(ascii(str(None))))))))    # 7
print(max(range(ord(str(int(bool(None)))))))    # 6
print(ord(str(int(bool(None)))))    # 4 in 47
print(len(bin(id(None))))    # 3 in 9, 51
print(ord(str(len(str(complex(bool(None)))))))  # 6
print(len(ascii(bin(id(None)))))    # 4
print(ord(str(len(str(None)))))     # 4
print(ord(str(len(str(bool(None))))))   # 5
print(ord(str(len(ascii(str(None))))))   # 5
print(ord(str(len(ascii(str(bool(None)))))))  # 6
print(max(range(len(dir(set(str(None)))))))     # 6
print(len(dir(set(str(None)))))     # 4 in 56
print(max(range(len(dir(float(bool(None)))))))  # 6
print(len(dir(float(bool(None)))))      # 4 in 58
print(ord(next(iter(str(type(None))))))     # 5
print(max(range(ord(next(reversed(str(type(None))))))))  # 7
print(ord(next(reversed(str(type(None))))))  # 5 in 61
print(len(str(bytes(len(str(id(None)))))))  # 6
print(max(range(len(str(list(str(type(int(bool(None))))))))))   # 9
print(len(str(list(str(type(int(bool(None))))))))   # 7 in 64
print(len(str(bytearray(len(str(type(int(bool(None)))))))))     # 8
print(len(str(bytes(len(ascii(hex(id(None))))))))   # 7
print(max(range(max(range(ord(min(str(bool(None)))))))))    # 8
print(max(range(ord(min(str(bool(None)))))))    # 6 in 68
print(ord(min(str(bool(None)))))    # 4 in 69
print(len(str(bytes(max(range(len(str(type(None)))))))))    # 8
print(len(ascii(str(list(hex(id(None)))))))     # 6
print(max(range(len(dir(bool(None))))))     # 5
print(len(dir(bool(None))))    # 3  in 73
print(len(str(bytes(len(str(type(None)))))))    # 6
print(max(range(max(range(ord(min(str(None))))))))  # 7
print(max(range(ord(min(str(None))))))  # 5  in 76
print(ord(min(str(None))))  # 3 in 8, 77
print(max(range(max(range(len(dir(str(None))))))))  # 7
print(max(range(len(dir(str(None))))))  # 5 in 79
print(len(dir(str(None))))  # 3 in 80
print(len(str(bytearray(max(range(len(str(type(None)))))))))    # 8
print(len(str(bytes(len(str(list(str(None))))))))   # 7
print(ord(min(str(bool(str(None))))))   # 5
print(len(ascii(str(bytes(len(ascii(hex(id(None)))))))))    # 8
print(len(str(bytearray(len(str(type(None)))))))
print(len(str(bytes(sum(range(len(ascii(str(bool(None))))))))))     # 9
print(len(str(list(zip(range(len(hex(id(None)))))))))  # 8
print(max(range(len(str(list(str(type(None))))))))  # 7
print(len(str(list(str(type(None))))))  # 5 in 89
print(sum(range(len(hex(id(None))))))   # 5
print(max(range(ord(max(str(list(range(bool(None)))))))))   # 8
print(ord(max(str(list(range(bool(None)))))))   # 6 in 92
print(max(range(ord(min(max(dir(None)))))))     # 6
print(ord(min(max(dir(None)))))     # 4 in 94
print(max(range(max(range(ord(max(bin(bool(None)))))))))    # 8
print(max(range(ord(max(bin(bool(None)))))))    # 6 in 96
print(ord(max(bin(bool(None)))))    # 4 in 97
print(len(str(bytes(max(range(len(dir(None))))))))  # 7
print(ord(max(min(dir(str(None))))))     # 5
# AND ZERO....
print(int(bool(None)))  # 2

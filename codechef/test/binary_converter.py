inputs = [376, 440, 448, 456]
for input in inputs:
    print('{:05d} : {:015b}'.format(input, input))

z = ((165 & 1023 ^ 32) | (31 & 126)) & (31 & 126)
print(z)
print(165 & (1023 ^ 32))
print(31 & 126)

a = "Individual Price: "
b = "Tax: "
c = "Total: "
d = 12
padding = 25
print(f'{a.ljust(padding)} {d}')
print(f'{b.ljust(padding)} {d*.3}')
print(f'{c.ljust(padding)} {(d*.3)+d}')
# Some formatting lines everything up
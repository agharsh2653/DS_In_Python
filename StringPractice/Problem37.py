#Write a Python program to display a number in left, right, and center aligned with a width of 10.

x = 89343
y = f"{x:<10d}"
print(f"Left align width 10 {x:< 10d}")
print(len(y))

print(f"Right aligned (width 10) {x:10d}")

print(f"Center aligned (width 10) {x:^10d}")
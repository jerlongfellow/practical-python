# bounce.py
#
# Exercise 1.5

height = 100
bounce_back = 3/5

for _ in range(10):
    height *= bounce_back
    print(round(height, 4))

import time
print("\033[1;32mDesafio 46\033[m")

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)

for e in range(2):
    print("\033[1;31mBOOM\033[m")
    time.sleep(0.5)
    print("\033[1;32mBOOM\033[m")
    time.sleep(0.5)
    print("\033[1;33mBOOM\033[m")
    time.sleep(0.5)

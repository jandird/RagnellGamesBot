import random

if __name__ == '__main__':
    arr = [1, 1, 1, 1, 1, 1,
           2, 2, 2, 2, 2, 2,
           3, 3, 3, 3, 3, 3,
           -1, -1, -1, -1,
           -2, -2, -2, -2,
           -3, -3, -3, -3,
           4, 4]

    for i in range(0, 4):
        for j in range(0, 8):
            val = random.choice(arr)
            print(val, end="\t")
            arr.remove(val)

        print("\n")

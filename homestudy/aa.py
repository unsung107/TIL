inpu = input()

words = list(inpu[i] for i in range(len(inpu)) if i % 2 == 0)

print(''.join(words))


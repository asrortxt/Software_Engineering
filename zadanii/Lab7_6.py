with open('input.txt', 'a') as f:
    f.write('\nIm additional time')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
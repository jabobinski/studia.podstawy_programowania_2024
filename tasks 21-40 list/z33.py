array_3d = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]

for plane in array_3d:
    for row in plane:
        print(' '.join(row))
    print('\n' + '=' * 10 + '\n')
import argparse
from defs import generator

print('Task 1')

if __name__ == '__main__':
    parser1 = argparse.ArgumentParser()
    parser1.add_argument('--N', required=True, type=int)
    result1 = parser1.parse_args()
    print(generator(result1.N), '% четных чисел')


import argparse
from defs import circle
from defs import triangle
from defs import rectangle

print('Task 2')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--figure', required=True, type=str, help="select circle, triangle or rectangle")
    parser.add_argument('--radius', type=int, help="radius of circle")
    parser.add_argument('--base', type=int, help="base of triangle")
    parser.add_argument('--height', type=int, help="height of triangle")
    parser.add_argument('--length', type=int, help="length of rectangle")
    parser.add_argument('--width', type=int, help="width of rectangle")
    result = parser.parse_args()
    if result.figure == 'circle':
        print("Area of circle:", circle(result.radius))
    elif result.figure == 'triangle':
        print("Area of triangle:", triangle(result.base, result.height))
    elif result.figure == 'rectangle':
        print("Area of rectangle:", rectangle(result.length, result.width))

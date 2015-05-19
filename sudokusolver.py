#!/usr/bin/env python
import sys


def get_possibles(i, grid):
    result = []

    x, y, bx, by = int(i%9), int(i/9), int(i%9/3), int(i/9/3)

    for p in xrange(1, 10):
        ok = True

        for idx in xrange(9):
            if grid[x + idx * 9] == p or grid[idx + y * 9] == p:
                ok = False

        for yy in xrange(by * 3, by * 3 + 3):
            for xx in xrange(bx * 3, bx * 3 + 3):
                if p == grid[xx + yy * 9]:
                    ok = False

        if ok is True:
            result.append(p)

    return result


def solve(grid):
    try:
        zero_pos = grid.index(0)
    except ValueError:
        return True
    
    possibles = get_possibles(zero_pos, grid)
    for p in possibles:
        grid[zero_pos] = p
        if solve(grid) is True:
            return True
    grid[zero_pos] = 0

    return False


def print_grid(grid):
    for index, elem in enumerate(grid):
        print elem,

        if (index + 1) % 3 == 0:
            print '',
        if (index + 1) % 9 == 0:
            print ''
        if (index + 1) % 27 == 0:
            print ''


def main(argv):
    with open('input.txt') as inp:
        grid = map(int, inp.read().split())

    solved = solve(grid)

    if solved:
        print_grid(grid)
    else:
        print 'Result not found.'

if __name__ == '__main__':
    main(sys.argv[1:])
def day3_check(grid, delta):
    """Check how many trees were seen moving with delta vec on 2D grid wrapping horizontally"""
    position = (0, 0)
    grid_height, grid_width = len(grid), len(grid[0])
    num_trees = 0
    while position[0] < grid_height:
        if grid[position[0]][position[1]] == "#":
            num_trees += 1
        position = (position[0] + delta[0], (position[1] + delta[1]) % grid_width)
    return num_trees


def print_grid(grid):
    print("\n".join(grid))


def day3_1(txt):
    """
    >>> day3_1(["..##.......", "#...#...#..", ".#....#..#.", "..#.#...#.#", ".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"])
    7
    """
    grid = [list(line) for line in txt]
    return day3_check(grid, (1, 3))


def day3_2(txt):
    """
    >>> day3_2(["..##.......", "#...#...#..", ".#....#..#.", "..#.#...#.#", ".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"])
    336
    """
    grid = [list(line) for line in txt]
    vecs = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    acc_product = 1
    for vec in vecs:
        acc_product *= day3_check(grid, vec)
    return acc_product


if __name__ == "__main__":
    with open("input3.txt", "r") as fd:
        data = fd.readlines()
    lines = [l.replace("\n", "") for l in data]
    print(day3_1(lines))
    print(day3_2(lines))

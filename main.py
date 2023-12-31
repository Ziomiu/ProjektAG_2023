from tests import run_tests

if __name__ == '__main__':
    max_x = 100
    max_y = 100
    min_x = 0
    min_y = 0
    n = 100
    region = ((0, 0), (10, 10))
    run_tests(n, min_x, max_x, min_y, max_y, region)

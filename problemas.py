from math import inf

problema_1 = {
    0: {0: 0, 1: 10, 2: 15, 3: 20},
    1: {0: 5, 1: 0, 2: 9, 3: 10},
    2: {0: 6, 1: 13, 2: 0, 3: 12},
    3: {0: 8, 1: 8, 2: 9, 3: 0}
}

problema_2 = {
    0: {0: 0, 1: 12, 2: 10, 3: 19, 4: 8}, 
    1: {0: 12, 1: 0, 2: 3, 3: 7, 4: 6},
    2: {0: 10, 1: 3, 2: 0, 3: 2, 4: 20},
    3: {0: 19, 1: 7, 2: 2, 3: 0, 4: 4}, 
    4: {0: 8, 1: 6, 2: 20, 3: 4, 4: 0}
}

problema_3 = {
    0: {0: 0, 1: 12, 2: 10, 3: inf, 4: inf, 5: inf, 6: 12}, 
    1: {0: 12, 1: 0, 2: 8, 3: 12, 4: inf, 5: inf, 6: inf}, 
    2: {0: 10, 1: 8, 2: 0, 3: 11, 4: 3, 5: inf, 6: 9}, 
    3: {0: inf, 1: 12, 2: 11, 3: 0, 4: 11, 5: 10, 6: inf},
    4: {0: inf, 1: inf, 2: 3, 3: 11, 4: 0, 5: 6, 6: 7}, 
    5: {0: inf, 1: inf, 2: inf, 3: 10, 4: 6, 5: 0, 6: 9}, 
    6: {0: 12, 1: inf, 2: 9, 3: inf, 4: 7, 5: 9, 6: 0}, 
}
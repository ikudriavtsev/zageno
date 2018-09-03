import sys
from challenge import find_shortest_distance


if __name__ == '__main__':
    file_path, word1, word2 = sys.argv[1:]
    with open(file_path, 'r') as f:
        distance = find_shortest_distance(f.read(), word1, word2)
        print("Distance equals {} between words `{}` and `{}` in file {}".format(distance, word1, word2, file_path))

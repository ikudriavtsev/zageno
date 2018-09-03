import sys


def find_shortest_distance(text, word1, word2):
    if not text or not word1 or not word2 or word1 not in text or word2 not in text:
        return -1
    result = sys.maxsize
    distance = 0
    last_seen_word = ""
    for word in text.split():
        word = word.strip(',').strip('.')
        if word == word1 or word == word2:
            if not last_seen_word:
                last_seen_word = word
            elif last_seen_word == word:
                distance = 0
            elif distance <= result:
                result = distance
                distance = 0
                last_seen_word = word
        elif last_seen_word:
            distance += 1
    return result

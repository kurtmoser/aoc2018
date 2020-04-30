import collections

class BoxScanner():
    def is_n_letter_code(self, word, num_letters):
        letter_map = collections.Counter(word)

        return num_letters in letter_map.values()

    def codes_differ_by_one(self, word1, word2):
        diff = 0

        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1

                if diff > 1:
                    return False

        return True

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matches = []
        for w in word_list:
            if sorted(w) == sorted(self.word) and w.lower() != self.word.lower():
                matches.append(w)
        return matches

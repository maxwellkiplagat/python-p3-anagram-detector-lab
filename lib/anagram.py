class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def is_anagram(self, match):
        return sorted(self.word) == sorted(match.lower())

    def match(self, words):  # <- this is the required method
        return [word for word in words if self.is_anagram(word)]

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}
        for i in range(len(sentence)):
            if sentence[i] in d:
                d[sentence[i]] += 1
            else:
                d[sentence[i]] = 1
        if len(d) == 26:
            return True
        else:
            return False

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch_dict = {}
        loop_dict = {}
        total_length = 0
        for letter in chars:
            if letter not in ch_dict:
                ch_dict[letter] = 1
            else:
                ch_dict[letter] += 1
        for word in words:
            loop_dict = ch_dict.copy()
            valid = True
            for letter in word:
                if letter in loop_dict and loop_dict[letter] > 0:
                    loop_dict[letter] -= 1
                else:
                    valid = False
                    break
            if valid is True:
                total_length += len(word)
        return total_length

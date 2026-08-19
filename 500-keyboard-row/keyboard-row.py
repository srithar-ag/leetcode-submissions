class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set('qwertyuiop')
        second_row = set('asdfghjkl')
        third_row = set('zxcvbnm')
        result = []
        for word in words:
            word_chars = set(word.lower())
            if (word_chars <= first_row or 
                word_chars <= second_row or 
                word_chars <= third_row):
                result.append(word)
        return result

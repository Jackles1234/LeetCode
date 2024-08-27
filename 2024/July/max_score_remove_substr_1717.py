class Solution(object):
    def get_values(self, s, substr, val, score):
        i = 0
        s = list(s)  
        while i < len(s) - 1:
            if s[i:i+2] == list(substr):
                score += val
                del s[i:i+2]
                i = max(0, i - 1)  
            else:
                i += 1
        return score, ''.join(s)  

    def maximumGain(self, s, x, y):
        score = 0
        if x > y:
            score, s = self.get_values(s, "ab", x, score)
            score, s = self.get_values(s, "ba", y, score)
        else:
            score, s = self.get_values(s, "ba", y, score)
            score, s = self.get_values(s, "ab", x, score)
        return score
    

#### kinda correct ###

### Needed some help with part of the get_values() function
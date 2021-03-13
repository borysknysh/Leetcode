class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_length = len(words)
        wl = len(words[0])
        chunk_size = wl*words_length
        length_str = len(s)
        inds = []
        words.sort()
        
        for i in range(0,length_str-chunk_size+1,1):
            temp = []
            subs = s[i:i+chunk_size]
            for j in range(words_length):
                temp.append(subs[j*wl:(j+1)*wl])
            
            temp.sort()
            
            if temp == words:
                inds.append(i)
        return inds

class Solution:
    def isMatchUtil(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        first_inex = bool(s) and p[0] in [s[0], '.']
        if len(p) >= 2 and p[1] == '*':
            return self.isMatchUtil(s, p[2:]) or (first_inex and self.isMatchUtil(s[1:], p))
        else:
            return first_inex and self.isMatchUtil(s[1:], p[1:])
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        # time O(S*P), space O(S*P)
        def skeleton(id_s, id_p):
            if (id_s, id_p) not in cache:
                if len(p) == id_p:
                    res = len(s) == id_s
                else:
                    first_index = id_s < len(s) and p[id_p] in [s[id_s], '.']
                    if len(p) > id_p+1 and p[id_p+1 ] == '*':
                        res = skeleton(id_s,id_p+2) or (first_index and skeleton(id_s+1, id_p))
                    else:
                        res = first_index and skeleton(id_s+1, id_p+1)
                cache[(id_s, id_p)] = res
            return cache[(id_s, id_p)]
        nuKak = skeleton(0,0)
        #nuKak = self.isMatchUtil(s, p)
        return nuKak

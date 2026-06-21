# d = {sorted, all strings with that sort}
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sortd = "".join(sorted(s))
            if sortd not in d:
                d[sortd] = []
            d[sortd].append(s)
        return list(d.values())


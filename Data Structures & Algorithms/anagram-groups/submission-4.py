class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort str
        result: List[List[str]] = []

        # hmap will contain: key(sorted): List[str] (original strings)
        hmap = {}
        
        for string in strs: 
            sortedString = "".join(sorted(string))

            if sortedString not in hmap:
                # create key
                hmap[sortedString] = [string]
            else:
                hmap[sortedString].append(string)

        # {'act': ['act', 'cat'], 'opst': ['pots', 'tops', 'stop'], 'aht': ['hat']}
        for i, k in enumerate(hmap):
            result.append([])
            for v in hmap[k]:
                result[i].append(v)


        return result


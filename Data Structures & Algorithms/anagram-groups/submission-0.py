class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for i in strs:
            counter = [0] * 26

            for j in i:
                counter[ord(j) - ord('a')] += 1

            hash_map[tuple(counter)].append(i)

        return list(hash_map.values())

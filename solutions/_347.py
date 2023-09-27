class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_counter = dict()
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            element_counter[n] = 1 + element_counter.get(n, 0)

        for n, c in element_counter.items():
            freq[c].append(n)

        ret = []

        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        freq_hash = {}
        for char in s:
            freq_hash[char] = freq_hash.get(char,0)-1

        ele_freq = [[freq_hash[key],key] for key in freq_hash]

        heapq.heapify(ele_freq)
        ans = []

        while ele_freq:
            count,ele = heapq.heappop(ele_freq)
            ans.append(ele*-count)

        return "".join(ans)
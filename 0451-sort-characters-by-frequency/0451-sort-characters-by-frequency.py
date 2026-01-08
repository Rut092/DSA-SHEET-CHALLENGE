import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        freq_hash = {}
        for char in s:
            freq_hash[char] = freq_hash.get(char,0)-1

        ele_freq = [[item,key] for key,item in freq_hash.items()]

        heapq.heapify(ele_freq)
        ans = []

        for i in range(len(freq_hash)):
            count,ele = heapq.heappop(ele_freq)
            ans.append(ele*-count)

        return "".join(ans)
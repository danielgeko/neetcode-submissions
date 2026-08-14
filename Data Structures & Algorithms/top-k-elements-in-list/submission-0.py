class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        maxHeap = []
        return_list = []

        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        for number, frequency in num_dict.items():
            heapq.heappush_max(maxHeap,(frequency,number))


        for i in range(0,k):
            frequency, number = heapq.heappop_max(maxHeap)
            return_list.append(number)

        return return_list



               
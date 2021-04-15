from collections import Counter, defaultdict        
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq, result = Counter(nums), []
        inverse_freq = defaultdict(list)
        for k1,v1 in freq.items():
            inverse_freq[v1].append(k1)
        for x in range(len(nums), 0, -1):
            if x in inverse_freq:
                result.extend(inverse_freq[x])
                if len(result) >= k:
                    break
        return result[:k]


def sort_dict_by_value(dic: dict = {'a':3, 'b':5, 'c':1, 'd':2, 'e':4}) -> list:
    """Sort the key/value pair in the dictionary by its value descendingly.
    
    Args:
      
    Returns:
      
    """
    return sorted(dic.items(), key=lambda x: -x[1])


if __name__ == "__main__":
    # s = Solution()
    # print(s.topKFrequent([5,2,3,4], 4))

    letters = ['b', 'c', 'd', 'a', 'e']
    numbers = [5,1,4,2,3]

    zipList = zip(letters, numbers)
    dic = dict(zipList)

    # print(zipList)
    # print(dic)
    print(sort_dict_by_value(dic))
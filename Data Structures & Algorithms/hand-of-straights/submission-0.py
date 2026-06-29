class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from heapq import heapify, heappop
        from collections import defaultdict
        
        if len(hand) % groupSize: return False

        count = defaultdict(int)
        for num in hand:
            count[num] += 1
        
        minH = list(count.keys())
        heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in count: return False
                count[i] -= 1

                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heappop(minH)
        
        return True
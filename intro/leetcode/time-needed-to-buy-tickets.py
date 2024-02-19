class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        ans = 0
        tickets = deque(tickets)
        while True:

            if tickets[0]:
                ans += 1
                tickets[0] -= 1
            if count % len(tickets) == k:
                if not tickets[0]: return ans
            
            tickets.append(tickets.popleft())
            count += 1
        
        
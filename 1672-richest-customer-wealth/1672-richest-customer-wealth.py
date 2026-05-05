class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth=0
        
        for customer in accounts:
                total=0

                for moneny in customer:
                    total += moneny 
                if total > max_wealth:
                    max_wealth = total
        return max_wealth
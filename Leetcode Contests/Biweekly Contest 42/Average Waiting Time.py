class Solution:
    def averageWaitingTime(self, customers):
        time = 0
        times = 0
        for customer in customers:
            if time > customer[0]:
                time += customer[1]
                times += time-customer[0]
            else:
                times += customer[1]
                time = customer[0]+customer[1]
        return times/len(customers)

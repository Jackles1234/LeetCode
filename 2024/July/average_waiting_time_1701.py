def averageWaitingTime(self, customers):
    curr_time = 0
    total_wait = 0
    for i in range(len(customers)):
        if curr_time < customers[i][0]:
            curr_time = customers[i][0]
        fin_time = curr_time+customers[i][1]
        total_wait += (fin_time-customers[i][0])
        curr_time = fin_time
    return (float(total_wait)/float(len(customers)))

###CORRECT###
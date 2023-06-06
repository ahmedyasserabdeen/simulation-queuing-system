import random


class row:

    def __init__(self, iat=0, st=0, arrival=0, sstart=0, send=0, waiting=0, qlen=0,idle=0):
        self.iat = iat
        self.st = st
        self.arrival = arrival
        self.sstart = sstart
        self.send = send
        self.waiting = waiting
        self.qlen = qlen
        self.idle=idle




def getst():
    arr_st = [0.10, 0.20, 0.30, 0.25, 0.10, 0.05]
    randomnum = random.randint(1, 100)
    if 1 <= randomnum <= (arr_st[0] * 100):
        return 1
    elif (arr_st[0] * 100) < randomnum <= ((arr_st[0] * 100) + (arr_st[1] * 100)):
        return 2
    elif ((arr_st[0] + arr_st[1]) * 100) < randomnum <= (((arr_st[0] + arr_st[1] + arr_st[2]) * 100)):
        return 3
    elif ((arr_st[0] + arr_st[1] + arr_st[2]) * 100) < randomnum <= (
            ((arr_st[0] + arr_st[1] + arr_st[2] + arr_st[3]) * 100)):
        return 4
    elif ((arr_st[0] + arr_st[1] + arr_st[2] + arr_st[3]) * 100) < randomnum <= (
            ((arr_st[0] + arr_st[1] + arr_st[2] + arr_st[3] + arr_st[4]) * 100)):
        return 5
    elif ((arr_st[0] + arr_st[1] + arr_st[2] + arr_st[3] + arr_st[4]) * 100) < randomnum <= (
    ((arr_st[0] + arr_st[1] + arr_st[2] + arr_st[3] + arr_st[4] + arr_st[5]) * 100)):
        return 6



def getir():
    arr_ir = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125,0.125,0.125]
    randomnum = random.randint(1, 100)
    if 1 <= randomnum <= (arr_ir[0] * 100):
        return 1
    elif (arr_ir[0] * 100) < randomnum <= ((arr_ir[0] * 100) + (arr_ir[1] * 100)):
        return 2
    elif ((arr_ir[0] + arr_ir[1]) * 100) < randomnum <= (((arr_ir[0] + arr_ir[1] + arr_ir[2]) * 100)):
        return 3
    elif ((arr_ir[0] + arr_ir[1] + arr_ir[2]) * 100) < randomnum <= (
            ((arr_ir[0] + arr_ir[1] + arr_ir[2] + arr_ir[3]) * 100)):
        return 4
    elif ((arr_ir[0] + arr_ir[1] + arr_ir[2] + arr_ir[3]) * 100) < randomnum <= (
            ((arr_ir[0] + arr_ir[1] + arr_ir[2] + arr_ir[3] + arr_ir[4]) * 100)):
        return 5
    elif ((arr_ir[0] + arr_ir[1] + arr_ir[2] + arr_ir[3] + arr_ir[4]) * 100) < randomnum <= (
            ((arr_ir[0] + arr_ir[1] + arr_ir[2] + arr_ir[3] + arr_ir[4] + arr_ir[5]) * 100)):
        return 6
    elif ((arr_ir[0] + arr_ir[1] + arr_ir[2] + arr_ir[3] + arr_ir[4] + arr_ir[5]) * 100) < randomnum <= (
            ((arr_ir[0] + arr_ir[1] + arr_ir[2] + arr_ir[3] + arr_ir[4] + arr_ir[5] + arr_ir[6]) * 100)):
        return 7
    elif ((arr_ir[0] + arr_ir[1] + arr_ir[2] + arr_ir[3] + arr_ir[4] + arr_ir[5] + arr_ir[6]) * 100) < randomnum <= (
            ((arr_ir[0] + arr_ir[1] + arr_ir[2] + arr_ir[3] + arr_ir[4] + arr_ir[5] + arr_ir[6] + arr_ir[7]) * 100)):
        return 8

total_sum_of_avarege_waiting = 0
total_max_waiting=0
total_percent_of_queue = 0
total_percent_of_queue_10 = 0
total_percent_of_service_busy = 0
total_percent_time_over_crowded = 0
for r in range(0, 1000):
    sim_table = []
    sim_table.append(row())
    max_q = 0
    sum_of_waiting = 0
    max_waiting = 0
    num_of_queue = 0
    percent_of_queue = 0
    num_of_queue_10 = 0
    percent_of_queue_10 = 0
    service_busy = 0
    percent_of_service_busy = 0
    time_over_crowded = 0
    percent_time_over_crowded = 0
    sim_table[0].iat = getir()
    sim_table[0].st = getst()
    sim_table[0].arrival = sim_table[0].sstart = sim_table[0].iat
    sim_table[0].send = sim_table[0].sstart + sim_table[0].st
    sim_table[0].waiting = sim_table[0].qlen = 0
    sim_table[0].idle = sim_table[0].iat
    sum_of_idle = sim_table[0].idle

    for i in range(1, 100):
        sim_table.append(row())
        sim_table[i].iat = getir()
        sim_table[i].st = getst()
        sim_table[i].arrival = sim_table[i-1].arrival + sim_table[i].iat
        sim_table[i].sstart = max(sim_table[i].arrival, sim_table[i-1].send)
        sim_table[i].send = sim_table[i].sstart + sim_table[i].st
        sim_table[i].waiting = sim_table[i].sstart - sim_table[i].arrival
        sum_of_waiting += sim_table[i].waiting

        q_count = 0
        x = i
        while sim_table[i].arrival<sim_table[x].sstart and x >= 0:
            q_count += 1
            x -= 1
        sim_table[i].qlen = q_count
        if max_q<sim_table[i].qlen:
            max_q = sim_table[i].qlen
        if sim_table[i].arrival>sim_table[i-1].send:
            sim_table[i].idle = sim_table[i].arrival - sim_table[i - 1].send
        else:
            sim_table[i].idle = 0
            sum_of_idle += sim_table[i].idle
        if sim_table[i].waiting > max_waiting:
            max_waiting = sim_table[i].waiting
        if sim_table[i].qlen != 0:
            num_of_queue += 1
            if sim_table[i].waiting >= 10:
                num_of_queue_10 +=1
        sum_of_idle += sim_table[i].idle
        if sim_table[i].qlen >= 8:
            time_over_crowded = time_over_crowded + (sim_table[i-7].sstart-sim_table[i].arrival)

        

    av_waiting= sum_of_waiting / 100
    total_sum_of_avarege_waiting += av_waiting
    if max_waiting > total_max_waiting:
        total_max_waiting =max_waiting
    percent_of_queue = (num_of_queue /100)*100
    total_percent_of_queue = total_percent_of_queue + percent_of_queue
    percent_of_queue_10 = (num_of_queue_10/100)*100
    total_percent_of_queue_10 = total_percent_of_queue_10 + percent_of_queue_10
    service_busy = sim_table[99].send - sum_of_idle
    percent_of_service_busy = (service_busy/sim_table[99].send)*100
    total_percent_of_service_busy = total_percent_of_service_busy + percent_of_service_busy
    percent_time_over_crowded = (time_over_crowded/sim_table[99].send)*100
    total_percent_time_over_crowded = total_percent_time_over_crowded + percent_time_over_crowded



total_average_of_waiting = total_sum_of_avarege_waiting / 1000
total_percent_of_queue = total_percent_of_queue/1000
total_percent_of_queue_10 = total_percent_of_queue_10 /1000
total_percent_of_service_busy = total_percent_of_service_busy /1000
total_percent_time_over_crowded = total_percent_time_over_crowded /1000




print("Average waiting time for a customer =", total_average_of_waiting)
print("Maximum waiting time for a customer =", total_max_waiting)
print("Percentage of customers who need to wait in a queue =", total_percent_of_queue)
print("Percentage of customers who wait more than 10 minutes in the queue =", total_percent_of_queue_10)
print("Server utilization =", total_percent_of_service_busy)
print("Percentage of time the system is overcrowded =", total_percent_time_over_crowded)


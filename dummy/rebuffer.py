with open("buffer_logs") as buffer_logs:
    total_rebuffer = 0
    for lines in buffer_logs.readlines():
        buffer_time = lines.split(";")
        print(buffer_time)
        buffer = buffer_time[0].split(":")
        print("buffer type: ", buffer[0])
        print("ELB-SB: ", buffer[1])
        starttime_buffer_time1 = buffer_time[1].split(":")
        print("start time 1: ", starttime_buffer_time1[0])
        print("buffer time 1: ", starttime_buffer_time1[1])
        #total_rebuffer = starttime_buffer_time1[1]
        try:
            total_rebuffer = starttime_buffer_time1[1]
            starttime_buffer_time2 = buffer_time[2].split(":")
            print("start time 2: ", starttime_buffer_time2[0])
            print("buffer time 2: ", starttime_buffer_time2[1])
            total_rebuffer = starttime_buffer_time1[1] + starttime_buffer_time2[1]
            starttime_buffer_time3 = buffer_time[3].split(":")
            print("start time 3: ", starttime_buffer_time3[0])
            print("buffer time 3: ", starttime_buffer_time3[1])

            starttime_buffer_time4 = buffer_time[4].split(":")
            print("start time 4: ", starttime_buffer_time4[0])
            print("buffer time 4: ", starttime_buffer_time4[1])


            #total_rebuffer = starttime_buffer_time1[1] + starttime_buffer_time2[1] +starttime_buffer_time3[1]



        except :
            print("Invalid")


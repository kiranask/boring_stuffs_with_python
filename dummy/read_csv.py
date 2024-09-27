with open("csv_oldest") as file:
    lines= file.readlines();
    sum_of_2xx = 0
    sum_of_3xx = 0
    sum_of_4xx = 0
    sum_of_5xx = 0
    sum_of_other = 0
    sum_of_egress_hits = 0
    sum_of_404 = 0
    sum_of_429 = 0
    for line in lines:
        # print(line)
        metrics = line.split(",")
        print("record type:",metrics[0])
        print("time: ",metrics[1])
        print("arl_id: ",metrics[2])
        print("fp_config_id: ",metrics[3] )
        print("traffic_type:(String) ",metrics[4])
        print("cdn_provider: string: ",metrics[5])
        print("cpcode: ",metrics[6])
        sum_of_2xx += int(metrics[10])
        print("egress_hits: r13 ",metrics[7])
        sum_of_egress_hits += int(metrics[7])

        print("egress_volume: r9  ",metrics[8])
        print("egress_volume actual", int(metrics[7]) * 10000)

        print("egress_volume_with_overhead:r9+r41 ",metrics[9])
        print("egress volume with over head actual", int(metrics[7])*11002)
        print("hits_2xx",metrics[10])
        print("hits_3xx: ",metrics[11])
        sum_of_3xx += int(metrics[11])
        print("hits_4xx: ",metrics[12])
        sum_of_4xx += int(metrics[12])
        print("hits_5xx: ",metrics[13])
        sum_of_5xx += int(metrics[13])
        print("hits_xxx: ",metrics[14])
        sum_of_other += int(metrics[14])
        print("hits_404: ",metrics[15])
        sum_of_404 += int(metrics[15])
        print("hits_429: ",metrics[16])
        sum_of_429 += int(metrics[16])
        print("egress_ttfb(r4+r5):",metrics[17])
        print("egress_ttfb actual", (50+50)*int(metrics[7]))
        print("egress_tdt(r4+r5+r6): ",metrics[18])
        print("egress_tdt actual", (50 + 50+100) * int(metrics[7]))
        print("sum of 2xx",sum_of_2xx)
        print("sum of egress hits",sum_of_egress_hits)
        print("sum of 3xx",sum_of_3xx)
        print("sum of 4xx",sum_of_4xx)
        print("sum of 5xx",sum_of_5xx)
        print("sum of other  ", sum_of_other)
        print("sum of 404", sum_of_404)
        print("sum of 429", sum_of_429)
        print("sum of all", sum_of_2xx+sum_of_3xx+sum_of_4xx+sum_of_5xx+sum_of_other)
        print("---------------------------------------------------------")
with open('bitrate') as fi:
    bitrate = 0
    playtime = 0
    fl = 0
    for lines in fi.readlines():
        fi_list = lines.split(":")
        print(fi_list)
        print("Bitrate values: ", fi_list[0])
        if fi_list[0] not in ["-"]:
            fl = int(fi_list[0]) * int(fi_list[2])
            playtime += int(fi_list[2])


        print("Stream head positions: ", fi_list[1])

        print("play time spent: ", fi_list[2])
        print("reson code: ", fi_list[3])
        print("bitrate count: ", fi_list[4])
        bitrate += fl
        print("===============done==============")
    print("bitrate ",bitrate)
    print("playtime", playtime)
    print("fl is ", bitrate, playtime)



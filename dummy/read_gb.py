with open('ad_metrics') as gb:
    for lines in gb.readlines():
        gb_list = lines.split(":")
        print("<====================start=============================")
        print(gb_list)
        print("id is: ", gb_list[0] )
        print("ad type is: ," ,gb_list[1])
        if int(gb_list[1]) == 0:
            print("pre-roll ad")
        elif int(gb_list[1]) == 1:
            print("mid-roll ad")
        elif int(gb_list[1]) == 2:
            print("post-roll ad")
        print("ad start pos is: ", gb_list[2])
        print("ad startup time: ", gb_list[3])
        print("ad playTime: ", gb_list[4])
        print("ad playBucket: ", gb_list[5])
        if int(gb_list[5]) ==0:
            print("<25% played")
        if int(gb_list[5]) ==1:
            print("<50% played ")
        if int(gb_list[5]) ==2:
            print("<75% played")
        if int(gb_list[5]) == 3:
            print("<99% played ")
        if int(gb_list[5]) == 4:
            print("100% played")
        print("ad endStatus: ", gb_list[6])
        if int(gb_list[6]) == 0:
            print("Ad Ended Normally")
        if int(gb_list[6]) == 1:
            print("User Cloded the Ad")
        if int(gb_list[6]) == 2:
            print("Application Cloded While Playing the Ad")
        if int(gb_list[6]) == 3:
            print("Error Condition")


        print("ad adDuration: ", gb_list[7])
        print("adTitle: ", gb_list[8])
        print("adCategory: ", gb_list[9])
        print("adPartnerId: ", gb_list[10])
        print("adServer: ", gb_list[11])
        print("adDaypart: ", gb_list[12])
        print("adIndustryCategory: ", gb_list[13])
        print("adEvent: ", gb_list[14])
        print("==============end ================")




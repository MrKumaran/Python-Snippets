# Converts 12 hr frmt to 24 hr frmt

time = "12:01:00AM"

if time[-2] == "P":
    if time[:2] != '12':
        time = (time.split("PM")[0]).split(":")
        time[0] = str(int(time[0]) + 12)
        time = ":".join(time)
    else:
        time = (time.split("PM")[0]).split(":")
        time = ":".join(time)

else:
    if time[:2] == '12':
        time = (time.split("AM")[0]).split(":")
        time[0].replace("12", "00")
        time = ":".join(time)
    else:
        time = (time.split("AM")[0]).split(":")
        time = ":".join(time)
print(time)

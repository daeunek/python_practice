# This progam changes from 24 hour format to 12 hour format.
def change_time_format(hour24_time):
    hour_str, min_str = hour24_time.split(":")
    hour = int(hour_str)
    min = int(min_str)

    if hour == 0 :
        hour12 = "12:{:02d}AM".format(min)
    elif 1 <= hour <= 11:
        hour12 = "{:02d}:{:02d}AM".format(hour, min)
    elif hour == 12:
        hour12 = "12:{:02d}PM".format(hour, min)
    else:
        hour12 = "{:2d}:{:02d}PM".format(hour-12,min)

    return hour12
  
hour24_time = input("Enter 24 hour format(HH:MM): ")
hour12_time = change_time_format(hour24_time)
print("time24hourTo12hour(\"{}\") => \"{}\"".format(hour24_time,hour12_time))


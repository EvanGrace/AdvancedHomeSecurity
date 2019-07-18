from datetime import datetime
import time
myfile = open("importProbemon/currentProbemonOutput","rt")
contents = myfile.readlines()
myfile.close()
numoflines = 4
numoflines = numoflines + 1
one_unix_minute = 60
num_of_minutes = 0.25
last_mac = 0
log_time = int(time.time())
print(log_time)
open("importProbemon/wifi_data_for_email.txt","w").close()

unix_time, mac_address, manufacturer, ssid = contents[-1].split("\t")

look_back = int(unix_time) - (one_unix_minute * num_of_minutes)

writefile = open("importProbemon/wifi_data_for_email.txt","a")
writefile.write("Current Time: ")
writefile.write(str(datetime.fromtimestamp(float(unix_time))))
writefile.write("\n")
writefile.write("Time of Earliest Wifi Probe Data: ")
writefile.write(str(datetime.fromtimestamp(float(look_back))))
writefile.write("\n")

i = 1
while int(unix_time) > int(look_back):
    #print(unix_time, look_back)
    #print(datetime.fromtimestamp(float(unix_time)),datetime.fromtimestamp(float(look_back)))
    unix_time, mac_address, manufacturer, ssid = contents[-i].split("\t")
    #print(unix_time, mac_address,manufacturer, ssid)
    #print(mac_address, unix_time)
    
    writefile.write("Time: ")
    writefile.write(str(datetime.fromtimestamp(float(unix_time))))
    writefile.write("    ")
    writefile.write("Mac Address: ")
    writefile.write(mac_address)
    writefile.write("    ")
    writefile.write("Manufacturer: ")
    writefile.write(manufacturer)
    writefile.write("\t")
    writefile.write("SSID: ")
    writefile.write(ssid)
    writefile.write("\n")
    i = i + 1
    last_mac = mac_address
    #time.sleep(.1)
    
    #print("\n")

#for i in range(1,numoflines):
    ## print(contents[-i])
    #unix_time, mac_address, manufacturer, ssid = contents[-i].split("\t")
    #print(unix_time, mac_address,manufacturer, ssid)
    #print(datetime.fromtimestamp(float(unix_time)))

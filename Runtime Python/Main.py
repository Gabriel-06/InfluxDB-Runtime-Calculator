import subprocess



## defining reading and writing functions

##CHANGE THIS TO SUIT YOUR CONFIG

username = "influxuser"
password = "influxuserpassword"
address = "10.0.0.215"




def read_data():
    file = open("runtime.txt", "r")
    contents = file.read()
    file.close()
    return contents

def write_data(data):
    file = open("runtime.txt", "a")
    if data == isinstance(data, str):
        file.write(data+"\n")
    else:
        file.write(str(data)+"\n")

def get_uptime():
    process = subprocess.Popen(['uptime'], stdout=subprocess.PIPE)
    out, err = process.communicate()

    out = str(out).split(" ")

    uptime = out[4]

    uptime = uptime[:-1]

    return uptime

def write_to_influx(indata):



current_time = 0 #set current time variable to 0

current_time = read_data()

print(get_uptime())
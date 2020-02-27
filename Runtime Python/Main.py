import subprocess



#defining reading and writing functions

#CHANGE THIS TO SUIT YOUR CONFIG

#TODO write documentation for code.

username = "influxuser" #Your Influx username
password = "influxuserpassword" #Your InfluxDB password
address = "10.0.0.215" #Your InfluxDB host's IP (You can use "localhost")



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

   # TODO write function for influx


print(get_uptime())
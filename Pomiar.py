class Pomiar ():

    def __init__ (self, measure):
        self.name = measure[0]
        self.temp = measure[1]
        self.presure = measure[2]
        #self.humidity = measure[3]
        #self.altitiude = measure[4]

    def __repr__ (self):
        return (repr((self.name, self.temp, self.presure)))#, self.humidity, self.altitiude)))

def create_object (line):
    first_three = str(line[0])
    first_three = [float(first_three[0]),float(first_three[1:4]), float(first_three[4:len(str(line[0]))])]
    line = first_three + line[1:len(line)]
    for i in range (len(line)):
        line[i] = float(line[i])
    pomiar = Pomiar (line)
    return pomiar
    



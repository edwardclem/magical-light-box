import wiringpi2 

class LEDremote: 
    def toggle(self, color):
        print('Input: ',color)
        if (color == "red"): 
            if (self.redIsOn == True):
                wiringpi2.softPwmWrite(self.redPin,0) 
                self.redIsOn = False 
            elif (self.redIsOn == False): 
                wiringpi2.softPwmWrite(self.redPin , self.redLevel) 
                self.redIsOn = True
        elif (color == "blue"): 
            if (self.blueIsOn == True):  
                wiringpi2.softPwmWrite(self.bluePin,0) 
                self.blueIsOn = False 
            elif(self.blueIsOn == False):
                wiringpi2.softPwmWrite(self.bluePin, self.blueLevel) 
                self.blueIsOn=True 
        elif (color == "green"): 
            if (self.greenIsOn == True): 
                wiringpi2.softPwmWrite(self.greenPin,0) 
                self.greenIsOn = False 
            elif (self.greenIsOn == False):  
                wiringpi2.softPwmWrite(self.greenPin, self.greenLevel)
                self.greenIsOn = True 
                
    def levelSet(self,color,level): 
        if(color == "red" and self.redIsOn == True): 
            wiringpi2.softPwmWrite(self.redPin, int(level)) 
        elif(color == "blue" and self.blueIsOn == True): 
            wiringpi2.softPwmWrite(self.bluePin, int(level)) 
        elif(color == "green" and self.greenIsOn==True):
            wiringpi2.softPwmWrite(self.greenPin, int(level)) 
            
    def cleanup(self, color = None):
        wiringpi2.softPwmWrite(self.redPin,0) 
        wiringpi2.pinMode(self.redPin,0) 
        wiringpi2.softPwmWrite(self.greenPin,0) 
        wiringpi2.pinMode(self.greenPin,0) 
        wiringpi2.softPwmWrite(self.bluePin,0) 
        wiringpi2.pinMode(self.bluePin,0)
        print "goodbye"
        return False
        
    def __init__(self):  
        wiringpi2.wiringPiSetupGpio() 
        
        self.redPin = 23 
        self.bluePin = 24 
        self.greenPin = 18 
        
        wiringpi2.pinMode(self.redPin, 1)
        wiringpi2.pinMode(self.bluePin, 1)
        wiringpi2.pinMode(self.greenPin, 1)
        wiringpi2.softPwmCreate(self.redPin,0,100) 
        wiringpi2.softPwmCreate(self.bluePin,0,100) 
        wiringpi2.softPwmCreate(self.greenPin,0,100) 
        
        self.redIsOn = False 
        self.blueIsOn = False 
        self.greenIsOn = False

        self.redLevel = 100
        self.blueLevel = 100
        self.greenLevel = 100

        print('Remote initiated.')
        

if __name__=="__main__":
    def main(self): 
        remote = LEDremote()

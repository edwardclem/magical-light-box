import pygtk
pygtk.require('2.0')
import gtk 
import wiringpi2 

class LEDremote: 
    def buttonToggled(self,widget,data):
        if (data == "red"): 
            if (self.redIsOn == True):
                print "lightsoff"  
                wiringpi2.softPwmWrite(self.redPin,0) 
                self.redIsOn = False 
            elif (self.redIsOn == False): 
                wiringpi2.softPwmWrite(self.redPin , int(self.redSlider.get_value())) 
                self.redIsOn = True
                print "lightson"
        elif (data == "blue"): 
            if (self.blueIsOn == True):  
                wiringpi2.softPwmWrite(self.bluePin,0) 
                self.blueIsOn = False 
            elif(self.blueIsOn == False):
                wiringpi2.softPwmWrite(self.bluePin, int(self.blueSlider.get_value())) 
                self.blueIsOn=True 
        elif (data == "green"): 
            if (self.greenIsOn == True): 
                wiringpi2.softPwmWrite(self.greenPin,0) 
                self.greenIsOn = False 
            elif (self.greenIsOn == False):  
                wiringpi2.softPwmWrite(self.greenPin, int(self.greenSlider.get_value()))
                self.greenIsOn = True 
                
    def sliderMoved(self,widget,data): 
        if(data == "red" and self.redIsOn == True): 
            wiringpi2.softPwmWrite(self.redPin, int(self.redSlider.get_value())) 
        elif(data == "blue" and self.blueIsOn == True): 
            wiringpi2.softPwmWrite(self.bluePin, int(self.blueSlider.get_value())) 
        elif(data == "green" and self.greenIsOn==True):
            wiringpi2.softPwmWrite(self.greenPin, int(self.greenSlider.get_value())) 
            
    def cleanupHandler(self, widget, data = None): 
        print "goodbye" 
        wiringpi2.softPwmWrite(self.redPin,0) 
        wiringpi2.pinMode(self.redPin,0) 
        wiringpi2.softPwmWrite(self.greenPin,0) 
        wiringpi2.pinMode(self.greenPin,0) 
        wiringpi2.softPwmWrite(self.bluePin,0) 
        wiringpi2.pinMode(self.bluePin,0)
        gtk.main_quit() 
        return False
        
    def __init__(self): 
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL) 
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
        
        self.checkBoxBox=gtk.HBox(False,0) 
        self.sliderBox=gtk.HBox(False,0) 
        self.bigBox=gtk.VBox(False,0) 
        
        self.window.set_border_width(50) 
        self.red=gtk.CheckButton("Red",False) 
        self.red.connect("toggled",self.buttonToggled, "red") 
        self.green=gtk.CheckButton("Green",False) 
        self.green.connect("toggled",self.buttonToggled, "green") 
        self.blue=gtk.CheckButton("Blue",False) 
        self.blue.connect("toggled",self.buttonToggled, "blue") 
        self.window.connect("delete-event", self.cleanupHandler) 
        
        self.window.set_title("Magical Light Box") 
        
        self.redIsOn = False 
        self.blueIsOn = False 
        self.greenIsOn = False
        self.redSlider = gtk.VScale() 
        self.greenSlider = gtk.VScale() 
        self.blueSlider = gtk.VScale() 
        
        buttonList=[self.red,self.green,self.blue] 
        sliderList=[self.redSlider,self.greenSlider,self.blueSlider] 
        for button in buttonList: 
            self.checkBoxBox.pack_start(button,False,False,10) 
            button.show() 
            
        for slider in sliderList: 
            slider.set_range(0,100) 
            slider.set_inverted(True) 
            slider.set_round_digits(0) 
            slider.set_increments(1,100) 
            slider.set_size_request(35,150) 
            
        self.redSlider.connect("value-changed", self.sliderMoved , "red") 
        self.greenSlider.connect("value-changed", self.sliderMoved , "green") 
        self.blueSlider.connect("value-changed", self.sliderMoved , "blue") 
        
        for slider in sliderList: #I can probs merge these loops
            self.sliderBox.pack_start(slider,True,True,10) 
            slider.show() 
            
        self.bigBox.pack_start(self.checkBoxBox,False,False,10) 
        self.checkBoxBox.show() 
        
        self.bigBox.pack_start(self.sliderBox,False,False,10) 
        self.sliderBox.show() 
        self.window.add(self.bigBox) 
        self.bigBox.show() 
        self.window.show() 
        
    def main(self): 
        gtk.main() 
        
if __name__=="__main__": 
    remote = LEDremote() 
    remote.main()
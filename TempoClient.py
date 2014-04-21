import pygtk
pygtk.require('2.0')
import gtk 
import socket
import time

#this version stores the light states in an array, then sends them to the server every pulse.

class GUIremoteclient: 
    def buttonToggled(self,widget,data):
        if(data == 'pulsing' and not self.pulsing):
            print "Start pulsing"
            self.pulsing = True
        elif(data == 'pulsing' and self.pulsing):
            print "Stop pulsing"
            self.pulsing = False
        else:
            self.s.send('toggle,' + data)
                
    def sliderMoved(self,widget,data): 
        if (data == "red"): 
            #self.s.send('level,red,' + str(int(self.redSlider.get_value())))
            self.lightsConfiguration[0] = 'level,red,' + str(int(self.redSlider.get_value()))
        elif (data == "blue"): 
            self.lightsConfiguration[1] = 'level,blue,' + str(int(self.redSlider.get_value()))
        elif (data == "green"):
            self.lightsConfiguration[2] = 'level,blue,' + str(int(self.redSlider.get_value()))

        if (not pulsing):
            for data in self.lightsConfiguration:
                self.s.send(data)

            
    def cleanupHandler(self, widget, data = None): 
        print "goodbye" 
        self.s.send('exit')
        gtk.main_quit() 
        return False

    def pulse():
        self.s.send('toggle,red')
        self.s.send('toggle,blue')
        self.s.send('toggle,green')
        for data in self.lightsConfiguration:
            self.s.send(data)
            
      
        

        
    def __init__(self): 
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL) 

        #opens up connection to server
        host = 'localhost' 
        port = 60000
        size = 1024 
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.s.connect((host,port)) 
        
        self.redPin = 23 
        self.bluePin = 24 
        self.greenPin = 18 
    
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
        self.pulseBox=gtk.CheckButton("Pulsing",False)
        self.pulseBox.connect("toggled",self.buttonToggled, "pulsing")
        self.window.connect("delete-event", self.cleanupHandler) 
        
        self.window.set_title("Magical Light Box") 
        
        self.redSlider = gtk.VScale() 
        self.greenSlider = gtk.VScale() 
        self.blueSlider = gtk.VScale() 
        self.tempoSlider = gtk.VScale()
        #range: 60 to 250
        
        buttonList=[self.red,self.green,self.blue,self.pulseBox] 
        sliderList=[self.redSlider,self.greenSlider,self.blueSlider,self.tempoSlider] 
        for button in buttonList: 
            self.checkBoxBox.pack_start(button,False,False,10) 
            button.show() 
            
        for slider in sliderList: 
            if (slider == self.tempoSlider):
                slider.set_range(60,250)
            else:
                slider.set_range(0,100)
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

        self.lightConfiguration = ["" "" ""]

        while(True):
            if (self.pulsing and time.clock() % int(self.tempoSlider.get_value())/180):
                self.pulse()
        
    def main(self): 
        gtk.main() 
        
if __name__=="__main__": 
    remote = GUIremoteclient() 
    remote.main()
import pygtk
pygtk.require('2.0')
import gtk 
import socket

class GUIremoteclient: 
    def buttonToggled(self,widget,data):
       s.send('toggle,' + data)
                
    def sliderMoved(self,widget,data): 
        if(data == "red"): 
            s.send('level,red,' + str(int(self.redSlider.get_value())))
        elif(data == "blue"): 
            s.send('level,blue,' + str(int(self.blueSlider.get_value())))
        elif(data == "green"):
            s.send('level,green,' + str(int(self.greenSlider.get_value()))) 
            
    def cleanupHandler(self, widget, data = None): 
        print "goodbye" 
        s.send('cleanup')
        gtk.main_quit() 
        return False
        
    def __init__(self): 
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL) 

        #opens up connection to server
        host = 'localhost' 
        port = 60000
        size = 1024 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((host,port)) 
        
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
        self.window.connect("delete-event", self.cleanupHandler) 
        
        self.window.set_title("Magical Light Box") 
        
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
    remote = GUIremoteclient() 
    remote.main()
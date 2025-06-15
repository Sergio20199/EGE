import mouse
import keyboard
import time
class clicker:
    def __init__(self):
        self.paused = True
        self.running = True
        self.mainloop()
    
    def mainloop(self):
        while self.running:
            if not self.paused:
                mouse.press()
                mouse.release()
                time.sleep(2)
            if self.paused:
                time.sleep(0.01)
                if keyboard.is_pressed('='):
                    self.paused = False
            if keyboard.is_pressed('-'):
                self.paused = True
                print('paused')
            if keyboard.is_pressed('0'):
                self.running = False
                print('code over')
click = clicker()


            
            
                


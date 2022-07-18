import RPi.GPIO as GPIO
from rplidar import RPLidar, RPLidarException
import time
import vlc

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(40, GPIO.IN)



def findRange(array):
    for x in array:
        if(x>200 and x<500):
            return 1
            break
        


media = vlc.MediaPlayer("/home/pi/Track3Violin.mp3")
#media.play()
ses = [0,10,20,30,40,50,60,70,80,90,100]
i=0
#media.audio_set_volume(0)
res = 0
while(1):
    if(GPIO.input(5)):
        try:
            
            time.sleep(0.05)
            if(res==0):
                
                media.play()
                media.audio_set_volume(0)
                 
            res = 1
            lidar = RPLidar('/dev/ttyUSB0')
            
            for scan in (lidar.iter_scans(max_buf_meas=False)):
               
                scan_list1 = [x[2] for x in scan]
                        
                inRange = findRange(scan_list1)
                print("range :",inRange)
                if((GPIO.input(5))== 0):
                    time.sleep(0.5)
                    print("durdu")
                    lidar.stop()
                    lidar.stop_motor()
                    media.stop()
                    lidar.disconnect()
                    GPIO.setup(40, GPIO.IN)
                    
                       
    
                if (i<0):
                    i =0
                if(i>10):
                    i=10
            
                if inRange == 1:
                    
                    
                    GPIO.setup(40, GPIO.OUT)                               
                    if(i==10):
                        
                        continue
                        
                    else:
                            
                        media.audio_set_volume(ses[i])
                        i = i+1
                        print(i)
                               
                else:
                    
                  
                    if(i==0):
                        GPIO.setup(40, GPIO.IN)
                        continue
                    else:
                        media.audio_set_volume(ses[i])
                        i = i-1
        except:
            print("hata")
            
            continue
    
    else:
        GPIO.setup(40, GPIO.IN)
        res = 0
        print("low")
        
        
            
      
    
   



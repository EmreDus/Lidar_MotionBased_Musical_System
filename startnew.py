import RPi.GPIO as GPIO
from rplidar import RPLidar, RPLidarException
import time
import vlc



def findRange(array):
    for x in array:
        if(x>200 and x<500):
            return 1
            break
        


media = vlc.MediaPlayer("/home/pi/Track3Violin.mp3")
media.play()
ses = [0,10,20,30,40,50,60,70,80,90,100]
i=0
media.audio_set_volume(0)
while(1):
    
    try:
        lidar = RPLidar('/dev/ttyUSB0')
        
        for scan in (lidar.iter_scans(max_buf_meas=False)):
           
            scan_list1 = [x[2] for x in scan]
                    
            inRange = findRange(scan_list1)
            print(inRange)
            time.sleep(0.05)
    
          
            if (i<0):
                i =0
            if(i>10):
                i=10
        
            if inRange == 1:
            
                #media.audio_set_volume(100)
            
                
                if(i==10):
                    continue
                    
                else:
                        
                    media.audio_set_volume(ses[i])
                    i = i+1
                    print(i)
                           
                                            
        
            else:
            
                #media.audio_set_volume(0)
            
                        
              
                if(i==0):
                    continue
                else:
                    media.audio_set_volume(ses[i])
                    i = i-1
                    
    except:
        print("hata")
        continue
            
      
    
   

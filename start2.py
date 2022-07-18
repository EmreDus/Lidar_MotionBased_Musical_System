import RPi.GPIO as GPIO

from rplidar import RPLidar
from audioplayer import AudioPlayer
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(5, GPIO.OUT)

player = AudioPlayer("mizika.mp3")

lidar = RPLidar('/dev/ttyUSB1')

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)
a=0
player.play(loop=True)
player.volume = 0
for i, scan in enumerate(lidar.iter_scans(max_buf_meas=False)):
    #print('%d: Got %d measurments' % (i, len(scan)))
    scan_list1 = [x[2] for x in scan]
    near = min(scan_list1)
    
    #print(scan_list1)
    print(near)
    
    if near < 600:
        #player.volume=100
        if(player.volume==100):
            player.volume=100
        else:   
            player.volume = player.volume + 10    
            
        
    elif near > 600:
        if(player.volume == 0):
            player.volume = 0
        else:
            player.volume = player.volume -5
    if((GPIO.input(5))==0):
        #lidar.stop()
        player.stop()
        lidar.stop_motor()
        lidar.disconnect()
        quit()
        
        

    


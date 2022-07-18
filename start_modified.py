import time
import pyglet
from rplidar import RPLidar, RPLidarException
from pyglet.media import SourceGroup


def inRange(array):
    "muzik calmasi gerekiyorsa True degilse False doner"
    retval = False

    for x in array:
        if x > 300 and x < 500:
            retval = True
            break

    return retval


def increase_volume(volume_level: float) -> float:
    if volume_level >= 1.0:
        return volume_level
    else:
        return volume_level + 0.05


def decrease_volume(volume_level: float) -> float:
    if volume_level <= 0.0:
        return volume_level
    else:
        return volume_level - 0.05


pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
pyglet.options['search_local_libs'] = True
source = pyglet.media.StaticSource(pyglet.media.load('adamlar.mp3'))
player = pyglet.media.Player()
player.queue(source)

print("müzik yüklendi")

lidar = RPLidar("/dev/ttyUSB0")
VOLUME = 0.0
player.play()
player.volume = 0
time.sleep(5)

while True:
    time.sleep(0.05)
    try:
        # lidar scan fail olabilir
        lidar_scan = lidar.iter_scans(max_buf_meas=False)
    except RPLidarException:
        continue

    for scan in lidar_scan:
        scan_list1 = [x[2] for x in scan]

        inran = inRange(scan_list1)
        print(inran)
        if inran:
            VOLUME = increase_volume(VOLUME)
        else:
            VOLUME = decrease_volume(VOLUME)

        player.volume = VOLUME


lidar.stop()
lidar.stop_motor()
lidar.disconnect()

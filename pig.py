import pyglet

# create a player and queue the song
player = pyglet.media.Player()
sound = pyglet.media.load('tambur.mp3')
player.queue(sound) 

# keep playing for as long as the app is running (or you tell it to stop):
player.eos_action = pyglet.media.SourceGroup.loop

player.play()
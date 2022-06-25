import pygame
pygame.mixer.init()
pygame.display.init()
screen = pygame.display.set_mode((420, 240))
playlist = list()
playlist.append("scorpion102.mp4")
playlist.append("scorpion103.mp4")
playlist.append("scorpion105.mp4")
pygame.mixer.music.load(playlist.pop()) # Get the first track from the playlist
pygame.mixer.music.queue(playlist.pop()) # Queue the 2nd song
pygame.mixer.music.set_endevent(pygame.USEREVENT) # Setup the end track event
pygame.mixer.music.play() # Play the music
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: # A track has ended
            if len(playlist) > 0: # If there are more tracks in the queue...
                pygame.mixer.music.queue(playlist.pop())

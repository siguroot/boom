#!/home/jason/boom/bin/python3

import mido
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


pygame.mixer.init()

inputs = mido.get_input_names()
boom = "/home/jason/samples/drop-the-bass.wav"

for i in inputs:
    if 'AudioBox' in i:
        port = mido.open_input(i)

while True:
    msg = port.receive()
    if msg.type == "program_change" and 0 <= msg.program <= 19:
        pygame.mixer.music.load(boom)
        pygame.mixer.music.play()
        print('BOOOOOOOOM {}'.format(msg.program))

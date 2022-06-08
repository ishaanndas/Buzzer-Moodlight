import time
import board
from digitalio import DigitalInOut, Direction, Pull
import digitalio
import neopixel
import touchio

try:
    from audiocore import WaveFile
except ImportError:
    from audioio import WaveFile

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

# Enable the speaker
spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=2.0)


#Make D1 pin the button
button = DigitalInOut(board.D1)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)

audiofiles = ["rimshot.wav", "wrong.wav"]

def play_file(filename):
    print("Playing file: " + filename)
    wave_file = open(filename, "rb")
    with WaveFile(wave_file) as wave:
        with AudioOut(board.SPEAKER) as audio:
            audio.play(wave)
            while audio.playing:
                pass

#play sound and light up neopixels when button pressed
while True:
    if button.value:
        pixels.fill((0, 0, 250))
        play_file(audiofiles[0])
    if touch_A1.value:
        pixels.fill((250, 0, 0))
        play_file(audiofiles[1])
    else:
        pixels.fill((0, 0, 0))

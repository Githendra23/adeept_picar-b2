#!/usr/bin/env python3
from gpiozero import TonalBuzzer
from time import sleep

# Initialize a TonalBuzzer connected to GPIO18 (BCM)
class Buzzer:
    def __init__(self): 
        self.GPIOpin = 18
        self.tb = TonalBuzzer(self.GPIOpin)

    def play(self, tune):
        """
        Play a musical tune using the buzzer.
        :param tune: List of tuples (note, duration), 
        where each tuple represents a note and its duration.
        """
        for note, duration in tune:
            self.tb.play(note)  # Play the note on the buzzer
            sleep(float(duration))  # Delay for the duration of the note
            self.tb.stop()  # Stop playing after the tune is complete

if __name__ == "__main__":
    # Define a musical tune as a sequence of notes and durations.
    SONG =	[
    ["E5",0.3],["Eb5",0.3],
    ["E5",0.3],["Eb5",0.3],["E5",0.3],["B4",0.3],["D5",0.3],["C5",0.3],
    ["A4",0.6],[None,0.1],["C4",0.3],["E4",0.3],["A4",0.3],
    ["B4",0.6],[None,0.1],["E4",0.3],["Ab4",0.3],["B4",0.3],
    ["C5",0.6],[None,0.1],["E4",0.3],["E5",0.3],["Eb5",0.3],
    ["E5",0.3],["Eb5",0.3],["E5",0.3],["B4",0.3],["D5",0.3],["C5",0.3],
    ["A4",0.6],[None,0.1],["C4",0.3],["E4",0.3],["A4",0.3],
    ["B4",0.6],[None,0.1],["E4",0.3],["C5",0.3],["B4",0.3],["A4",0.1]
    ]
    
    try:
        buzzer = Buzzer()
        buzzer.play(SONG)  # Execute the play function to start playing the tune.

    except KeyboardInterrupt:
        # Handle KeyboardInterrupt for graceful termination
        pass

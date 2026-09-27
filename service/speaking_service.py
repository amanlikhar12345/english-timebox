import sounddevice as sd
from scipy.io.wavfile import write


class SpeakingService:

    def __init__(self):

        self.sample_rate = 44100
        self.recording = None
        self.is_recording = False

    def start_recording(self):

        self.is_recording = True
        self.recording = sd.rec(int(44100 * 60 * 10),samplerate=self.sample_rate,channels=1,dtype="int16")

    def stop_recording(self, filename):

        if not self.is_recording:
            return

        sd.stop()
        self.is_recording = False

        write(filename,self.sample_rate,self.recording)

        self.recording = None
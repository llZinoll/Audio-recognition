import pyaudio
import wave

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANENELS = 1
FRAME_RATE = 16000

p =  pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANENELS,
    rate=FRAME_RATE,
    input=True,
    frames_per_buffer= FRAMES_PER_BUFFER
)

print("start recording")

seconds = 60
frames = []

for i in range(0, int(FRAME_RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.start_stream()
stream.close()
p.terminate()

obj = wave.open("output.wav", "wb")
obj.setnchannels(CHANENELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(FRAME_RATE)
obj.writeframes(b"".join(frames))
obj.close
import wave

#audio signal parameters
#Number od chanel (Mono or stereo)
#Number of bits sample width
#Sample rate: 44,100Hz(This normal in songs)
#Number of framas
#value of a frame

#Load wav
obj = wave.open("It_Could_Have_Been_Me.wav", "rb")

print("Number of chanels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("All parameters", obj.getparams())

#Duration of the audio
time_audio = obj.getnframes() / obj.getframerate()

print("Time length:",time_audio / 60)

#Frames of the audio
frames = obj.readframes(-1)

print(type(frames), type(frames[0]))
print(len(frames)/2)

#Once done close
obj.close()

#New object
obj_new = wave.open("It_Could_Have_Been_Me_new.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(44100)

obj_new.writeframes(frames)

obj_new.close()
import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Recording started....")
frames = []

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)
except KeyboardInterrupt:
    pass  # Stop recording on Ctrl+c

print("Recording stopped....")

stream.stop_stream()
stream.close()
audio.terminate()

output_filename = "recorded_audio.wav"

with wave.open(output_filename, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Audio saved as {output_filename}")

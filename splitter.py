from pydub import AudioSegment

sound = AudioSegment.from_wav("./sound/transcribed.wav")

# halfway_point = len(sound) / 2
# second_half = sound[halfway_point:]
ten_seconds = 10*1000
first_10_seconds = sound[:ten_seconds]

# halfway_point.export("./sound/harmonSplit1.wav", format="wav")
# second_half.export("./sound/harmonSplit2.wav", format="wav")
first_10_seconds.export("./sound/harmonSplit1testTenSecs.wav", format="wav")


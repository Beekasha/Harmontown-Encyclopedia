from pydub import AudioSegment

sound = AudioSegment.from_wav("./sound/transcribed.wav")

# halfway_point = len(sound) / 2
# second_half = sound[halfway_point:]
thirty_seconds = 30*1000
first_30_seconds = sound[:thirty_seconds]
last_30_seconds = sound[-30000:]



# halfway_point.export("./sound/harmonSplit1.wav", format="wav")
# second_half.export("./sound/harmonSplit2.wav", format="wav")
first_30_seconds.export("./sound/harmonSplit1testTenSecs.wav", format="wav")
last_30_seconds.export("./sound/harmonSplit1testTenSecs2.wav", format="wav")



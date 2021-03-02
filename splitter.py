from pydub import AudioSegment
import math

podcast = AudioSegment.from_wav("../htown/samples/20120704-Achieve Weightlessness (6.16.12).wav")

# halfway_point = len(podcast) / 2
# second_half = podcast[halfway_point:]



def segment_count():
    thirty_seconds = 30*1000
    podcast_length = len(podcast)
    segment_count = math.ceil(podcast_length / thirty_seconds)
    print(segment_count)
    first_30_seconds = podcast[:thirty_seconds]
    last_30_seconds = podcast[-30000:]

segment_count()

# halfway_point.export("./sound/harmonSplit1.wav", format="wav")
# second_half.export("./sound/harmonSplit2.wav", format="wav")

# # correctly exports
# first_30_seconds.export("./sound/harmonSplit1testFirst30.wav", format="wav")
# last_30_seconds.export("./sound/harmonSplit1testLast30.wav", format="wav")



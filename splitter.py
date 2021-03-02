from pydub import AudioSegment
import math

podcast = AudioSegment.from_wav("../htown/samples/20120704-Achieve Weightlessness (6.16.12).wav")

# halfway_point = len(podcast) / 2
# second_half = podcast[halfway_point:]



def segment_count(podcast):
    thirty_seconds = 30*1000

    podcast_length = len(podcast)
    segment_count = math.ceil(podcast_length / thirty_seconds)
    leftovers = (segment_count-(podcast_length / thirty_seconds))*1000
    
    return [segment_count, leftovers]



def chop_audio(podcast):
    thirty_seconds = 30*1000
    lengths = segment_count(podcast)

    for x in range(0,lengths[0]-1):
        print("this is segment " + str(x))
        startTime = x*thirty_seconds
        extract = podcast[startTime:(startTime+thirty_seconds)]
        print(extract)
        extract.export( "./testDump/harmoning"+str(x)+".wav", format="wav")

    # startTimeLastChunk = (lengths[0]-1)*thirty_seconds
    # endTimeLastChunk = 




# segment_count(podcast)
chop_audio(podcast)


# halfway_point.export("./sound/harmonSplit1.wav", format="wav")
# second_half.export("./sound/harmonSplit2.wav", format="wav")

# # correctly exports
# first_30_seconds.export("./sound/harmonSplit1testFirst30.wav", format="wav")
# last_30_seconds.export("./sound/harmonSplit1testLast30.wav", format="wav")



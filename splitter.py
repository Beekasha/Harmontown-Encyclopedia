from pydub import AudioSegment
import math

from dotenv import load_dotenv
load_dotenv()

import os

pathname="../htown/samples/20120704-Achieve Weightlessness (6.16.12).wav"
podcast = AudioSegment.from_wav(pathname)


# creates all directories for new audio
def create_all_directories():
    # directory of all the original MP3 files
    directory = os.environ.get("directory-of-original-audio")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".mp3"): 
            path = os.path.join(directory, filename)
            print(path)
            # create_new_directory(path)
      





# Returns date of episode from pathname
def get_podcast_date(pathname):
    split = pathname.split("-")
    date = split[0].split("/")[-1]
    return date


# Creates new directory titled with the date
def create_new_directory(pathname):
    date = get_podcast_date(pathname)

    # protects against same date
    try:
        os.mkdir(f'./sound/split-audio/{date}')
    except OSError as error:
        print(error)
        # appends a '2' to the file if the date already exists (aka Denver and KC)
        os.mkdir(f'./sound/split-audio/{date}2')


# Counts how many 15sec. segments we need to slice the audio into
def segment_count(podcast):
    fifteen_seconds = 15*1000

    podcast_length = len(podcast)
    segment_count = math.ceil(podcast_length / fifteen_seconds)
    
    return segment_count





# Chops up the audio into multiple smaller files
def chop_audio(podcast):
    fifteen_seconds = 15*1000
    length = segment_count(podcast)

    for x in range(1,length-1):
        print("this is segment " + str(x))
        startTime = x*fifteen_seconds
        extract = podcast[startTime:(startTime+fifteen_seconds)]
        print(extract)
        extract.export( "./testDump/harmoning"+str(x)+".wav", format="wav")

    startTimeLastChunk = (length-1)*fifteen_seconds
    endTimeLastChunk = len(podcast)
    lastChunk = podcast[startTimeLastChunk:endTimeLastChunk]
    lastChunk.export( "./testDump/harmoning"+str(length-1)+".wav", format="wav")


create_all_directories()



# # Splits Files
# chop_audio(podcast)


# halfway_point.export("./sound/harmonSplit1.wav", format="wav")
# second_half.export("./sound/harmonSplit2.wav", format="wav")

# # correctly exports
# first_30_seconds.export("./sound/harmonSplit1testFirst30.wav", format="wav")
# last_30_seconds.export("./sound/harmonSplit1testLast30.wav", format="wav")



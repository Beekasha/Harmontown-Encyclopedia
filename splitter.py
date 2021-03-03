from pydub import AudioSegment
import math

from dotenv import load_dotenv
load_dotenv()

import os

pathname="../htown/samples/20120704-Achieve Weightlessness (6.16.12).wav"
# podcast = AudioSegment.from_wav(pathname)


# creates all directories for new audio in split-audio
def create_all_directories():
    # directory of all the original MP3 files
    directory = os.environ.get("directory-of-test")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".mp3"): 
            path = os.path.join(directory, filename)
            create_new_directory(path)
      





# Returns date of episode from pathname
def get_podcast_date(pathname):
    split = pathname.split("-")
    date = split[0].split("/")[-1]
    return date



# Creates new directory titled with the date in split-audio directory
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
def chop_wav(pathname):
    podcast = AudioSegment.from_wav(pathname)
    fifteen_seconds = 15*1000
    length = segment_count(podcast)
    date = get_podcast_date(pathname)

    for x in range(1,length-1):
        print("this is segment " + str(x))
        startTime = x*fifteen_seconds
        extract = podcast[startTime:(startTime+fifteen_seconds)]
        extract.export(f'./sound/split-audio/{date}/{date}-{str(x)}.wav', format="wav")
        

    # last chunk will most likely not be 15 seconds in length
    startTimeLastChunk = (length-1)*fifteen_seconds
    endTimeLastChunk = len(podcast)
    lastChunk = podcast[startTimeLastChunk:endTimeLastChunk]
    lastChunk.export( f'./sound/split-audio/{date}/{date}-{str(length-1)}.wav', format="wav")

# # must make folders first
# chop_wav('../htown/S1Test/20121022-Back To The Future Part Kush (10.01.12).wav')
def split_all_wav(directory):
    create_all_directories()
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".wav"): 
            print(filename)
            chop_wav(f'{directory}/{filename}')

      
split_all_wav(os.environ.get("directory-of-test"))
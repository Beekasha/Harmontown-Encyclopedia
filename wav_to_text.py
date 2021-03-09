import speech_recognition as sr

from dotenv import load_dotenv
load_dotenv()

import os
from pydub import AudioSegment

import json

# # this works
# r = sr.Recognizer()

# harvard = sr.AudioFile('./sound/harmonSplit1testFirst30.wav')
# with harvard as source:
#     audio = r.record(source)
#     trans = r.recognize_google(audio)
#     print(trans)






def transcribe_wav(audio_path):
    r = sr.Recognizer()

    harvard = sr.AudioFile(audio_path)
    with harvard as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        trans = r.recognize_google(audio, language='en-US', show_all=True)
        print(trans)
        return(trans)

# transcribe_wav('./sound/split-audio/20120830/20120830-106.wav')

# Empty?
# transcribe_wav('./sound/split-audio/20120830/20120830-107.wav')


# def transcribe_all(pathname):
#     #Change working directory
#     os.chdir(pathname)
#     audio_files = os.listdir()

#     print(f'We have {len(audio_files)} files to convert')
#     for file in audio_files:
#         #spliting the file into the name and the extension
#         name, ext = os.path.splitext(file)
        
#         if ext == ".mp3":
#             mp3_sound = AudioSegment.from_mp3(file)
#             print(f'printing {name}')
#             #rename them using the old name + ".wav"
#             mp3_sound.export("{0}.wav".format(name), format="wav")






# THIS NEEDS EP ID NUMS
def response_to_json(response, episode_id, sequence, title):
    transcription = response['alternative'][0]['transcript']
    confidence = response['alternative'][0]['confidence']
    data = {}
    data['episodes'] = []
    data['episodes'].append({
        'episode-id': episode_id,
        'transcription': transcription,
        'confidence': confidence,
        'title': title,
        'sequence': sequence
    })

    print(data)


    # TEST RESPONSE 
    # {'alternative': [{'transcript': 'is in this room', 'confidence': 0.75383753}, {'transcript': 'is it in this room'}, {'transcript': 'as in this room'}, {'transcript': 'in this room'}, {'transcript': "he's in this room"}], 'final': True}

# response_to_json({'alternative': [{'transcript': 'is in this room', 'confidence': 0.75383753}, {'transcript': 'is it in this room'}, {'transcript': 'as in this room'}, {'transcript': 'in this room'}, {'transcript': "he's in this room"}], 'final': True})
# {
#     "title": "Harmontown",
#     "episodes": [
#         {
#             "episode-id": "$$$2010292",
#             "location-in-seq": "$$$CU",
#             "transcription": "$$$transcription"
#             "confidence": "$$$confidence"
#         }
#         # {episode object}
#         # {episode object}
#         # {episode object}
#     ]
# }







# # Runs transcription for all files in directory
# for filename in os.listdir('./testDump'):
    
#     if filename.endswith(".wav"):
#         print("this is " + filename)
#         transcribe('./testDump/' + filename)










# # convert mp3 file to wav                                                       
# sound = AudioSegment.from_mp3("./sound/harmonTest.mp3")
# sound.export("./sound/transcribed.wav", format="wav")

# # Tis works too
# # transcribe audio file                                                         
# AUDIO_FILE = "transcriptHAR.wav"

# # use the audio file as the audio source                                        
# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#         audio = r.record(source)  # read the entire audio file                  

#         print("Transcription: " + r.recognize_google(audio))

def transcribe_all(split_directory):
    for subdir, dirs, files in os.walk(split_directory):
        for file in files:
            name, ext = os.path.splitext(file)
            # for all WAV in directory
            if ext == ".wav":
                # ./sound/split-audio/20120816-Confessions Of An Alcoholic Mars Rover (8.7.12)/20120816-59.wav
                filedir = os.path.join(subdir, file)
                # 20120816-59.wav
                filename = (os.path.join(subdir, file)).split("/")[-1]
                print("Working on:")
                print("Filename:")
                print(filename)
                print("Filedir")
                print(filedir)
                # Call to actually make the transcription
                response = transcribe_wav(filedir)

                print("Response:")
                print(response)

                # transcription = response['alternative'][0]['transcript']
                print('\n')
                # response_to_json(response,)
                ep_id = filename.split("-")[0]
                seq = filename.split("-")[1].split(".")[0]
                title = filedir.split("/")[-2]
                # want to now take this response and pass it off to make json
                response_to_json(response, ep_id, seq, title)
transcribe_all(os.environ.get("split-audio-directory"))
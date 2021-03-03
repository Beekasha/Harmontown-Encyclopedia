from dotenv import load_dotenv
load_dotenv()

import os
from pydub import AudioSegment



def mp3_to_wav(pathname):
    #Change working directory
    os.chdir(pathname)
    audio_files = os.listdir()

    print(f'We have {len(audio_files)} files to convert')
    for file in audio_files:
        #spliting the file into the name and the extension
        name, ext = os.path.splitext(file)
        
        if ext == ".mp3":
            mp3_sound = AudioSegment.from_mp3(file)
            print(f'printing {name}')
            #rename them using the old name + ".wav"
            mp3_sound.export("{0}.wav".format(name), format="wav")

# mp3_to_wav(path)
mp3_to_wav(os.environ.get("directory-of-mp3-test"))
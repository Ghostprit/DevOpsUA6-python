from os import listdir
from moviepy import *


def mp4ToMp3(inputFilePath, outputFilePath):
    converted = AudioFileClip(inputFilePath)
    converted.write_audiofile(outputFilePath)
    converted.close()

if __name__ == "__main__":
    for file in listdir('.'):
        if file.endswith(".mp4"):
            mp4ToMp3(file, file.replace(".mp4", ".mp3"))
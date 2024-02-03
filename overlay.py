import os
from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate_videoclips , clips_array, vfx, AudioFileClip, ImageClip 
from moviepy.video.fx import resize

timesRan = 0
clipIndex = 0

backgroundClip = input("What Video File Clip for Background? ")
directoryName = input("What directory name? ")

parent_dir = "C:\\Open Source\\Tiktok Clip Editing"

clipFolder = "C:\\Open Source\\Tiktok Clip Editing\\clips"

folderPath = os.path.join(parent_dir,directoryName)

os.makedirs(folderPath, exist_ok= True)

clipList = os.listdir(clipFolder)

clipCount = len(clipList)

def videoGen(list, minecraftClip, timesRan, folderPath, directoryName, clipFolder, clipIndex, listLength):
    while timesRan < listLength:

        clipFilePath = os.path.join(clipFolder, list[clipIndex])
        overlayClip = VideoFileClip(clipFilePath)

        bgClip = VideoFileClip(minecraftClip)

        overlayResize = overlayClip.resize(width=800, height=519)
        overlayFinal = overlayResize.set_position("top")

        clipDuration = (int(overlayClip.duration))
        overlayFinal = overlayFinal.margin(top=100, opacity=0)

        clips = CompositeVideoClip([bgClip, overlayFinal]) \
        .set_duration(clipDuration) \

        outputFilePath = os.path.join(folderPath, f'{directoryName}{timesRan}.mp4')

        clips.write_videofile(outputFilePath, audio_codec='aac')
    
        timesRan = timesRan + 1
        clipIndex = clipIndex + 1


    
    print("Complete!")


videoGen(clipList, backgroundClip, timesRan, folderPath, directoryName, clipFolder, clipIndex, clipCount)

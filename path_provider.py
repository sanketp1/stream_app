import os 
from dataclasses import dataclass
from pathlib import Path
import uuid

ROOT_DIR = os.getcwd()

@dataclass
class MediaPath:
    RECORDED_SESSION_MEDIA = "sessions"
    ANALYSIS_MEDIA = "analysis"
    FEEDBACK_MEDIA = "feedbacks"
    PROFILES_MEDIA = 'profiles'

# checking is session directory is exist or not 
# if it's not exist then create initially
if(not os.path.isdir(os.path.join(os.getcwd(), MediaPath.RECORDED_SESSION_MEDIA))):
    os.mkdir(MediaPath.RECORDED_SESSION_MEDIA)

if(not os.path.isdir(os.path.join(os.getcwd(), MediaPath.ANALYSIS_MEDIA))):
    os.mkdir(MediaPath.ANALYSIS_MEDIA)

if(not os.path.isdir(os.path.join(os.getcwd(), MediaPath.FEEDBACK_MEDIA))):
    os.mkdir(MediaPath.FEEDBACK_MEDIA)

if(not os.path.isdir(os.path.join(os.getcwd(), MediaPath.PROFILES_MEDIA))):
    os.mkdir(MediaPath.PROFILES_MEDIA)


def get_media_path(path_name:str):
    return os.path.join(os.getcwd(), path_name)



path = 'C:\\Users\\sanketpatil\\Videos\\courses\\Python\\code\\practice\\stream_app\\sessions\\03d4af13-3a99-4a52-8753-7aca588d449d\Exercise 2_ Adding Custom Color Theme to TextUtils _ Complete React Course in Hindi _14(720P_HD).mp4'

x = path.split("\\")
print(x)
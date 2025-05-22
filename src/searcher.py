from time import sleep
from mutagen import File
import regex
import os

bms_id_regex = r"BeatmapSetID:\s*?(\d+)"
osu_regex = r"{free}:\s*?(.+)"

def first(pat,st):
    content = regex.findall(pat,st)
    return False if len(content) == 0 else content[0]

def find_name(what,content):
    res = first(osu_regex.replace("{free}",what),content)
    if not res:
        return None
    return res.strip()

class OsuSearcher():
    def __init__(self,osu_folder,id_cache=None,folder_cache=None):
        self.queue = []
        self.songs = os.path.join(osu_folder,"Songs")
        
        if os.path.isdir(self.songs):
            self.queue = os.listdir(self.songs)
        else:
            raise Exception("That isn't an osu folder, buddy!")
        
        self.id_cache = id_cache or {}
        self.folder_cache = folder_cache or {}
    
    def step(self):
        song = self.queue.pop()
        if song in self.folder_cache.keys():
            return
        path = os.path.join(self.songs,song)
        files = os.listdir(path)
        bms_id = None
        audio_path = None
        
        for i in files:
            osu_file = os.path.join(path,i)
            if osu_file.endswith(".osu"):
                #print(osu_file)
                with open(osu_file,"r") as f:
                    content = f.read()
                
                bms_id = first(bms_id_regex,content)
                if bms_id in self.id_cache.keys():
                    return
                audio_path = find_name("AudioFilename",content)
                
                title = find_name("Title",content)
                artist = find_name("Artist",content)
                tags = find_name("Tags",content)
                if bms_id and audio_path and title and artist:
                    break
        if not audio_path:
            return
        real_path = os.path.join(song,audio_path)
        if real_path:
            actual = os.path.join(path,audio_path)
            if not os.path.isfile(actual):
                return False
            seconds = 0
        
            audio = File(actual)
            if audio and audio.info:
                seconds = audio.info.length
            self.id_cache[bms_id] = {
                "audio": real_path,
                "title": title,
                "artist": artist,
                "tags": tags,
                "length": round(seconds)
            }
            self.folder_cache[song] = bms_id
            
            return bms_id

        return False
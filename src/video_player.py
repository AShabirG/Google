"""A video player class."""

from .video_library import VideoLibrary
global Playing
import random
Playing="No"
Pause = False
class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        #print(len(self._video_library.get_all_videos()))
        #for i in self._video_library.get_all_videos():
         #   print(self._video_library.get_video(i))
        first=[]
        second=[]
        third=[]
        infile=open(r"C:\google-code-sample-main\python\src\videos.txt","r")
        while True:
            lines = infile.readline()
            splitter=lines.split("|")
            first.append(splitter)
            print(str(splitter[0])+ "("+str(str(splitter[1]).split())+")")
            print(splitter[1])
            print(splitter[2])
            #second.append(splitter[1])
            #third.append(splitter[2])
            if not lines:
                break
        first.sort()
        print(first)
        
        #p=lines.sort()
        #print(p)

        #print(f.read())
        #print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.
        
        Args:
            video_id: The video_id to be played.
        """
        global Playing
        global Pause
        infile=open(r"C:\google-code-sample-main\python\src\videos.txt","r")
        line_number = 0
        test=False
        
        with open(r"C:\google-code-sample-main\python\src\videos.txt", 'r') as read_obj:
        
            for line in read_obj:
            
                line_number += 1
                if video_id in line:
                
                    for i, line in enumerate(infile):
                        if i == line_number-1:
                            splitter=line.split("|")
                            
                            Playing=splitter[0]
                            print("Playing video: ", Playing)
                            Pause= False
                            test=True
                    break
        if test==False:
            print("Cannot play video: Video does not exist")
        
        

    def stop_video(self):
        global Playing
        """Stops the current video."""
        if Playing != "No":
            print("Stopping video: ",Playing)
            Playing="No"
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        global Playing
        global Pause
        if Playing != "No":
            print("Stopping video: ", Playing)
            Pause = False
            n = random.randint(0,4)
            infile=open(r"C:\google-code-sample-main\python\src\videos.txt","r")
            for position, line in enumerate(infile):
                if position == n:
                    splitter=line.split("|")
                    print("Playing video: ", splitter[0])
                    Playing = splitter[0]
        else:
            n = random.randint(0,4)
            infile=open(r"C:\google-code-sample-main\python\src\videos.txt","r")
            for position, line in enumerate(infile):
                if position == n:
                    splitter=line.split("|")
                    print("Playing video: ", splitter[0])
                    Playing = splitter[0]

    def pause_video(self):
        """Pauses the current video."""
        global Playing
        global Pause
        if Playing != "No":
            if Pause == False:
                Pause = True
                print ("Pausing video: ", Playing)
            elif Pause == True:
                print("Video already paused: ", Playing)
        elif Playing == "No":
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        global Playing
        global Pause
        if Pause == True :
            Pause = False
            print("Continuing video: ", Playing)
        elif Pause == False and Playing != "No":
            print("Cannot continue video: Video is not paused")
        elif Pause == False and Playing == "No":
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        global Playing
        global Pause
        infile=open(r"C:\google-code-sample-main\python\src\videos.txt","r")
        line_number=0
        if Playing == "No":
            print("No video is currently playing")
        elif Playing != "No":
            with open(r"C:\google-code-sample-main\python\src\videos.txt", 'r') as read_obj:
        
                for line in read_obj:
                    line_number += 1
                    if Playing in line:
                        
                        for i, line in enumerate(infile):
                           
                            if i == line_number-1:
                                
                                splitter=line.split("|")
                               
                                print(str(splitter[1]).strip())
                                
                        
                                if Pause==False:
                                    print("Currently playing: "+ str(splitter[0]) + "("+ str(str(splitter[1]).split())+ ") ["+ str(str(splitter[2]).split())+ "]")
                                elif Pause== True:
                                    print("Currently playing: "+ str(splitter[0]).split() + "("+ str(splitter[1]).split() + ") ["+ str(splitter[2]).split()+ "] - PAUSED")
                              
            
        

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

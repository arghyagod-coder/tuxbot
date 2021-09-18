from youtube_search import YoutubeSearch 
import requests, urllib, re
def yturl(song):
    music_name = song
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    results = YoutubeSearch(clip2, max_results=1).to_dict()
    res = results[0]
    title = res["title"]
    turl = res["thumbnails"][0]
    return clip2, title, turl



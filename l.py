from lyrics_extractor import SongLyrics


sc = SongLyrics('AIzaSyCBc9vGiM-q0dIOpt0mSIdhraUGiF1pU_U', '2c0e4a26e5d598f41')
js = sc.get_lyrics(
    'Bella ciao'
)
print(js["lyrics"])
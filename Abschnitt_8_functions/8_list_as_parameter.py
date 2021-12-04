playlist = [
    {"band" : "Queen", "name" : "Another one bites the dust"},
    {"band" : "Aerosmith", "name" : "Crazy"},
    {"band" : "Ozzy Osbourne", "name" : "Crazy train"},
    {"band" : "Queen", "name" : "We will rock you"}
]

def get_track_by_band(band_name, track_list): # funktionsparamter tracklist = argument aus programm = playlist
    tracks_found = [] # liste zum Speichern der Loop-Ergebnisse
    for track in track_list:
        if track["band"] == band_name: # wenn parameter "band" in tracklist (also playlist) = argument aus programm
            tracks_found.append(track) # füge das list->dict der Sammelliste tracks_found hinzu
    return tracks_found # gebe tracks_found ans Programm zurück

search_result = get_track_by_band("Queen", playlist) # gibt argumente in die Funktion und speichert ergebnis in var (zwecks Weiterverwendung, hier: print)
print(search_result)


from sulley import *

s_initialize("m3u")

#header
s_static("#EXTM3U\r\n")
s_static("#EXTINF:191,Artist Name - Track Title\r\n")

#sample url resource; https://www.lifewire.com/Sample.mp3
s_static("https://")
s_string("www")
s_delim(".")
s_string("lifewire")
s_delim(".")
s_string("com")
s_delim("/")
s_string("Sample")
s_delim(".")
s_static("mp3")

#Generating Fuzz samples
i=1
while s_mutate():
	fuzz_file = open("Playlist\mutant-" +str(i) + ".m3u", "w")
	fuzz_file.write(s_render())
	fuzz_file.close
	i=i+1
print '[+] Done fuzzing'
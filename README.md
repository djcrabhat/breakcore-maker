# How it works i guess????
this takes a snippet of a wav file and turns it into breakcore.

recommended file size seems to be 3 seconds of music.


`python3 main.py inputfile.wav outputfile.wav`
The input and output args are optional and default to some files on djcrabhat's computer.


## Other useful tools/commands
convert mp3 to wav
`ffmpeg  -i YOUR_SAMPLE.mp3 YOUR_SAMPLE.wav`

`ffmpeg -ss 60 -i YOUR_SAMPLE.wav -t 3 -c copy YOUR_SAMPLE_OUTPUT.wav`
Skip 60 seconds into the track and extract 3 seconds of audio

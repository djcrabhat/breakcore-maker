import random
import wave
import sys
import os


class Sample:
    def __init__(self, path):
        self.path = path

    def chunk(self, slices=16):
        with wave.open(self.path) as w:
            self.channels = w.getnchannels()
            self.width = w.getsampwidth()
            self.rate = w.getframerate()
            frames = w.getnframes()
            chunk_size = int(frames / slices)
            chops = []
            for x in range(slices):
                chops.append(w.readframes(chunk_size))
            return chops

    def write_chunks(self, slices=16, name_format="output_{}.wav"):
        chunks = self.chunk(slices=slices)
        i = 0
        for c in chunks:
            with wave.open(name_format.format(i), "w") as w:
                w.setnchannels(s.channels)
                w.setsampwidth(s.width)
                w.setframerate(s.rate)
                w.writeframes(c)
            i += 1

    def fuck_it_up(self, slices=16, total_chunks=32, name_format="fuck_it_up.wav"):
        chunks = self.chunk(slices=slices)
        with wave.open("output/" + name_format, "w") as w:
            w.setnchannels(s.channels)
            w.setsampwidth(s.width)
            w.setframerate(s.rate)

            for i in range(total_chunks):
                index = random.randint(0, len(chunks) - 1)
                w.writeframes(chunks[index])


if __name__ == "__main__":
    inputFile = sys.argv[1] if len(
        sys.argv) >= 2 else "cw_amen01_175.wav"

    outputFile = sys.argv[2] if len(sys.argv) >= 3 else "fuck_it_up_6.wav"
    s = Sample(inputFile)

    outputFolder = "output"
    if not os.path.isdir(outputFolder):
        os.makedirs(outputFolder)

    # s.write_chunks()

    # s.fuck_it_up(slices=32,total_chunks=64, name_format="fuck_it_up_3.wav")
    s.fuck_it_up(slices=16, total_chunks=128, name_format=outputFile)
    print(f"written to {outputFile}")

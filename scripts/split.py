import pysrt

BASE_DIR = "./subs/en/"

# load full en sub
subs = pysrt.open(BASE_DIR + "full.en.srt", encoding="utf-8")

# split into multiple subs, each containing 1,000 lines
for i in range(0, len(subs), 1000):
    chunk = subs[i : i + 1000]
    chunk.save(BASE_DIR + "%02d.en.srt" % (i / 1000), encoding="utf-8")

print("Done!")

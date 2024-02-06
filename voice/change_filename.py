import os
import glob

for filename in glob.glob("*.wav"):
    new_filename = f"small_{filename}"
    os.rename(filename, new_filename)
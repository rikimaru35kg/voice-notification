import os
import sys
import glob

print("DO YOU REALLY WANT TO EXECUTE THIS SCRIPT?")
ans = input().lower()
if (ans not in ['y', 'yes']): sys.exit()

for filename in glob.glob("*.wav"):
    new_filename = f"small_{filename}"
    os.rename(filename, new_filename)
print("Done!")

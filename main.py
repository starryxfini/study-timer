import time

print("⋆｡study timer°✩")

minutes = int(input("how many minutes do you want to study?"))

seconds = minutes * 60

while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60
    print(f"time left: {mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)
    seconds -= 1

print("\n  ˖.𖥔 ݁ time is up˖ ⊹good job! ࣪ ˖ ")
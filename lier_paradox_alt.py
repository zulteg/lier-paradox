import time

start_time = int(time.time())

default_moment = 5
now_moment = input(f"Длительность момента \"сейчас\" в секундах ({default_moment}с):")
now_moment = int(now_moment) if now_moment else default_moment

phrase = "\"Мой нос сейчас вырастет\""

prev_action = int(input("\nЧто Буратино сказал ранее?\n0: ложь\n1: правда\n"))

print("")

if prev_action == 0:
    print("(ранее Буратино соврал)")
else:
    print("(ранее Буратино сказал правду)")
print(f"Буратино говорит {phrase}")

delta_time = int(time.time()) - start_time
if delta_time <= now_moment:
    now_moment_left = False
    print("(момент \"сейчас\" еще существует)")
else:
    now_moment_left = True
    print("(момент \"сейчас\" прошел)")

print("")

if not now_moment_left:
    if prev_action == 0:
        print(f"Нос Буратино вырастет, так как ранее он сказал ложь, "
              f"а последующая фраза {phrase} стала истинной")
    else:
        print(f"Нос Буратино вырастет, от того что фраза {phrase} "
              f"является ложью, так как ранее он сказал правду")
else:
    if prev_action == 0:
        print(f"Нос Буратино вырастет дважды, так как ранее он соврал "
              f"и фраза {phrase} в новом \"сейчас\" является ложной")
    else:
        print(f"Нос Буратино вырастет, от того что фраза {phrase} "
              f"является ложью в новом моменте \"сейчас\"")


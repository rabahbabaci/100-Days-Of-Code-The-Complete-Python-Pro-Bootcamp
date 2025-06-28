import random

head_tail = ["Head", "Tail"]
random.shuffle(head_tail)

if head_tail[0] == "Head":
    print("Head is chosen!!!")
else:
    print("Tail is chosen!!!")
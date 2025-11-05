print("hello, i am minecraft. What is your name? : ")
name = input()
print(f"Nice to meet you, {name}!")
print("how are u feeling today? (good/bad) : ")
mood = input().lower
if mood == "good":
    print("i am glad to hear that!")
elif mood == "bad":
    print("i am sorry to hear that. Hope things briten up soon")
else:
    print("i see. Sometimes it i shard to put feeling into words")

print(f"it was nice chatting with u {name}. goodbye")
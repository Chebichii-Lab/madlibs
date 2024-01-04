# # using string concatenation (putting strings together)
# # how do you put strings together?
# # supposed you wan to create a string that says "subscribe to________"
# youtuber = "nat king cole" #some string

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber)) # puts the value of youtuber inside where the curly braces are.
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)
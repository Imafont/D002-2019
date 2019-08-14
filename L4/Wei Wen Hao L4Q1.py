#1
collection = ["Pikachu", "Bulbasaur", "Squirtle", "Nidoqueen"]
newly_caught = ["Bulbasaur", "Kakuna", "Arbok", "Jigglypuff"]
for i in newly_caught:
    if i not in collection:
        collection.append(i)
print(collection)

#2
hsi = [20000, 21000, 21500, 22125, 21015, 22013, 19942, 24500]
change = []
for i in range(0, int(len(hsi)-1)):
    change.append(hsi[i+1] - hsi[i])
print(change)

#3
channels = ["TVB", "CCTV", "VIU", "RTHK", "Netflix", "TBS", "KBS"]
current_channel = 0
while True:
    print("You are now watching %s" % channels[current_channel])
    a = input("Please choose either Up/Down/Off\n")
    if a == 'U':
        current_channel = current_channel + 1
        current_channel = current_channel%7
    if a == 'D':
        current_channel = current_channel - 1
        current_channel = current_channel%7
    if a == 'o':
        print("Shutting down...")
        break

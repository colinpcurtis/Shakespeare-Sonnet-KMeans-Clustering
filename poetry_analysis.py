with open("shakespere_sonnett.txt") as file:
    new_file = open("sonnett", "w")
    for line in file:
        line = line.strip()
        if len(line) > 15:
            new_file.write(line)
            new_file.write("\n")
    new_file.close()

file = open("sonnett", "r")
data = file.read().replace("?", "").replace(",", "").replace("!", "").replace("'", "e").replace(":", "") \
    .replace(";", "").replace("-", "").replace(".", "")
file.close()

file = open("sonnett", "r")
new_data = []
for line in file:
    new_data.append(line.strip().split())
file.close()


def create_poems():  # each poem is 14 lines, so we just have to take each 14 line chunk and add it to a list
    poems = []
    for i in range(0, len(new_data), 14):
        if i < len(new_data) - 13:
            poems.append(new_data[i] + new_data[i + 1] + new_data[i + 2] + new_data[i + 3] + new_data[i + 4] +
                         new_data[i + 5] + new_data[i + 6] + new_data[i + 7] + new_data[i + 8] + new_data[i + 9] +
                         new_data[i + 10] + new_data[i + 11] + new_data[i + 12] + new_data[i + 13])
    return poems


poems = create_poems()

new = []
with open ("funktiosanat.txt","r") as f:
    for line in f:
        stripped = line.strip("\n")
        new.append(stripped)

new.sort() #sorts by letter
with open ("3ex.txt","w") as file:
    for k in new:
        file.write(k + "\n")
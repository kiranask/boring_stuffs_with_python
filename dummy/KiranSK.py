with open("1556280001_dna.cpcode.account.info.csv", "r") as file:
    lines = set()
    for line in file:
        lines.add(frozenset(line.strip("\n").split(",")))

with open("1556280001_dna.cpcode.account.info.csv", "w") as file:
    for line in lines:
        file.write(",".join(line)+"\n")


print("Done")
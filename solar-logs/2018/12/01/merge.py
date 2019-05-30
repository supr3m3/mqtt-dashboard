import json
import glob


result = []
for f in glob.glob("*.json"):
    with open(f, "r") as infile:
        for line in infile:
            result.append(line)

with open("merged_data.json", "w") as output:
    json.dump(result, output)

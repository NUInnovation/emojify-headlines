with open("../emojis.json", "r") as rf:
  with open("../emojis_no_underscores.json", "w") as wf:
    for line in rf:
      wf.write(line.replace("_", " "))
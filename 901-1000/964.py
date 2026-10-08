lines = open("INPUT.TXT").read().split("\n")
n = int(lines[0])
sites_by_word = {}
results = []
for i in range(1, n + 1):
    line = lines[i].strip()
    first = line.index('"')
    second = line.index('"', first + 1)
    word = line[first + 1:second]
    command = line.split()[0]
    sites = sites_by_word.setdefault(word, set())
    if command == "Search":
        found = sorted(sites)
        out = ["Results: %d site(s) found" % len(found)]
        for k, site in enumerate(found[:10]):
            out.append("%d) %s" % (k + 1, site))
        results.append("\n".join(out))
    else:
        site = line[second + 1:].split()[1]
        if command == "Add":
            if site in sites:
                results.append("Already exists")
            else:
                sites.add(site)
                results.append("OK")
        else:
            if site in sites:
                sites.remove(site)
                results.append("OK")
            else:
                results.append("Not found")
open("OUTPUT.TXT", "w").write("\n=====\n".join(results) + "\n")

lines = open("INPUT.TXT").read().split("\n")
name = lines[0].split()[1]
times = []
for line in lines[1:5]:
    if "Time=" in line:
        times.append(int(line.split("Time=")[1].split()[0]))
received = len(times)
lost = 4 - received
out = [
    "Ping statistics for %s:" % name,
    "Packets: Sent = 4 Received = %d Lost = %d (%d%% loss)" % (received, lost, lost * 25),
]
if received:
    average = (2 * sum(times) + received) // (2 * received)
    out.append("Approximate round trip times:")
    out.append("Minimum = %d Maximum = %d Average = %d" % (min(times), max(times), average))
open("OUTPUT.TXT", "w").write("\n".join(out) + "\n")

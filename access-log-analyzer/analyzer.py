rawlog = []
ips = {}
urls = {}
# schema = {"ip": [" - - "], "date": {"day": ["/"], "month": ["/"], "year": [":"], "time": [":", ":", " "]},
#           "httpmethod": ["\"", " "], "url": [" "], "statuscode": [" ", " "], "domain": [" \""] "useragent": ["\"", "\""]}
logfilename = "access1.log"

def out_title(title):
    print(title + "\n" + "-"*len(title))

def get_most_common(data, limit=-1):
    # limit being -1 means no limit
    most = 0
    common = {}
    for num in data.values():
        most = num if num > most and (limit == -1 or num < limit) else most
    for x, num in data.items():
        if num != most:
            continue
        if not(num in common):
            common[num] = [x]
        else:
            common[num].append(x)
    return common

def output_most_common(data, title="MOST COMMON", text="visits"):
    out_title(title)
    for num, things in data.items():
        out = ""
        for thing in things:
            out += thing + ", "
        # get rid of the last seperator
        out = out[:-2]
        print(out, "with", num, text)



# get the log's contents
with open(logfilename) as logfile:
    lines = logfile.readlines()
    for i in range(0, len(lines)):
        # remove \n at end of each line
        lines[i] = lines[i][:-1]
    rawlog = lines

# get ips
for line in rawlog:
    ip = line[0:line.index(" - - ")]
    if ip in ips:
        ips[ip] += 1
    else:
        ips[ip] = 1

# get urls
for line in rawlog:
    url = line[line.index("\""):]
    url = url[1:]
    url = url[:url.index("\"")]
    url = url[url.index(" "):]
    url = url[1:]
    url = url[:url.index(" ")]
    if url in urls:
        urls[url] += 1
    else:
        urls[url] = 1
clone = urls.copy()
for url, visits in urls.items():
    # remove "duplicate" urls, e.g. "/home/" and "/home", sum visits
    for check, num in urls.items():
        if len(check) == 1:
            continue
        if url[:-1] == check and url in clone:
            clone[check] += visits
            clone.pop(url)
        elif check[:-1] == url and check in clone:
            clone[url] += num
            clone.pop(check)
urls = clone
    

# print out the 5 most common ip(s)
common = get_most_common(ips)
for i in range(0, 5):
    common.update(get_most_common(ips, list(common.keys())[i]))
output_most_common(common, "MOST COMMON IP ADDRESSES", "hits")
print("\n")

# print out the most commonly visited url
visited = get_most_common(urls)
for i in range(0, 5):
    visited.update(get_most_common(urls, list(visited.keys())[i]))
output_most_common(visited, "MOST COMMONLY VISITED URLS")
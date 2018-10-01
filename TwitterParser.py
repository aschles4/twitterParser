twitterData = []
users = 10


def sort(hash):
    return sorted(hash.items(), key=lambda kv: kv[1], reverse=True)[:users]


file = open('twitter.txt', 'r', encoding="utf-8")
for line in file:
    # print(line.replace("\n", "").split(" "))
    twitterData.append(line.replace("\n", "").split(" "))

# 0 = username
# 1 = timestamp
# len - 2 = followers
# len - 1 = retweet count

# Get the most twitted the entire time line
twitted = {}

for data in twitterData:
    if data[0] in twitted:
        count = twitted.get(data[0])
        twitted[data[0]] = count + 1
    else:
        twitted[data[0]] = 1
print("")
print("Top ", users, " who twitted the most")
for k, v in sort(twitted):
    print(k, v)

# The top 10 users who have tweeted the most for every hour.
hours = {}
for data in twitterData:
    # get the military time of the post and seperate it off of that
    d = data[1].split(":")[1]
    if d in hours:
        hash = hours[d]
        if data[0] in hash:
            count = hash.get(data[0])
            hash[data[0]] = count + 1
        else:
            hash[data[0]] = 1
    else:
        hours[d] = {}
        hash = hours[d]
        hash[data[0]] = 1
print("")
print("Top ", users, " who twitted the most per hour")
for hour in hours.keys():
    print("")
    print("Hour:", hour)
    for k, v in sort(hours.get(hour)):
        print(k, v)

# The top 10 users who have the maximum followers.
twitterFollowers = {}

for data in twitterData:
    twitterFollowers[str(data[0])] = int(data[len(data) - 2])
print("")
print("Top ", users, " with the most followers")
for k, v in sort(twitterFollowers):
    print(k, v)

# The top 10 tweets which have the maximum retweet count.
twitterRetweets = {}

for data in twitterData:
    twitterRetweets[data[0]] = int(data[len(data)-1])

print("")
print("Top ", users, " with the most retweets")
for k, v in sort(twitterRetweets):
    print(k, v)
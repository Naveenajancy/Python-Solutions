def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    reverseSortredShirtSpeeds =sorted(redShirtSpeeds, reverse=True)
    sortblueShirtSpeeds = sorted(blueShirtSpeeds)
    #print(reverseSortredShirtSpeeds, sortblueShirtSpeeds)
    teamList = list(zip(reverseSortredShirtSpeeds, sortblueShirtSpeeds))
    #team = (list(teamList))
    print(f"teamPair {teamList}")
    return sum(list(map(lambda x:max(x),teamList))) if fastest == True else sum(list(map(lambda x:min(x), teamList)))

print(tandemBicycle([1,2,3,9,12,3], [3,3,4,6,1,2], fastest=True))
#print(tandemBicycle([3,6,7,2,1], [5,5,3,9,2], fastest=False))
print(tandemBicycle([5,5,3,9,2], [3,6,7,2,1], fastest=True))
# Sets do not have order and don't contain duplicate elements
art_friends = {"Rolf", "Anne"}
science_freinds = {"Jen", "Charli"}

art_friends.add("Jen")
print(art_friends)

art_friends.add("Jen")
print(art_friends)

art_friends.remove("Jen")
print(art_friends)

## Why friends are useful
art_friends = {"Rolf", "Anne", "Jen"}
science_freinds = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_freinds) 
science_but_not_art = science_freinds.difference(art_friends)

print(art_but_not_science) #{'Anne', 'Rolf'}
print(science_but_not_art) # {'Charlie'}

not_in_both = art_friends.symmetric_difference(science_freinds)
print(not_in_both) #{'Anne', 'Charlie', 'Rolf'}

art_and_science = art_friends.intersection(science_freinds)
print(art_and_science) #{'Jen'}

all_friends = art_friends.union(science_freinds)
print(all_friends) #{'Anne', 'Rolf', 'Jen', 'Charlie'}

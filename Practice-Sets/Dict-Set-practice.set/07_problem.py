#if the names of 2 friends are the same, 
# what will happen to the program ??


friends = {}

friends["Saniya"] = "Python"
friends["Ali"] = "C++"

#Duplicate key is not allowed 
# Same name entered again

friends["Saniya"] = "Java"

print(friends)


#Explanation :
#Actually, dictionary does NOT allow duplicate keys, but it DOES allow duplicate values. 
#will update the first key value into second key value
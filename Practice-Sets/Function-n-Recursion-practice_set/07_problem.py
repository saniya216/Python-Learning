def remove_word(lst , word):
    for item in lst[:]:
        if word == item.strip():            #spaces remove
            lst.remove(item)                     

names = ["ALI" , "SANI" , "AMAN" , "SANI"]
remove_word(names , "SANI")

print(names)
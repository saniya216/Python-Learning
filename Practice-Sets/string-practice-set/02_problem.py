
#To fill in a letter template given below with name and date.

letter = '''
Dear <|Name|>, 
        You are Selected !
<|Date|>
         '''

print(letter.replace("<|Name|>","Sania").replace("<|Date|>","25 September 2025"))
my_binary_file = open("binaryinput.txt") #opens file
whole_binarytemp = my_binary_file.read() #reads file into a string
wholeindex = whole_binarytemp.index(".") + 1 
whole_binary = whole_binarytemp[wholeindex:len(whole_binarytemp)]
print(whole_binary)


databaseopen = open("database_1.txt")
database_str = databaseopen.read()
data_base = {"\n":"011100", "-":"1011011" #reads in data base
}
#print(database_str)
temp_data_base = database_str.split("\n") #converts to list of sets
for i in range(0,len(temp_data_base)): #converts list to binary
    index = temp_data_base[i].index("-")
    character = temp_data_base[i][0:index]
    end = len(temp_data_base[i])
    binarytemp = temp_data_base[i]
    binary = binarytemp[index +1:end]
    data_base.update({character:binary})

reverse_data_base = {"011100": "\n", "1011011":"-"
}

for i in data_base:
    reverse_data_base.update({data_base[i]:i}) #reverses database set

#print(reverse_data_base)
fixes = {
}
#print(data_base)
for i in data_base:
    if (len(i) > 1) and (i != "/n"):
        fixes.update({i:data_base[i]}) #seperates fixes set
for i in fixes:
    data_base.pop(i) 

#print(fixes)
reverse_fixes = {
}

for i in fixes:
    reverse_fixes.update({fixes[i]:i}) #reverses fixes set for debinarizing
#print(reverse_fixes)


def debinarize(tstring:str) -> str:
    result = ""
    index = 0 #counter
    while index < len(tstring):
        if tstring[index] == "1": #checks for long
            if tstring[index+1] == "1":  #accounts for prefixes and common terms
                result += reverse_fixes[tstring[index:index +7]]#recalls data from data set
            else:
                result += reverse_data_base[tstring[index:index+7]]  #determine corresponding long and appends
            index += 7 #adjusts counter
        if tstring[index] == "0": #checks for short
            result += reverse_data_base[tstring[index:index+6]] #determine corresponding short and appends
            index += 6 #adjusts counter
    return result 


bi = open("textoutput.txt", "w")
bi.write(debinarize(whole_binary))
bi.close()
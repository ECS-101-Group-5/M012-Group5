my_file = open("textinput.txt") #opens file
whole_str = my_file.read() #reads file into a string
whole_length = len(whole_str) #takes length of string
whole_list = []
for i in range(0,whole_length):
    whole_list.append(whole_str[i]) #converts to list

databaseopen = open("database_1.txt")
database_str = databaseopen.read()
data_base = {"\n":"011100", "-":"1011011"
}
#print(database_str)
temp_data_base = database_str.split("\n")
for i in range(0,len(temp_data_base)):
    index = temp_data_base[i].index("-")
    character = temp_data_base[i][0:index]
    end = len(temp_data_base[i])
    binarytemp = temp_data_base[i]
    binary = binarytemp[index +1:end]
    data_base.update({character:binary})

reverse_data_base = {"011100": "\n", "1011011":"-"
}

for i in data_base:
    reverse_data_base.update({data_base[i]:i})

#print(reverse_data_base)
fixes = {
}
#print(data_base)
for i in data_base:
    if (len(i) > 1) and (i != "/n"):
        fixes.update({i:data_base[i]})
for i in fixes:
    data_base.pop(i)

#print(fixes)
reverse_fixes = {
}

for i in fixes:
    reverse_fixes.update({fixes[i]:i})
#print(reverse_fixes)
def binarize(tlist:list) -> str:
    result = ""
    fix_counter = 0
    i = 0
    while i < len(tlist):
        if i == len(tlist)-4:
           result += data_base[tlist[i]]
           result += data_base[tlist[i+1]]
           result += data_base[tlist[i+2]]
           result += data_base[tlist[i+3]]
           result2 = (str((len(result))) + "." + result)
           return result2
        elif tlist[i] + tlist[i+1] in fixes:
            result += fixes[tlist[i] + tlist[i+1]]
            i += 2
        elif tlist[i] + tlist[i+1] + tlist[i+2] in fixes:
            result += fixes[tlist[i] + tlist[i+1] +tlist[i+2]]
            i += 3
        elif tlist[i] + tlist[i+1] + tlist[i+2] + tlist[i+3] in fixes:
            result += fixes[tlist[i] + tlist[i+1] +tlist[i+2] + tlist[i+3]]
            i += 4
        elif tlist[i] + tlist[i+1] + tlist[i+2] + tlist[i+3] + tlist[i+4] in fixes:
            result += fixes[tlist[i] + tlist[i+1] +tlist[i+2] + tlist[i+3] + tlist[i+4]]
            i += 4
        elif tlist[i] + tlist[i+1] + tlist[i+2] not in fixes:
            result += data_base[str(tlist[i])] #appends it onto result string
            i += 1

#print(whole_str)
#print(whole_list)
#print(binarize(whole_list))

n = open("binaryoutput.txt","w")
n.write(binarize(whole_list))
n.close()


print(binarize(whole_list))
if ((binarize(whole_list))) == whole_str:
    print(True)
else:
    print(False)
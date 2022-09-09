kaupungit_list= []

kaupungit= input("Anna viiden kaupungit nimet:")

while kaupungit!=(""):
    kaupungit_list.append(kaupungit)
    kaupungit= input("Anna viiden kaupungit nimet:")

for n in kaupungit_list:
    print (n)
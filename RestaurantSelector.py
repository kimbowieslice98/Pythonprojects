##Input data and store it to listChoice
Vegetarian = input('Is anyone in your party vegetarian? Type yes or no: ')
Vegan = input('Is anyone in your party vegan? Type yes or no: ')
GF = input('Is anyone in your party gluten-free? Type yes or no: ')
listChoice = [Vegetarian, Vegan, GF]
##listPrint Holds the places
listPrint = ["   Joe's Gourmet Burgers", "   Main Street Pizza company", "   Corner Cafe", "   Mama's Fine Italian", "   The Chef's Kitchen"]
print("Here are the restaurant choices: ")
##Joe's is only place without Vegetarian so it's removed if someone is
if listChoice[0] == 'yes':
    listPrint.remove("   Joe's Gourmet Burgers")
##Mama and Main Street dont offer vegan so they are removed if some is
if listChoice[1] == 'yes':
    ##test to see if item has already been removed
    if "   Joe's Gourmet Burgers" in listPrint:
        listPrint.remove("   Joe's Gourmet Burgers")
    listPrint.remove("   Mama's Fine Italian")
    listPrint.remove("   Main Street Pizza company")
##Joe and Mana dont offer GF so they are removed if someone is
if listChoice[2] == 'yes':
    if "   Joe's Gourmet Burgers" in listPrint:
        listPrint.remove("   Joe's Gourmet Burgers")
    if "   Mama's Fine Italian" in listPrint:
        listPrint.remove("   Mama's Fine Italian")
##print the remaining places
for x in range(len(listPrint)):
    print(listPrint[x])


myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "vastu": "Item"
}
print("Options are ",myDict.keys())
a = input("Enter the hindi word\n")
print("The meaning of hindi word is:", myDict.get(a))
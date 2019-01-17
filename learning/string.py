from difflib import SequenceMatcher

#a = 'Dump Administration Dismisses Surgeon General Vivek Murthy (http)PUGheO7BuT5LUEtHDcgm"
#b = 'Dump Administration Dismisses Surgeon General Vivek Murthy (http)avGqdhRVOO"
a = 'basavaraja'
b = 'basavaraja'
ratio = SequenceMatcher(None, a, b).ratio()
print(ratio)

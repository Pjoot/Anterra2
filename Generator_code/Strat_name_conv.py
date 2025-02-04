# FOR UPDATING STRATEGIC REGION NAMES

import os
import sys

#Doc = 'localisation\\strategic_region_names_l_english.yml'
Output = 'Generator_code\\Output\\'
Source = 'map\\strategicregions\\'

print("The script has started. Please do not touch any files")

List = [filename for filename in os.listdir(Source)]

TXT = "ï»¿l_english: \n"		#needs to have that weird starter to ensure it is a readable file

for region in List:

	ID = region.split("-",1)[0]						#find region ID
	Pre_NAME = region.split("-",1)[1]
	NAME = Pre_NAME.split(".")[0]					#find file name

	#STRATEGICREGION_4:0 "Ireland"
	Entry = f' STRATEGICREGION_{ID}:0 "{NAME}" \n'	#put the ID and name into loc file
	print(Entry)

	TXT += Entry

with open(Output+"strategic_region_names_l_english.yml", 'w') as DOC:
	DOC.write(TXT)									#writes the file
DOC.close()

print("- The script has ended. Thank you for using! -")

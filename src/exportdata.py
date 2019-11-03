# Author: 		Doug Ortiz
# Creation Date:	November 02, 2019
# Project:		InforCodingTest
# Updates:
# ---

# Packages/Modules Utilized
import csv, json
import validations
import pprint

# Variables and Constants

# Convert List to a Dictionary
def convertToDictionary(lst): 
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)} 
    return res_dct 

# Export to Csv File
def exportToCsv(exportList):
   exportedCsv = False;
   try:
      if(validations.validateList(exportList) == True):
         with open('ApiDetails.csv', 'w') as csvFile:
              wr = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
              wr.writerow(exportList)
         csvFile.close()
         exportedCsv = True;
         print("Exported CSV File Successfully!")

   except Exception as e:
      print("Error while attempting to Write to CSV File!")
   return exportedCsv;

def exportToJson(exportList):
   exportedJson = False;
   try:
      if(validations.validateList(exportList) == True):
         exportDict = convertToDictionary(exportList)

         with open('ApiDetails.json', 'w') as jsonFile:
              json.dump(exportDict, jsonFile)
         jsonFile.close()
         exportedJson = True;
         print("Exported JSON File Successfully!")

   except Exception as e:
      print("Error while attempting to Write to Json File!")
   return exportedJson;

def exportToJsonPretty(exportList):
   exportedJsonPretty = False;
   try:
      if(validations.validateList(exportList) == True):
         exportDict = convertToDictionary(exportList)
         parsedJson = json.dumps(exportDict, indent=2, sort_keys=True)

         with open('ApiDetails-Pretty.txt', 'w') as jsonFile:
              json.dump(parsedJson, jsonFile)
         jsonFile.close()
         exportedJsonPretty = True;
         print("Exported JSON Pretty File Successfully!")

   except Exception as e:
      print("Error while attempting to Write to Json Pretty File!")
   return exportedJsonPretty;
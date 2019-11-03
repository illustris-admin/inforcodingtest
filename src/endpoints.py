# Author: 		   Doug Ortiz
# Creation Date:	November 02, 2019
# Project:		   InforCodingTest
# Updates:
# ---

# Packages/Modules Utilized
import validations

# Variables and Constants
endpoints = {("Used for mobile purposes","NoapiKeyRequired", "CORS"):"us-east-1", 
             ("Used for Data Transfers", "apiKeyRequired", "SSL"):"us-west-1",
             ("Used for Web Applications", "apiKeyRequired", "waf"):"us-central-1"} 
  
def getApiDetails(region):
   returnList = []
   try:
      # Traversing dictionary with multi-keys
      for i in endpoints: 
          if(region == endpoints.get(i)):
             returnList.append(endpoints.get(i))
             returnList.append(i[0])
             returnList.append(i[1])
             returnList.append(i[2])
  
   except Exception as e:
      print("Error while retrieving Api Details!")
   return returnList;

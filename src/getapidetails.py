# Author: 		Doug Ortiz
# Creation Date:	November 02, 2019
# Project:		InforCodingTest
# Updates:
# ---

# Packages/Modules Utilized
import validations
import endpoints
import exportdata
import sys

def main():
   # Get User Provided Parameters
   passedArguments = sys.argv[1:]


   # Validate the Arguments Count, credentials and region
   if (validations.validArgumentsCount(len(sys.argv)) and validations.validateCredentials(passedArguments[0]) 
      and validations.validateRegions(passedArguments[1])):
         # Provided valid credential 
         print("Valid Credential: '" + passedArguments[0] + "'")
         # Provided valid region
         print("Valid Region: '" + passedArguments[1] + "'")

         apiDetails = endpoints.getApiDetails(passedArguments[1])
         if(validations.validExportArgument(passedArguments[2])):
            if(passedArguments[2] == 'csv'):
               exportdata.exportToCsv(apiDetails)
            if(passedArguments[2] == 'json'):
               exportdata.exportToJson(apiDetails)
            if(passedArguments[2] == 'json-pretty'):
               exportdata.exportToJsonPretty(apiDetails)

# Check for main definition and make the call
if __name__ == '__main__':
   main()
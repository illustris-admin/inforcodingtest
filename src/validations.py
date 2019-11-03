# Author: 		Doug Ortiz
# Creation Date:	November 02, 2019
# Project:		InforCodingTest
# Updates:
# ---

# Packages Utilized
# 

# Variables and Constants
# Credentials list
credsList = ['admin', 'dev']
# Regions List
regionsList = ['us-west-1', 'us-east-1', 'us-central-1']

# Validates credentials parameter provided 
# against Credentials List
def validateCredentials(username):
   validCredential = True;
   try:
      # Validate Credential Parameter
      if username not in credsList :
         print("Credential: '" + username + "' is not valid!")
         validCredential = False;
  
   except Exception as e:
      print("Provided credential not valid!")
   return validCredential;

# Validates regions provided as a parameter
# against Regions List
def validateRegions(region):
   validRegion = True;
   try:
      # Validate Region Parameter
      if region not in regionsList :
         print("Region : '" + region + "' is not valid!")
         validRegion = False;
  
   except Exception as e:
      print("Provided Region not valid!")
   return validRegion;

# Validates if a List is empty
def validateList(list):
   validList = False;
   try:
      # Validate List Parameter
      if len(list) > 0 :
         validList = True;
  
   except Exception as e:
      print("Provided List not valid!")
   return validList;

# Validates if the number of arguments
# Matches the expected number of arguments
def validArgumentsCount(argsCount):
   validArgumentsCount = False;
   try:
      # Validate Arguments Count
      if argsCount == 4 :
         validArgumentsCount = True;
  
   except Exception as e:
      print("Provided Arguments Count is not valid!")
   return validArgumentsCount;

# Validates Export Arguments
def validExportArgument(exportArgument):
   validExportArg = False;
   try:
      # Validate Export Argument
      if ( exportArgument == "csv" or exportArgument == "json"
         or exportArgument == "json-pretty" ):
            validExportArg = True;
  
   except Exception as e:
      print("Provided Export Argument is not valid!")
   return validExportArg;
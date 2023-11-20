'''
Create a script that reads the access log from a file. 
The name of the file is provided as an argument. An output of the 
script should provide the total number of different User Agents and 
then provide statistics with the number of requests from each of them.
'''

# import argparse
# parser = argparse.ArgumentParser(description="Returns user statistics of provided access logs")
# parser.add_argument("file",  help="Access log text file")
# args = parser.parse_args()

#import regex 
import re 

#Return a dictionary of account id and total amount 
def getFileData(file): 
    with open(file,'r') as f: 
        data=f.read().split('\n') #Read file 
        return data #return data
    
def genClientIP(data): 
    ipDict={} 
    for line in data: 
        #Split using regex 
        match = re.match(r'(\S+) - - \[([^\]]+)\] "([^"]+)" (\d+) (\d+) "([^"]+)" "([^"]+)"', line)
        if match:
            ip_address, timestamp, request, status_code, response_size, referer, user_agent = match.groups()    
            #Check if ip is present in dictionary 
            if ip_address in ipDict:                                # add the new number to the existing slot 
                count=ipDict[ip_address] 
                ipDict[ip_address]=count+1     
            else:                                                   #create a new item in this slot 
                count=1 
                ipDict[ip_address]=count 
        totalusers = len(ipDict)         
    return ipDict , totalusers
      
def genStatusCode(data): 
    statusDict={}  
    for line in data: 
        #Split using regex 
        match = re.match(r'(\S+) - - \[([^\]]+)\] "([^"]+)" (\d+) (\d+) "([^"]+)" "([^"]+)"', line)
        if match:
            ip_address, timestamp, request, status_code, response_size, referer, user_agent = match.groups()
        #Check if status is present in dictionary 
        if request[0] in statusDict: 
            # add the new number to the existing slot 
            count= statusDict[request[0]] 
            statusDict[request[0]]=count+1 
        else: # create a new item in this slot 
            count=1 
            statusDict[request[0]]=count 
    return statusDict 
    
def printReport(IPDict,statusDict): 
    print("-----------------------------------------------------\nStatistics for the Apache log file access_log\n-----------------------------------------------------") 
    print("Frequency of Client IP Addresses:") 
    for ip,v in IPDict.items(): 
        print(ip+"\t\t",end =" ") 
        
        for i in range(0,v): 
            print("*",end="") 
            print() 
            print("\nHTTP Status Codes Summary:") 
            
            totalItems=sum(statusDict.values()) 
            for status,v in statusDict.items(): 
                percent=(v/totalItems)*100 
                format_percent = "{:.2f}".format(percent) 
                print(status,":\t",format_percent,"%") 
                
#Driver code 
data=getFileData("/Users/aalyahjohnson/Desktop/Python3/Task3/access.log.5") 
#print(data)
IPDict=genClientIP(data) 
#print(IPDict)

statusDict=genStatusCode(data) 
print(statusDict)

#printReport(IPDict,statusDict)
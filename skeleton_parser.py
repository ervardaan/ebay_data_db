
"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014

Skeleton parser for CS564 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
#NO TOUCHING ABOVE THIS COMMENT
def parseJson(json_file):
    #MAKING 6 FILES TO BE OPENED AND APPENDED-USE APPENDED OPTION ONLY AS FOR ALL THE INPUT 40 FILES, WE NEED TO OPEN THESE 6 FILES EVERY TIME AND APPEND CONTENTS TO THEM
    itemsfile=open(r"items.dat",'a')
    sellfile=open(r"sell.dat",'a')
    bidderfile=open(r"bidder.dat",'a')
    sellerfile=open(r"seller.dat",'a')
    bidsfile=open(r"bids.dat",'a')
    userfile=open(r"user.dat",'a')
    with open(json_file, 'r') as f:
        userlist=[]
        selllist=[]
        bidderlist=[]
        bidslist=[]
        sellerlist=[]
        catlistline=[]#no need to check if category array is null or not beacuse an item will be of at least one category,thus array length>=1 always
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        for item in items:
            
            """
            TODO: traverse the items dictionary to extract information from the
            given `json_file' and generate the necessary .dat files to generate
            the SQL tables based on your relation design
            """
            #CREATING SEPARATE TUPLES FOR SECURING LINES FOR EACH OF THE 6 FILES
            itemsline=""
            sellline=""
            bidderline=""
            sellerline=""
            bidsline2=""
            userline=""
            userline2=""
            #structure of items relation in same order-
            #itemid,name,buyprice,currently,firstbid,numberofbids,description,started,ends,category  
            #strucrture of sell-itemid,userid(of seller),category
            if( 'ItemID' in item.keys() and item["ItemID"]!=None):      
                itemid=int(item["ItemID"]) 
                sellline+=str(itemid)+"|"
                itemsline+=str(itemid)+"|"#it is an integer actually
                bidsline2+=str(itemid)+"|"
            else:
                continue#if itemid is only not there then no need to do anything else
            if( 'Name' in item.keys() and item["Name"]!=None): 
                name=item["Name"]
                name=name.replace("\"","\"\"")#in every string which can contain a quotation, we have to escape it with another quote
                itemsline+="\""+name+"\""+"|"
            else:
                itemsline+="null"+"|"
            if( 'Buy_Price' in item.keys() and item["Buy_Price"]!=None):
                buyprice=item["Buy_Price"]#this is not required to be there
                itemsline+="\""+transformDollar(buyprice)+"\""+"|"
            else:
                itemsline+="null"+"|"
            if( 'Currently' in item.keys() and item["Currently"]!=None): 
                #NO NEED TO TAKE CARE OF THE FACT THAT CURRENTLY ATTRIBUTE=FIRST_BID WHEN THERE ARE NO BIDS-THIS FACT IS BEING TAKEN BY WRITERS OF JSON FILE SUCH THAT 
                #WHEN THEY GIVE NUMBEROFBIDS=0, THEY GIVE SAME VALUES(NOT NULL) TO BOTH FIRSTBID AND CURRENTLY ATTRIBUTES
                currently=item["Currently"]
                currently=transformDollar(currently)
                itemsline+="\""+currently+"\""+"|"
            else:
                itemsline+="null"+"|"
            if( 'First_Bid' in item.keys() and item["First_Bid"]!=None): 
                firstbid=item["First_Bid"]
                firstbid=transformDollar(firstbid)
                itemsline+="\""+firstbid+"\""+"|"
            else:
                itemsline+="null"+"|"
            if( 'Number_of_Bids' in item.keys() and item["Number_of_Bids"]!=None): 
                numberofbids=int(item["Number_of_Bids"])
                itemsline+=str(numberofbids)+"|"#actually an integer
            else:
                itemsline+="null"+"|"
            if('Description' in item.keys() and item["Description"]!=None ):
                description=item["Description"]
                description=description.replace("\"","\"\"")#again escape quotes
                itemsline+="\""+description+"\"|"
            else:
                itemsline+="null|"
            if( 'Started' in item.keys() and item["Started"]!=None): 
                started=item["Started"]#TODO
                started=transformDttm(started)
                itemsline+="\""+started+"\"|"
            else:
                itemsline+="null|"
            if( 'Ends' in item.keys() and item["Ends"]!=None): 
                ends=item["Ends"]#TODO
                ends=transformDttm(ends)
                itemsline+="\""+ends+"\""#not adding | at end of ends
            else:
                itemsline+="null"
            category=None
            if( 'Category' in item.keys() and item["Category"]!=None): 
                category=item["Category"]
                for cat in category:
                    catlistline.append(itemsline+"|"+"\""+cat+"\"")#this contains all the tuples going into the items relation
            else:
                #if no category, then no tuple as category should be not null-so don't add anything to catlistline array as a tuple to be inserted into items relation
                continue#if there is no category of an ite then it is not a valid item-so don't do anything else-don't put anything in catlistline array as well
            #user-userid,rating,location,country
            #seller-userid,location,country
            #bidder-userid,rating
            #every value from these text files will only give us bidders and users-not sellers(we have to populate sellers later on)-but still keep track of their userid
            #so that we populate sellers after populating users and then we can check which users want to be sellers
            if( 'Seller' in item.keys() and item["Seller"]!=None): 
                seller=item["Seller"]#TODO
                if( 'UserID' in seller.keys() and seller["UserID"]!=None): 
                    sellerid=seller["UserID"]
                    userline+="\""+sellerid+"\""+"|"
                    sellerline+="\""+sellerid+"\""+"|"
                    sellline+="\""+sellerid+"\""#not adding | after this because we do it in next line for each categ element
                    for  categ in category:#only make tuples for the sell relation if a seller is associated with the item
                        selllist.append(sellline+"|\""+categ+"\"")
                    if( 'Rating' in seller.keys() and seller["Rating"]!=None): 
                        rating2=seller["Rating"]#should be an integer value
                        userline+=(rating2)+"|"
                        #sellerline+=(rating2)+"|"#only 2 attributes we get for seller from these json files-seller table doesn't contain rating column
                    else:
                        userline+="null"+"|"
                        #sellerline+="null"+"|"
                    if( 'Location' in item.keys() and item["Location"]!=None): 
                        locationseller=item["Location"]
                        locationseller=locationseller.replace("\"","\"\"")#escaping quotes
                        userline+="\""+locationseller+"\"|"
                        sellerline+="\""+locationseller+"\"|"
                    else:
                        userline+="null|"
                        sellerline+="null|"
                    if( 'Country' in item.keys() and item["Country"]!=None): 
                        country=item["Country"]
                        country=country.replace("\"","\"\"")#escaping quotes
                        userline+="\""+country+"\""
                        sellerline+="\""+country+"\""
                    else:
                        userline+="null"
                        sellerline+="null"
                    userlist.append(userline)
                    sellerlist.append(sellerline)
            
                
            
            bids=item["Bids"]#TODO
            #there may be no bids so check for null value of bid array
            listofbids=[]
            if(bids!=None):
                #get each bid made by one bidder
                for onebid in bids:
                    onebid=onebid['Bid']
                    bidder=onebid["Bidder"]
                    userline2=""#make a new userline for every bidder
                    bidderline=""
                    bidsline=bidsline2
                    userid=bidder["UserID"]
                    userline2="\""+userid+"\""+"|"
                    bidderline+="\""+userid+"\""+"|"
                    if('Rating' in bidder.keys() and bidder["Rating"]!=None ):
                        rating=bidder["Rating"]#actually an integer
                        userline2+=rating+"|"
                        bidderline+=rating+""
                    else:
                        bidderline+="null"
                        userline2+="null|"
                    location=None
                    countrybidder=None
                    if('Location' in bidder.keys() and bidder["Location"]!=None ):
                        location=bidder["Location"]
                        location=location.replace("\"","\"\"")#escaping quotes
                        userline2+="\""+location+"\"|"
                    else:
                        userline2+="null|"
                    if('Country' in bidder.keys() and bidder["Country"]!=None ):
                        countrybidder=bidder["Country"]
                        countrybidder=countrybidder.replace("\"","\"\"")#escaping quotes
                        userline2+="\""+countrybidder+"\""
                    else:
                        userline2+="null"
                    userlist.append(userline2)
                    bidderlist.append(bidderline)
                    #NOW CREATE BID RELATION
                   
                    
                    #format of a bid-itemid,time,amount,userid of bidder,category
                    time=onebid["Time"]
                    time=transformDttm(time)
                    amount=onebid["Amount"]
                    amount=transformDollar(amount)
                    bidsline+="\""+time+"\"|"
                    bidsline+="\""+amount+"\"|"
                    bidsline+="\""+userid+"\""#Not adding | after this because it will be added by category
                    for catgry in category:
                        bidslist.append(bidsline+"|\""+catgry+"\"")
                    

            
            
            
        
                      
            pass

        print("no of users enteries is {}".format(len(userlist)))
        print("no of seller enteries is {}".format(len(sellerlist)))
        print("number of bidders enteries is {}".format(len(bidderlist)))
        print("number of items enteries is {}".format(len(catlistline)))
        print("no of bids enteries is {}".format(len(bidslist)))
        print("no of selling enteries is {}".format(len(selllist)))
        #WRITING TO FIRST FILE-ITEMS RELATION'S DAT FILE
        for line in catlistline:
            itemsfile.write(line+"\n")
        for line2 in userlist:
            userfile.write(line2+"\n")
        for line3 in sellerlist:
            sellerfile.write(line3+"\n")
        for line4 in bidderlist:
            bidderfile.write(line4+"\n")
        for line5 in selllist:
            sellfile.write(line5+"\n")
        for line6 in bidslist:
            bidsfile.write(line6+"\n")
        itemsfile.close()
        sellerfile.close()
        bidsfile.close()
        userfile.close()
        sellfile.close()
        bidderfile.close()

"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print ('Usage: python skeleton_json_parser.py <path to json files>', file=sys.stderr)
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print ("Success parsing ", f)

if __name__ == '__main__':
    main(sys.argv)

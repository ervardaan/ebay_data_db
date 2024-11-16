#!/bin/bash
make clean
make createDATfiles
#sort sell.dat | uniq -D
# this command shows the duplicating groups-this will show all 11 items one after the other(sorted by each of the 4 groups)
#awk '{ if (seen[$0]++) { count++; } } END { print count }' sell.dat
#this command shows number of repeating/duplicating GROUPS(if 4 groups have 11 items repeating as 3,4,2,2 duplicates then answer wil be 4)
awk -i inplace '!seen[$0]++' sell.dat
#this command deletes the duplicate tuples/lins from the files
#sort items.dat | uniq -D
#awk '{ if (seen[$0]++) { count++; } } END { print count }' items.dat
awk -i inplace '!seen[$0]++' items.dat
#sort user.dat | uniq -D
#awk '{ if (seen[$0]++) { count++; } } END { print count }' user.dat
awk -i inplace '!seen[$0]++' user.dat
#sort seller.dat | uniq -D
#awk '{ if (seen[$0]++) { count++; } } END { print count }' seller.dat
awk -i inplace '!seen[$0]++' seller.dat
#sort bids.dat | uniq -D
#awk '{ if (seen[$0]++) { count++; } } END { print count }' bids.dat
awk -i inplace '!seen[$0]++' bids.dat
#sort bidder.dat | uniq -D
#awk '{ if (seen[$0]++) { count++; } } END { print count }' bidder.dat
awk -i inplace '!seen[$0]++' bidder.dat
make makeAdatabase
make loadData
make run7queries


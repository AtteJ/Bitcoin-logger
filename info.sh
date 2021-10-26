#!/bin/zsh

# defines colors
BLUE='\033[1;34m'
CYAN='\033[1;36m'
RED='\033[0;31m'
GREEN='\033[1;32m'
NC='\033[0m'

# displays how many lines csv has
echo
echo -n "${CYAN}number of lines in csv: ${NC}"
wc -l < /media/pi/tikku/data/bitcoin.csv

# displays file size in bytes, KB or MB
echo -n "${CYAN}Csv file size: ${NC}"
FILESIZE=$(stat -c%s "/media/pi/tikku/data/bitcoin.csv")
if [ "$FILESIZE" -lt 1000 ]
then
    echo -e "${FILESIZE}"
elif [ "$FILESIZE" -lt 1000000 ]
then
    inkb=$(echo "scale=1; $FILESIZE/1000"|bc)
    echo -e "${inkb} KB"
else
    inmb=$(echo "scale=1; $FILESIZE/1000000"|bc)
    echo -e "${inmb} MB"
fi

# displays 3 last lines from csv
echo
tail -n 3 /media/pi/tikku/data/bitcoin.csv|tr ',' '|'|tr ' ' '|'
echo

# displays cpu temperature
echo -n -e  "${GREEN}CPU temperature: ${NC}"
cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "$((cpu/1000)) ${GREEN}C${NC}"
echo "---------------------------------------"

# calculates bitcoins value using last line from csv
IFS=, read -r time price < <(tail -n1 /media/pi/tikku/data/bitcoin.csv)
AMOUNT=0.0122492
price=${price%$'\r'}
value=$(echo "scale=2; $price*$AMOUNT/1"|bc)
echo -e "${BLUE}Bitcoin price is ${RED}$price${BLUE} €"
echo -e "You have ${RED}$AMOUNT${BLUE} bitcoins"
echo -e "Your bitcoins value is ${RED}$value${BLUE} €${NC}"

# price day ago
IFS=, read -r time price_day_ago < <(tail -n 144 /media/pi/tikku/data/bitcoin.csv|head -n 1)
price_day_ago=${price_day_ago%$'\r'}

#calculate price change in 24h
echo
if (( $(echo "$price > $price_day_ago"|bc -l) ))
then
    change_up=$(echo "scale=5; ((${price}-${price_day_ago})/${price_day_ago})*100"|bc -l)
    echo -e "${BLUE}24h change +${GREEN}$change_up${BLUE}%${NC}"
else
    change_down=$(echo "scale=5; ((${price_day_ago}-${price})/${price_day_ago})*100"|bc -l)
    echo -e "${BLUE}24h change -${RED}$change_down${BLUE}%"
fi
echo -e "${BLUE}Price yesterday: ${GREEN}${price_day_ago}${BLUE} €${NC}"
echo -e "${BLUE}Price now:       ${GREEN}${price}${BLUE} €${NC}"
echo

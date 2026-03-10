#!/bin/bash
echo "welcome to subdomain-finder by yusef-mohey"
echo "tel : +966539797419"
echo 'usage: {./main.sh domain.com }'

if [ -z "$1" ]
then
    echo "usage: chmod +x main.sh ; ./main.sh domain.com"
    exit
fi

echo "checking domain..."

ping -c 1 "$1" > /dev/null 2> errors.txt

if grep -q "$1" errors.txt
then
    echo "domain not valid"
    > errors.txt
    exit
fi

echo "searching for subdomains..."

for sub in $(cat subdomains.txt)
do
    newdomain="$sub.$1"

    ping -c 1 "$newdomain" > /dev/null 2>errwhilepining.txt

    if [ ! -s errwhilepining.txt ]
    then
        echo "domain found: $newdomain"
    fi
done

echo "scan finished"

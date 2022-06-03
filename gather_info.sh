#! /bin/bash

line="---------------------------------------------------------"
echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free ; echo $line

echo "WHO"; who ; echo $line

echo "HOST"
if grep "127.0.0.1" /etc/hosts; then
    echo "Everything OK"
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi
echo $line

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
    sleep $n
    ((n=n+1))
    echo "Retry #$n"
done; echo $line

for file in *.HTM; do
    name=$(basename "$file" .HTM)
    echo mv "$file" "$name.html"
done

echo "Finishing at: $(date)"

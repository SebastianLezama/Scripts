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

echo "Finishing at: $(date)"
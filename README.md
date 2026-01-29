# Flask bruteforcer demo
## THIS IS NOT INTENDED FOR MALICIOUS PURPOSES, FOR EDUCATIONAL PURPOSES ONLY
A simple python program which uses requests and random-user-agent to continuously bruteforce a flask login page which is ran on the localhost, this is purely a cybersecurity project and made for educational and learning purposes only.


## Why I made this?
I made this to demonstrate how easily weak and common passwords can be bruteforced when there is no rate limiting or throttling in a login page and no logging of suspicious activity, this is intended only to be used against your own flask endpoint.

## What the script does
The script reads a list of common passwords from wordlist.txt, and uses them to send HTTP POST requests to a local flask login page, it counts the amount of combos attempted and breaks when the correct username and password is found. It also uses rotating user agents to simulate varying clients.


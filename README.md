# My choice of team at Illumio

# Installation
1. Run `pip3 install pandas` and `pip3 install ipaddress`

# Usage
Run `python3 other_tests.py input.csv` to run my created test file with the given input csv file. In order to change the tests, use the structure from the test files in a python program and the structure from the csv files (the exact same column names as `input.csv` are integral to pandas functionality). The first argument when run from terminal should be the input csv file.

# Design Notes
I used pandas to parse through the csv file, and created a dict that acted as a database and stored each row of the csv file. For example, "outbound" in the dict stores two dicts inside of it, "tcp" and "udp". Inside of each of those are their respective port ranges, and inside each of those are the respective IP ranges.

The difficulty in this question stemmed from the fact that the csv file could contain ranges. I chose to store the start and end of the range (no matter if it the specific input was an individual number or a range), because that allowed me to check if the provided values in accept_packet were inside the range in O(1) time. I also considered parsing the range and storing each value in the range inside of the dict. This would increase both the time and space complexity of initialization and accept_packet by O(n) where n is the length of the range.

# Bottlenecks
The bottleneck of this program is that for each run of accept_packet, the program loops through every port with the given direction/protocol and will also loop through every subsequent IP address at that specific port(s). This gives the program a time complexity of O(n) where n is the amount of rows in the csv file. In a larger csv file, that time per accept_packet call will increase linearly per the number of rows.
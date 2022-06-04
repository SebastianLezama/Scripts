# Parse log file with regex into a dictionary
# Sort dict according to specs
# Write to a file in csv format
# Move file to different directory
# call csv_to_html.py with bash passing name_of_csv and name_of_html file to generate

import re
import os
import csv

"""
Extract ranking of errors report, from most common to least.
User statistics report by username.
Use two scripts, but automate it.
"""


log_data = [
    "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)\n",
    "Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)\n",
    "Dec 18 8:45:40 ubuntu.local ticky: INFO: Created ticket [#7546] (slezama)\n",
    "Jul 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)\n",
    "Dec 18 11:45:40 ubuntu.local ticky: INFO: Created ticket [#8764] (slezama)\n",
    "Jul 1 11:06:48 ubuntu.local ticky: ERROR: Network problem (slezama)\n",
    "Aug 9 11:45:40 ubuntu.local ticky: INFO: Created ticket [#8864] (slezama)\n",
    "Feb 1 11:06:48 ubuntu.local ticky: ERROR: Network problem (slezama)\n",
    "Aug 9 17:45:40 ubuntu.local ticky: INFO: Created ticket [#8798] (rbm)\n",
    "Feb 13 11:06:48 ubuntu.local ticky: ERROR: Network problem (rbm)\n",
]

log_name = 'coursera_log.txt'
os.chdir('Documents\\Scripts')

def writeLog(name) -> None:
    with open(name, 'w') as file:
        for log in log_data:
            file.write(log)
    return

def parseInfoLog(file) -> None:
    info_log = {}
    with open(file) as f:
        for line in f:
            # Parsing info by username
            if "INFO" not in line:
                continue
            info_pattern = r"^([A-Z][a-z]* \d{,2} \d*:\d{2}:\d{2}).*\w*(INFO): ([A-Z][a-z].*\w*)\[#(\d*)\] \((\w*)\)"
            search_result = re.search(info_pattern, line)
            username = search_result[5]
            info_log[username] = info_log.get(username, 0) + 1
        return info_log

def parseErrorLog(file) -> None:
    error_log = {}
    with open(file) as f:
        for line in f:
            # Parsing errors
            if "ERROR" not in line:
                continue
            error_pattern = r"^([A-Z][a-z]* \d{,2} \d*:\d{2}:\d{2}).*\w*(ERROR): "#([A-Z][a-z].*\w*)]\[#(\d*)\]"
            search_errors = re.search(error_pattern, line)
            print(search_errors)
            print(search_errors[1])
            print(search_errors[2])
            print(search_errors[3])


            error = search_errors[2]
            error_log[error] = search_errors[1, 3]
    for i in sorted(error_log):
        pass

def makeCsv(file, name) -> None:
    with open(f"{name}.csv", 'w', newline='') as f:
        columns = ['Username', 'Entries']
        writer = csv.DictWriter(f, fieldnames=file.keys())
        writer.writeheader()
        writer.writerow(file)

def main():
    writeLog(log_name)
    parseErrorLog(log_name)
    makeCsv(sorted_info_log, 'sorted_info_log')
    makeCsv(sorted_error_log, 'sorted_error_log')

sorted_info_log = parseInfoLog(log_name)
sorted_error_log = {}

if __name__ == '__main__':
    main()

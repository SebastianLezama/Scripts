# Parse log file with regex into a dictionary YES
# Sort dict according to specs YES
# Write to a file in csv format YES
# Move file to different directory
# call csv_to_html.py with bash passing name_of_csv and name_of_html file to generate

import re
import os
import csv
from collections import Counter
import pandas as pd

log_data = [
    "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)\n",
    "Jun 1 17:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)\n",
    "Dec 18 8:45:40 ubuntu.local ticky: INFO: Created ticket [#7546] (slezama)\n",
    "Jul 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)\n",
    "Jul 1 8:06:48 ubuntu.local ticky: ERROR: Network problem (slezama)\n",
    "Aug 9 11:45:40 ubuntu.local ticky: INFO: Created ticket [#8864] (slezama)\n",
    "Feb 1 11:06:48 ubuntu.local ticky: ERROR: Network problem (slezama)\n",
    "Aug 9 17:45:40 ubuntu.local ticky: INFO: Created ticket [#8798] (rbm)\n",
    "Feb 13 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (rbm)\n",
    "Nov 27 11:03:03 ubuntu.local ticky: INFO: Created ticket [#1333] (rbm)\n",

]

log_file = 'coursera_log.txt'
os.chdir('Documents\\Scripts')


def writeLog(name) -> None: # Writes the log text into a .txt
    with open(name, 'w') as file:
        for log in log_data:
            file.write(log)
    return

"""
Extract ranking of errors report, from most common to least. YES
User statistics report by username. YES. Stating how many info or error msgs they listed.
Use two scripts, but automate it.
"""

def parseLog(file, name) -> None: # Parses log file into a detailed CSV file
    info_pattern = r"^([A-Z][a-z]* \d{,2} \d*:\d{2}:\d{2}).*\w*(INFO): ([A-Z][a-z]*.*\w*)\[#(\d*)\] \((\w*)\)"
    error_pattern = r"^([A-Z][a-z]* \d{,2} \d*:\d{2}:\d{2}).*\w*(ERROR): ([A-Z][a-z]*.*\w*) \((\w*)\)"
    big_list = []
    entry_log = []
    new_list = []
    with open(f"{name}.csv", 'w', newline='') as f: # Writing columns to CSV file
        columns = ['User', 'Type', 'Info', 'Ticket number', 'Date']
        writer = csv.writer(f)
        writer.writerow(columns)
        with open(file) as log:
            for line in log:
                # Parsing info and writing to CSV
                if "INFO" not in line:
                    continue
                search_result = re.search(info_pattern, line)
                info = [
                    search_result[5],
                    search_result[2],
                    search_result[3],
                    search_result[4],
                    search_result[1]
                    ]
                big_list.append(info)
                info_count = [
                    search_result[5],
                    search_result[2]
                    ]
                entry_log.append(info_count)
        with open(file) as log:
            for line in log: # Parsing errors and writing to CSV 
                if "ERROR" not in line:
                    continue
                search_errors = re.search(error_pattern, line)
                error = [
                    search_errors[4],
                    search_errors[2],
                    search_errors[3],
                    'No ticket',
                    search_errors[1]
                    ]
                big_list.append(error)
                error_count = [
                    search_errors[4],
                    search_errors[2]
                    ]
                entry_log.append(error_count)
            writer = csv.writer(f)
            entry_log = pd.Series(entry_log).value_counts().reset_index().values.tolist()
            for i in entry_log: # iterate through items to append count and make a new list
                i[0].append(i[1])
                new_list.append(i[0])
                new_list.sort(key=lambda x: x[0])
            with open("entry_log.csv", 'w', newline='') as entry:
                columns = ['User', 'Entry', 'Occurrances']
                error_writer = csv.writer(entry)
                error_writer.writerow(columns)
                for i in new_list:
                    error_writer.writerow(i)
            big_list.sort(key=lambda x: x[0])
            for item in big_list:
                writer.writerow(item)


def parseErrorLog(file, name) -> None: # Parses log file and counts error msgs into a CSV
    error_log = {}
    error_pattern = r"^([A-Z][a-z]* \d{,2} \d*:\d{2}:\d{2}).*\w*(ERROR): ([A-Z][a-z]*.*\w*) "
    with open(f"{name}.csv", 'w', newline='') as f:
        columns = ['Problem', 'Occurrances']
        writer = csv.writer(f)
        writer.writerow(columns)
        with open(file) as f:
            for line in f: # Parsing errors
                if "ERROR" not in line:
                    continue
                search_errors = re.search(error_pattern, line)
                error = search_errors[3]
                error_log[error] = error_log.get(error, 0) + 1
        error_log = dict(sorted(error_log.items(), key=lambda item: item[1], reverse=True))
        for key, value in error_log.items():
            writer.writerow([key, value])


def main() -> None:
    writeLog(log_file)
    parseLog(log_file, 'sorted_info_log')
    parseErrorLog(log_file, 'sorted_error_log')


if __name__ == '__main__':
    main()

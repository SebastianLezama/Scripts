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
User statistics report by username. Stating how many info or error msgs they listed.
Use two scripts, but automate it.
"""


log_data = [
    "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)\n",
    "Jun 1 17:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)\n",
    "Dec 18 8:45:40 ubuntu.local ticky: INFO: Created ticket [#7546] (slezama)\n",
    "Jul 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)\n",
    "Dec 18 11:45:40 ubuntu.local ticky: INFO: Created ticket [#8764] (slezama)\n",
    "Jul 1 8:06:48 ubuntu.local ticky: ERROR: Network problem (slezama)\n",
    "Aug 9 11:45:40 ubuntu.local ticky: INFO: Created ticket [#8864] (slezama)\n",
    "Feb 1 11:06:48 ubuntu.local ticky: ERROR: Network problem (slezama)\n",
    "Aug 9 17:45:40 ubuntu.local ticky: INFO: Created ticket [#8798] (rbm)\n",
    "Feb 13 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (rbm)\n",
]

log_file = 'coursera_log.txt'
os.chdir('Documents\\Scripts')

def writeLog(name) -> None:
    with open(name, 'w') as file:
        for log in log_data:
            file.write(log)
    return

def parseInfoLog(file) -> None:
    info_log = []
    columns = ['date', 'type', 'info', 'ticket number']
    info_pattern = r"^([A-Z][a-z]* \d{,2} \d*:\d{2}:\d{2}).*\w*(INFO): ([A-Z][a-z]*.*\w*)\[#(\d*)\] \((\w*)\)"
    with open(file) as f:
        for line in f:
            # Parsing info by username
            if "INFO" not in line:
                continue
            search_result = re.search(info_pattern, line)
            row = 0
            colum = 0
            sr = 0
            print(search_result[sr + 1])
            for result in range(1, 4):
                print(result)
                print(columns[colum])
                index = columns[colum]
                info_log[result] = search_result[result]
                row += 1


        return info_log



def parseLog(file, name) -> None:
    info_pattern = r"^([A-Z][a-z]* \d{,2} \d*:\d{2}:\d{2}).*\w*(INFO): ([A-Z][a-z]*.*\w*)\[#(\d*)\] \((\w*)\)"
    error_pattern = r"^([A-Z][a-z]* \d{,2} \d*:\d{2}:\d{2}).*\w*(ERROR): ([A-Z][a-z]*.*\w*) \((\w*)\)"
    with open(f"{name}.csv", 'w', newline= '') as f:
        # Writing columns to CSV file
        columns = ['date', 'type', 'info', 'ticket number', 'username']
        writer = csv.writer(f)
        writer.writerow(columns)
        with open(file) as log:
            for line in log:
                # Parsing info and writing to CSV
                if "INFO" not in line:
                    continue
                search_result = re.search(info_pattern, line)
                info = [
                    search_result[1],
                    search_result[2],
                    search_result[3],
                    search_result[4],
                    search_result[5]
                    ]
                writer = csv.writer(f)
                writer.writerow(info)
        with open(file) as log:
            for line in log:
                # Parsing errors and writing to CSV 
                if "ERROR" not in line:
                    continue
                search_errors = re.search(error_pattern, line)
                error = [
                    search_errors[1],
                    search_errors[2],
                    search_errors[3],
                    'No ticket',
                    search_errors[4]
                    ]
                writer = csv.writer(f)
                writer.writerow(error)
        return 

def parseErrorLog(file, name) -> None:
    error_log = {}
    error_pattern = r"^([A-Z][a-z]* \d{,2} \d*:\d{2}:\d{2}).*\w*(ERROR): ([A-Z][a-z]*.*\w*) "
    with open(f"{name}.csv", 'w', newline='') as f:
        columns = ['Problem', 'Occurrances']
        writer = csv.writer(f)
        writer.writerow(columns)
        with open(file) as f:
            for line in f:
                # Parsing errors
                if "ERROR" not in line:
                    continue
                search_errors = re.search(error_pattern, line)
                print(search_errors)
                error = search_errors[3]
                error_log[error] = error_log.get(error, 0) + 1
        sort = dict(sorted(error_log.items(), key=lambda item: item[1], reverse=True))
        for key, value in error_log.items():
            writer.writerow([key, value])

def main() -> None:
    writeLog(log_file)
    parseLog(log_file, 'sorted_info_log')
    parseErrorLog(log_file, 'sorted_error_log')


if __name__ == '__main__':
    main()

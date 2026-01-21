# Copyright (c) 2025 Luukas Kola and Luka Hietala
# License: MIT
import types
import importlib
from datetime import datetime
import csv

def read_data(filename: str) -> (list[str], list[list[str]]):
    """
    Reads the CSV file and returns the rows in a suitable structure.

    :filename: Name of file
    :returns:
        :fields: Column headers in CSV
        :rows: Rows in CSV
    """

    # Column titles
    fields : list [str] = []
    # Row data
    rows : list[list[str]] = []
    
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        fields = next(reader)
        for row in reader:
            rows.append(row)

    return fields, rows

def format_data(rows: list[str]) -> dict[datetime.date, dict[str, float]]:
    """
    Does calculations and formats csv data into dictionary
    
    :rows: List of data produced by read_data
    :returns: Dictionary which maps days to dictionaries, which map Consumption
    and Production into float values.
    """
    results : dict[datetime.date, dict[str, float]] = {}
    for row in rows:
        date : datetime.date = datetime.strptime(row[0], "%Y-%m-%dT%H:%M:%S").date()
        if not date in results:
            results[date] = {}
            results[date]['C1'] = float(row[1]) / 1000
            results[date]['C2'] = float(row[2]) / 1000
            results[date]['C3'] = float(row[3]) / 1000
            results[date]['P1'] = float(row[4]) / 1000
            results[date]['P2'] = float(row[5]) / 1000
            results[date]['P3'] = float(row[6]) / 1000
        else:
            results[date]['C1'] += float(row[1]) / 1000
            results[date]['C2'] += float(row[2]) / 1000
            results[date]['C3'] += float(row[3]) / 1000
            results[date]['P1'] += float(row[4]) / 1000
            results[date]['P2'] += float(row[5]) / 1000
            results[date]['P3'] += float(row[6]) / 1000
    return results

def result_data(titles : list[str], data : dict[datetime.date, dict[str, float]]) -> str:
    """
    Puts formatted data in a pretty little table, and returns it as a string

    :titles: The titles for each column
    :data: Formatted data returned by format_data
    :returns: Table
    """
    result : str = ""
    # Print titles
    header = "\t".join(titles) + "\n"
    result += header
    # Print data
    paivat : list[str] = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
    for day, data in data.items():
        paiva : str = paivat[day.weekday()]
        date_str : str = day.strftime("%d.%m.%Y")
        result += f'{paiva} \t{date_str} {f'\t{data['C1']:.2f}\t{data['C2']:.2f}\t{data['C3']:.2f}\t{data['P1']:.2f}\t{data['P2']:.2f}\t{data['P3']:.2f}'.replace('.',',')}\n'
    return result

def write_summary(result: str) -> None:
    """
    Writes the result to summary.txt
    """
    with open("summary.txt", "w") as f:
        f.write(result)

def main() -> None:
    """
    Main function: reads data, computes daily totals, and prints the report.
    """
    summary : str = ""
    for week in ['week41.csv', 'week42.csv', 'week43.csv']:
        fields, rows = read_data(week)
        # Title
        summary += week.split('.csv')[0].title() + ' electricity consumption and production (kWh, by phase)\n'
        # summary += ''.join([char.upper() if index==0 else char for index, char in enumerate(week.split('.csv')[0])]) + '\n'
        # Convert CSV data into desired format
        formatted_data = format_data(rows)
        # Format formatted data as table
        summary += result_data(fields, formatted_data)
    # Write summary to file
    write_summary(summary)

if __name__ == "__main__":
    main()


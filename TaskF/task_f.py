# Copyright (c) 2026 Luukas Kola
# License: MIT
from datetime import datetime, timedelta

def read_data(filename: str) -> dict[datetime.date, dict[str, float]]:
    """Reads a CSV file and returns the rows in a suitable structure."""
    ...
    data: dict[datetime.date, dict[str, float]] = {}
    with open(filename) as f:
        text: str = f.read()
        for line in text.splitlines()[1:]:
            # Values from csv
            values: list[str] = line.split(';')
            # Date
            date: datetime.date = datetime.strptime(values[0].strip(), '%Y-%m-%dT%H:%M:%S.%f%z').date()
            # Create entry if no date meaning on header
            if date not in data:
                row: dict[str|float] = {}
                # Add row values
                row['con'] = float(values[1].replace(',','.'))
                row['pro'] = float(values[2].replace(',','.'))
                row['tmp'] = float(values[3].replace(',','.'))
                # Add row to data
                data[date] = row
            else:
                data[date]['con'] += float(values[1].replace(',','.'))
                data[date]['pro'] += float(values[2].replace(',','.'))
                data[date]['tmp'] += float(values[3].replace(',','.'))
    # Average out temperatures
    for _,v in data.items():
        v['tmp'] /= 24
    return data

def write_report_to_file(lines: list[str]) -> None:
    """Writes report lines to the file report.txt."""
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write('\n'.join(lines) + '\n')

def show_main_menu(data: dict[datetime.date, dict[str, float]]) -> str:
    """Prints the main menu and returns the user selection as a string."""
    menu : str = '''Choose a report type:
    1) Daily summary for a date range
    2) Monthly summary for one month
    3) Full year 2025 summary
    4) Exit the program'''
    print(menu)
    option : str = str(input(': '))
    # If picked incorrect option
    for o in ['1', '2', '3', '4']:
        if o in option:
            break
    else:
        print('Incorrect input')
        return
    # If actual option
    match option.strip():
        case '1':
            lines: list[str] = create_daily_report(data)
            if lines is None:
                return
            print_report_to_console(lines)
            show_extra_menu(lines, data)
        case '2':
            lines: list[str] = create_monthly_report(data)
            if lines is None:
                return
            print_report_to_console(lines)
            show_extra_menu(lines, data)
        case '3':
            lines: list[str] = create_yearly_report(data)
            if lines is None:
                return
            print_report_to_console(lines)
            show_extra_menu(lines, data)
        case '4':
            exit()

def show_extra_menu(lines: list[str], data: dict[datetime.date, dict[str, float]]) -> None:
    """Prints extra menu after report type is chosen"""
    menu: str = '''What would you like to do next?
    1) Write the report to the file report.txt
    2) Create a new report
    3) Exit'''
    print(menu)

    try:
        selection = int(input(': '))
    except ValueError:
        print("Input must be a number")
        show_extra_menu(lines)

    match selection:
        case 1:
            write_report_to_file(lines)
        case 2:
            show_main_menu(data)
        case 3:
            exit()
        case _:
            print("Select between 1-3!")


def create_daily_report(data: dict[datetime.date, dict[str, float]]) -> list[str]:
    """Builds a daily report for a selected date range."""
    try:
        start: datetime.date = datetime.strptime(input('Enter start date (dd.mm.yyyy)\n: '), "%d.%m.%Y").date()
        end: datetime.date = datetime.strptime(input('Enter end date (dd.mm.yyyy)\n: '), "%d.%m.%Y").date()
        if end < start:
            raise Exception('Start later than end')
    except ValueError as e:
        print(e)
        return

    day: datetime.date = start
    consumption: float = 0
    production: float = 0
    average_t: float = 0
    while True:
        # do stuffed
        consumption += data[day]['con']
        production += data[day]['pro']
        average_t += data[day]['tmp']
        # Iterate day
        day = day + timedelta(days=1)
        if day == end:
            break
    # Average out temperature
    average_t /= (end - start).days
    # Format
    result: list[str] = []
    result.append(f'Range {start.strftime('%d.%m.%Y')}-{end.strftime('%d.%m.%Y')}')
    result.append(f'Total consumption: {consumption:.2f} kWh'.replace('.',','))
    result.append(f'Total production: {production:.2f} kWh'.replace('.',','))
    result.append(f'Average temperature: {average_t:.2f} C˚'.replace('.',','))
    return result

def create_monthly_report(data: dict[datetime.date, dict[str, float]]) -> list[str]:
    """Builds a monthly summary report for a selected month."""
    try:
        month: int = int(input('Enter month number (1-12)\n: '))
        if month < 1 or month > 12: 
            raise ValueError("Select from range 1-12")
    except ValueError as e:
        print(e)
        return

    day: datetime.date = datetime(2025, month, 1).date()
    days: int = 0
    consumption: float = 0
    production: float = 0
    average_t: float = 0
    while True:
        # do stuffed
        consumption += data[day]['con']
        production += data[day]['pro']
        average_t += data[day]['tmp']
        # Iterate day
        days += 1
        day = day + timedelta(days=1)
        # When end month
        if day.month != month:
            break
    # Average out temperature
    average_t /= days
    # Format
    result: list[str] = []
    result.append(f'Month {month} summary')
    result.append(f'Total consumption: {consumption:.2f} kWh'.replace('.',','))
    result.append(f'Total production: {production:.2f} kWh'.replace('.',','))
    result.append(f'Average temperature: {average_t:.2f} C˚'.replace('.',','))
    return result

def create_yearly_report(data: dict[datetime.date, dict[str, float]]) -> list[str]:
    """Builds a full-year summary report."""

    consumption: float = 0
    production: float = 0
    average_t: float = 0
    for _,v in data.items():
        # do stuffed
        consumption += v['con']
        production += v['pro']
        average_t += v['tmp']

    # Average out temperature
    average_t /= 365
    # Format
    result: list[str] = []
    result.append('Year 2025 summary')
    result.append(f'Total consumption: {consumption:.2f} kWh'.replace('.',','))
    result.append(f'Total production: {production:.2f} kWh'.replace('.',','))
    result.append(f'Average temperature: {average_t:.2f} C˚'.replace('.',','))
    return result

def print_report_to_console(lines: list[str]) -> None:
    """Prints report lines to the console."""
    for line in lines:
        print(line)

def main() -> None:
    """Main function: reads data, shows menus, and controls report generation."""
    # Read data first
    data: dict[datetime.date, dict[str, float]] = read_data('2025.csv')
    # Then allow the user to to read the data
    while True:
        show_main_menu(data)

if __name__ == "__main__":
    main()

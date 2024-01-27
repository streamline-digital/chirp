import os
import datetime
import argparse
import re

def generate_todo_file(date):

    year = date.strftime("%Y")
    month = date.strftime("%m")
    day = date.strftime("%d")

    # Create the directories if they don't exist

    os.makedirs(f"{year}/{month}", exist_ok=True)

    filepath = f"{year}/{month}/{day}.md"

    if os.path.isfile(filepath):

        # print(f"{YELLOW}{date.strftime('%Y-%m-%d')}{END}")

        return

    todo_file = open(filepath, "w")

    todo_file.write(f"# {date.strftime('%Y-%m-%d')}, {date.strftime('%A')}")

    todo_file.close()

    print(f"{GREEN}{date.strftime('%Y-%m-%d')} {END}")

    return

def scan_todo_files(start_date, end_date):

    completed_tasks = []
    incomplete_tasks = []

    upcoming_events = []
    past_events = []

    current_date = start_date

    while current_date <= end_date:

        year = current_date.strftime("%Y")
        month = current_date.strftime("%m")
        day = current_date.strftime("%d")

        filepath = f"{year}/{month}/{day}.md"

        if not os.path.isfile(filepath):

            break

        todo_file = open(filepath, "r").readlines()

        for line in todo_file:

            # Tasks

            if "- [x]" in line:

                task = line.replace("- [x]", "").strip()
                completed_tasks.append((current_date.strftime("%Y-%m-%d"), task))

            if "- [ ]" in line \
            or "- []" in line:

                task = line.replace("- [ ]", "").strip()
                incomplete_tasks.append((current_date.strftime("%Y-%m-%d"), task))

            # Events

            if line[0] == "@":

                event_time, event_description = line.strip().split(" ", 1)
                event_time = event_time.strip()[1:]
                event_description = event_description.strip()

                upcoming_events.append((current_date.strftime("%Y-%m-%d"), event_time, event_description))

        current_date += datetime.timedelta(days=1)

    return completed_tasks, incomplete_tasks, upcoming_events, past_events


def display_status(completed_tasks, incomplete_tasks, upcoming_events, past_events):

    # incomplete tasks

    if incomplete_tasks:

        print(f"\n{FUCHSIA}incomplete tasks:{END}\n")

        for task_date, task in incomplete_tasks:

            print(f" - {GREY}{task_date}{END}: {task}")

    else:

        print(f"\n{GREEN}No incomplete tasks{END}\n")

    # completed tasks

    if args.completed_tasks \
    and completed_tasks:

        print(f"\n{GREEN}completed tasks:{END}\n")

        for task_date, task in completed_tasks:

            print(f" - {GREY}{task_date}{END}: {task}")

    # Upcoming Events

    if upcoming_events:

        print(f"\n{FUCHSIA}Upcoming events:{END}\n")

        for event_date, event_time, event_description in upcoming_events:

            print(f" - {GREY}{event_date}{END}\n\n   {YELLOW}{event_time}{END}: {event_description}\n")

    else:

        print(f"\n{GREEN}No events{END}\n")

    # Past events

    if past_events:

        print(f"\n{RED}Upcoming events:{END}\n")

        for event_date, event_time, event_description in past_events:

            print(f" - {GREY}{event_date}{END}@{YELLOW}{event_time}{END}: {event_description}\n")


def parse_time_string(time_string):

    # Define regular expression patterns for each time unit
    # Initialize a dictionary to store the extracted values
    # Iterate over each pattern and extract the corresponding value from the time string

    patterns = {

        'y': r'(\d+)y',
        'w': r'(\d+)w',
        'd': r'(\d+)d',
        'h': r'(\d+)h',
        'm': r'(\d+)m',
        's': r'(\d+)s'

    }

    time_units = {}
    matches = 0

    for unit, pattern in patterns.items():

        match = re.search(pattern, time_string)

        if match:

            value = int(match.group(1))
            time_units[unit] = value

            matches += 1

        else:

            time_units[unit] = 0

    if matches == 0:

        time_units['d'] = time_string # default to days when an integer is passed

    return time_units

## Colored and styled terminal output

BLACK = '\033[38;5;0m'
MAROON = '\033[38;5;1m'
GREEN = '\033[38;5;2m'
OLIVE = '\033[38;5;3m'
NAVY = '\033[38;5;4m'
PURPLE = '\033[38;5;5m'
TEAL = '\033[38;5;6m'
SILVER = '\033[38;5;7m'
RED = '\033[38;5;9m'
LIME = '\033[38;5;10m'
YELLOW = '\033[38;5;11m'
BLUE = '\033[38;5;12m'
FUCHSIA = '\033[38;5;13m'
AQUA = '\033[38;5;14m'
WHITE = '\033[38;5;15m'
GREY = '\033[38;5;250m'

BOLD = '\033[1m'
UNDERLINE = '\033[4m'    
END = '\033[0m'

## Parse command-line arguments

parser = argparse.ArgumentParser(description="Generate and manage todo files.")

parser.add_argument("timespan", type=str, help="Span of time")
parser.add_argument("--completed-tasks", action="store_true", help="Show incomplete tasks")
parser.add_argument("--incomplete-tasks", action="store_true", help="Show incomplete tasks")
parser.add_argument("--past-completed-tasks", action="store_true", help="Show incomplete tasks")
parser.add_argument("--past-incomplete-tasks", action="store_true", help="Show incomplete tasks")
parser.add_argument("--past-events", action="store_true", help="Show incomplete tasks")
parser.add_argument("--upcoming-events", action="store_true", help="Show incomplete tasks")
parser.add_argument("-d", "--debug") 

args = parser.parse_args()

## Handle time input 

time_units = parse_time_string(args.timespan)

days = int(time_units['d']) - 1

start_date = datetime.date.today()
end_date = start_date + datetime.timedelta(days=days)

current_date = start_date

## Create files if not already existing

while current_date <= end_date:

    generate_todo_file(current_date)

    current_date += datetime.timedelta(days=1)

## Search for incomplete tasks and upcoming events in the todo files

completed_tasks, incomplete_tasks, upcoming_events, past_events = scan_todo_files(start_date, end_date)

display_status(completed_tasks, incomplete_tasks, upcoming_events, past_events)




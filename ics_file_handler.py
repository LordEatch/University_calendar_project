from ics import Calendar

def get_events_from_file(ics_file_path):
    with open(ics_file_path) as ics_file:
        lines = ics_file.read()

    calendar = Calendar(lines)

    for e in calendar.events:
        print(e.name)

get_events_from_file("moodle_calendar.ics")

def get_events_by_summaries(file_path, summaries):
    event_beginning = 'BEGIN:VEVENT\n'
    event_end = 'END:VEVENT\n'

    with open(file_path) as file:
        lines = file.readlines()

    inside_event = False
    event_found = False
    new_lines = []
    temporary_lines = []
    event_count = 0

    for line in lines:
        if line == event_beginning:
            inside_event = True

        if inside_event:
            temporary_lines.append(line)

            # Check if the line contains any of the given summaries.
            for summary in summaries:
                if summary in line:
                    event_found = True
        else: # If not inside an event...
            new_lines.append(line) # Add the line (most likely calendar info).

        if line == event_end: # If the end of the event has been reached...
            if event_found:
                new_lines += temporary_lines
                event_count += 1

            temporary_lines = []
            inside_event = False # Set to false again so that the last line of the ics file is still read.
            event_found = False

    print(f'{event_count} events found with matching summaries!')

    return new_lines
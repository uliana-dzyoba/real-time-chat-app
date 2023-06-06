import datetime

DATE_FORMAT = "%B %-d"

def split_dates(messages):
    initial_split = messages[0].date_added.strftime(DATE_FORMAT)
    if messages[0].date_added.year != datetime.date.today().year:
        initial_split += f', {messages[0].date_added.year}'
    setattr(messages[0], 'split', initial_split)

    for i in range(1, len(messages)):
        split = None
        if messages[i].date_added.date() != messages[i-1].date_added.date():
            split = messages[i].date_added.strftime(DATE_FORMAT)
            if messages[i].date_added.year != datetime.date.today().year:
                split += f', {messages[i].date_added.year}'
        setattr(messages[i], 'split', split)


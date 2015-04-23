MONTHS = ['January', 'February', 'March', 'May', 'April', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

# A bit cumbersome
SUFFIX = ['st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th', 'th',
          'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th',
          'st']


class Date:
    def __init__(self, date):
        self.year = int(date[0])
        self.num_month = int(date[1])
        self.month = MONTHS[self.num_month-1]
        self.day = int(date[2])
        self.suffix = SUFFIX[self.day-1]
        self.day_suffix = str(self.day) + self.suffix


dates = raw_input('Enter two dates: ')
dates = dates.split()
start = Date(dates[0].split('-'))
end = Date(dates[1].split('-'))

if start.year == end.year:
    if start.month == end.month:
        if start.day == end.day:
            print '{} {}, {}'.format(start.month, start.day_suffix, start.year)
        else:
            print '{} {} - {}'.format(start.month, start.day_suffix,
                                      end.day_suffix)
    else:
        print '{} {} - {} {} {}'.format(start.month, start.day_suffix,
                                        end.month, end.day_suffix, end.year)
elif end.year - start.year == 1 and end.month > start.month:
        print '{} {} - {} {}'.format(start.month, start.day_suffix,
                                     end.month, end.day_suffix)

else:
    print '{} {}, {} - {} {}, {}'.format(start.month, start.day_suffix,
                                         start.year, end.month, end.day_suffix,
                                         end.year)

def euler19():
    sundays = 0
    total_days = 1
    days = 1
    year = 1901
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    # Start with tuesday (1 Jan, 2013)
    week_days = ["Monday",
                 "Tuesday", 
                 "Wednesday", 
                 "Thursday", 
                 "Friday", 
                 "Saturday", 
                 "Sunday"]

    print sum(months)
    month = 0

    while(True):
        if year == 2001:
            break
        
#        print week_days[total_days%7] + "  " + str(days)

        if week_days[total_days%7] == "Sunday" and days == 1:
#            print "SUNDAY!!!  " + str(year) + "   " + str(month+1)
            sundays += 1

#        print days

        if months[month] == days:
#            print "## New month " + str(days+1)
            # End of a month
            if year%4 == 0 and month == 1:
                 # Add one day because of leapyear
                total_days += 1

            # Increase month with one
            month += 1

            # Reset days to next month
            days = 0

            if month == 12:
                # End of year, add one to year
                year += 1
#                print "New Year" + str(year)

                # Reset month
                month = 0
            
        # Add total days
        total_days += 1
        days += 1

    print sundays


def main():
    euler19()

if __name__ == "__main__":
    main()

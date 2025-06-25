def add_time(start, duration, days_start = ''):
    time_period = ''
    start_time = start.split(':')
    duration_time = duration.split(':')

 

    #check and do some change whever start is PM or AM
    if 'PM' in start_time[1]:
        start_time[1] = start_time[1].rstrip(' PM')
        start_time[0] = int(start_time[0]) + 12
    else:
        start_time[1] = start_time[1].rstrip(' AM')

    
    #start + duration(minutes)
    minutes = (int(start_time[1])+ int(duration_time[1]))

    #start + duration(hours)
    hours = (int(start_time[0])+ int(duration_time[0])) 
    
    final_minutes = minutes%60
    #change how minutes look when print
    if final_minutes == 0: 
        final_minutes = '00'
    elif final_minutes < 10:
        final_minutes = '0' + str(final_minutes)

    #cal final_hours where hours + minutes that surpass 60
    final_hours = hours + (minutes//60)

    #cal day_move
    day_move = 0
    if(final_hours) > 24:
        day_move = final_hours//24
        final_hours = final_hours-(24*day_move)

    #PM or AM and 12 case
    if (final_hours-12) >0 :
        time_period = 'PM'
        final_hours = final_hours-12
    elif final_hours == 12:
        time_period = 'PM'
    else:
        time_period = 'AM'
        if final_hours == 0:
            final_hours = 12

    #show next day or days later depend on day_move
    show_day_move = ''
    if day_move == 1:
        show_day_move = ' (next day)'
    elif day_move >1 :
        show_day_move = f' ({day_move} days later)'
    
    #helper function to detect which day to start and end then return to print
    def _find_new_day(days_start, day_move):
        days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        try:
            start_day_index = days_list.index(days_start.capitalize())
        except ValueError:
            return ""
        new_day_index = (start_day_index + day_move) % 7

        return f', {days_list[new_day_index]}'


    new_time = str(final_hours) + ':' + str(final_minutes) + ' ' + time_period + _find_new_day(days_start,day_move) + show_day_move
  

    return new_time


print(add_time('3:30 PM', '2:12'))



def add_time(start, duration, days_start = ''):
    time_period = ''
    start_time = start.split(':')
    duration_time = duration.split(':')

    days_list = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    show_day = ''

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
        print('Day_move =',day_move)

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
    

    show_day = ''
    days = 0
    while days < 7:
        if days_start.lower() == (days_list[days]).lower():
            show_day = f', {days_list[days]}'
            if day_move != 0:
                if (days+day_move)>6:
                    print('test')
                    if day_move < 7:
                        new_days =(days+day_move)-7
                        show_day = f', {days_list[new_days]}'
                    elif day_move >= 7:
                        new_days = (days+day_move)-(7*((day_move+days)//7))
                        show_day = f', {days_list[new_days]}' 
                else:
                    new_days = days+day_move
                    show_day = f', {days_list[new_days]}'
        days += 1

    #put everything into new_time 
    new_time = str(final_hours) + ':' + str(final_minutes) + ' ' + time_period + show_day + show_day_move
  

    return new_time


print(add_time('8:16 PM', '466:02', 'tuesday'))




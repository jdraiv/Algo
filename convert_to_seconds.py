def convert_seconds(sec):
    hour_in_sec = 3600
    min_in_sec = 60
    
    #If secs are more than a min and an hour
    if sec >= 61 and sec >= 3600:
        #Decimal data
        not_decimal = sec % 1 == 0
        string_sec = str(sec)
        length = len(string_sec)
        last_digit = string_sec[length - 1]
        
        #How many hours?
        hours = int(sec) / hour_in_sec
        
        #Seconds left from hour
        rest_hours = sec - (hours * 3600)
        
        if rest_hours >= 60:
            
            if hours > 1:
                hours = str(hours) + " hours, "
            else:
                hours = str(hours) + " hour, "
                
            minutes = int(rest_hours) / min_in_sec
            
            rest_min = rest_hours - (minutes * min_in_sec)
            seconds = rest_min
            
            if minutes > 1:
                minutes = str(minutes) + " minutes, "
            else:
                minutes = str(minutes) + " minute, "
                
            if seconds > 1:
                seconds = str(seconds) + " seconds, "
            else:
                seconds = str(seconds) + " second,"
                
            result = hours + minutes + seconds
            
            return result
            
    #Minutes
    elif sec >= 60 and sec < hour_in_sec:
        minutes = sec / min_in_sec
        
        if minutes > 0:
            rest_min = sec - (minutes * min_in_sec)
            seconds = rest_min
            
            if minutes > 1:
                minutes = str(minutes) + " minutes, "
            else:
                minutes = str(minutes) + " minute, "
                
            if seconds > 1:
                seconds = str(seconds) + " seconds,"
            else:
                seconds = str(seconds) + " second,"
            result = "0 hours, " + minutes + seconds
            return result
            
        else:
            if minutes > 1:
                minutes = str(minutes) + " minutes, "
            else:
                 minutes = str(minutes) + " minute, "
                 
            result = "0 hours," + minutes + "0 seconds"
            return result
    
    #Seconds 
    elif sec < 60:
        seconds = sec
        
        if seconds > 1:
            seconds = str(seconds) + " seconds"
        else:
            seconds = str(seconds) + " second"
            
        result = "0 hours, 0 minutes, " + seconds
        return result
                
 
print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

print convert_seconds(1)
print convert_seconds(80)

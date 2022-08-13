def add_time(start, duration, day=None):
    
    """
    Dias de la semana a usar y variable "Next Day"
    """
    week_days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    """
    Contador de dias siguientes y modificador del nuevo dia
    """
    
    days_count = 0
    modifier_count = 0
    
    """
    Modificador inicial y final
    """
    
    PM_or_AM = ""
    end_modifier = ""
    
    """
    Tiempo final
    """
    
    end_time = ""
    
    """
    Modificador del tiempo inicial si lo hay
    """
     
    PM_or_AM = start.split(" ")[1]
    
    """
    Eliminacion del modificador en el tiempo inicial para dejar solo las horas y minutos creando un nuevo tiempo inicial sin modificador
    """
    
    start = start.split(" ")
    start.pop(1)
    new_startime = "".join(start)
    
    """
    Division en horas y minutos del nuevo tiempo inicial
    """
    
    new_startime = new_startime.split(":")
    
    start_hour = new_startime[0]
    start_minute = new_startime[1]
    
    """
    Hora final dividida en horas y minutos
    """
    
    end_hour = int(start_hour) + int(duration.split(":")[0])
    end_minute = int(start_minute) + int(duration.split(":")[1])
    
    """
    Verificando si la hora es mayor a 12 o es 12
    """
    
    while end_hour > 12:
        end_hour -= 12
        modifier_count += 1
        
    """
    Verificando la suma de minutos
    """
    
    if end_minute > 59:
        end_minute -= 60
        end_hour += 1    
        
    """
    Verificando el contador del modificador para saber que modificador pertenece a la hora final
    """ 
    
    if PM_or_AM == "PM" and modifier_count % 2 == 0:
        end_modifier = "PM"
    elif PM_or_AM == "AM" and modifier_count % 2 == 0:
        end_modifier = "AM"
    elif PM_or_AM == "PM" and modifier_count % 2 == 1:
        end_modifier = "AM"
    elif PM_or_AM == "AM" and modifier_count % 2 == 1:
        end_modifier = "PM"
        
    """
    Resultado del tiempo final
    """
      
    end_time = f"{end_hour}:{str(end_minute).zfill(2)} {end_modifier}"    
    
    """
    Verificando y contando los dias que pasaron
    """
    
    days_count = int()
            
        
    """
    Verificando el dia ingresado por el usuario si lo hay
    """
    
    if day:
        week_day = week_days_list.index(day.title())
        end_day = week_days_list[int((week_day + days_count) % 7)]	
        end_time += f" {end_day}"
    
    if PM_or_AM == "PM" and modifier_count == 1:
        end_time += " (next day)" 
        
    if modifier_count > 1:
        end_time += f", ({int(days_count)} days later)"
    
    return end_time

print(add_time("11:59 PM", "45:05", "wednesday"))
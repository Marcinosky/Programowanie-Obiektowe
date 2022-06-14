# class hours:
#     def __set__(self, instance, value):
#         if value <= 24 and value >= 0: self.value = value
#         else: raise(Exception)
# class minutes:
#     def __set__(self, instance, value):
#         if value <= 60 and value >= 0: self.value = value
#         else: raise(Exception) 
# class seconds:
#     def __set__(self, instance, value):
#         if value <= 60 and value >= 0: self.value = value
#         else: raise(Exception)
# ?????????????????????????????????????????????????????????

class Clock:
    def __init__(self, hours=0 , minutes=0, seconds=0):
        if hours <= 99 and hours >= 0 : self.hours = hours
        else: raise(Exception)
        if minutes <= 60 and minutes >= 0: self.minutes = minutes
        else: raise(Exception)
        if seconds <= 60 and seconds >= 0: self.seconds = seconds
        else: raise(Exception)
    
    def set(self, unit: str, value):
        if unit == "hours" and value <= 99 and value >= 0: self.hours = value
        elif unit == "minutes" and value <= 60 and value >= 0: self.minutes = value
        elif unit == "seconds" and value <= 60 and value >= 0: self.seconds = value
        else: raise(Exception)

    def tick(self):
        if self.hours == 99 and self.minutes == 59 and self.seconds == 59:
            print("Limit reached")
        elif self.seconds == 59:
            if self.minutes == 59:
                self.seconds = 0
                self.minutes = 0
                self.hours += 1
            else:
                self.seconds = 0
                self.minutes += 1
        else:
            self.seconds += 1

    def display(self, ticks=0):
        for i in range(ticks):
            self.tick()
        print(self)
        

    def __str__(self):
        string = ""
        if self.hours < 10:
            string += f"0{self.hours}:"
        else:
            string += f"{self.hours}:"
        if self.minutes < 10:
            string += f"0{self.minutes}:"
        else:
            string += f"{self.minutes}:"
        if self.seconds < 10:
            string += f"0{self.seconds}"
        else:
            string += f"{self.seconds}"
        return string

    def __repr__(self):
        return f"Clock({self.hours},{self.minutes},{self.seconds})"


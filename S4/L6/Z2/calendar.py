class Calendar:
    def __init__(self, years=1900 , months=1, days=1):
        if years <= 9999 and years >= 0 : self.years = years
        else: raise(Exception)
        if months <= 12 and months >= 0: self.months = months
        else: raise(Exception)
        if days <= 30 and days >= 0: self.days = days
        else: raise(Exception)
    
    def set(self, unit, value):
        if unit == "years" and value <= 9999 and value >= 0: self.years = value
        elif unit == "months" and value <= 12 and value >= 0: self.months = value
        elif unit == "days" and value <= 30 and value >= 0: self.days = value
        else: raise(Exception)

    def passage_of_time(self):
        if self.years == 9999 and self.months == 12 and self.days == 30:
            print("Limit reached")
        elif self.days == 30:
            if self.months == 12:
                self.days = 0
                self.months = 0
                self.years += 1
            else:
                self.days = 0
                self.months += 1
        else:
            self.days += 1
    
    def is_leap_year(self):
        if self.years % 400 == 0 or self.years % 100 != 0 and self.years % 4 == 0: return True
        else: return False

    def __str__(self):
        string = f"It's year {self.years}, day {self.days} of month {self.months}."
        if(self.is_leap_year()): string += " This is a leap year."
        return string

    def __repr__(self):
        return f"Calendar({self.years},{self.months},{self.days})"

    def test(self):
        print(self.years%100)
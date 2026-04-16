class SayDays:
    def __init__(self,year:int,month:int,day:int):
        self.year=year
        self.month=month
        self.day=day

    def is_leap(self)->bool:
        y=self.year
        return((y%4==0 and y%100!=0) or
               (y%400==0))

    def days(self)->int:
        days_in_month=[31,29 if self.is_leap() else 28,31,30,31,30,31,31,30,31,30,31]
        total=0
        m=0
        while m < self.month-1:
            total += days_in_month[m]
            m += 1
        total += self.day
        return total


    def days_left(self)->int:
        total_days=366 if self.is_leap() else 365
        return total_days - self.days()

    def weekday(self)->int:
        y=self.year
        m=self.month
        d=self.day

        if m<3:
            m+=12
            y-=1
        K=y%100
        J=y//100

        h=(d+(13*(m+1))//
           5+K+K//4+J//4+5*J)%7

        return h

    def weekday_name(self)->str:
        names=[
            "saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
        return names[self.weekday()]

year=int(input("what year is it"))
month=int(input("what month is it"))
day=int(input("what day is it"))

date=SayDays(year,month,day)

print("Days after Jan 1:", date.days())
print("Days until Dec 1:", date.days_left())
print("Numeric day of the week:", date.weekday())
print("English day of the week", date.weekday_name())
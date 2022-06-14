import clock, calendar

clk = clock.Clock()

clk.display()
clk.display(3600)
clk.display(356400)
clk.set("hours", 24)
print(clk)
print(repr(clk))

cal = calendar.Calendar()

print(cal)
for i in range(49334): cal.passage_of_time()
print(repr(cal))
for i in range(934): cal.passage_of_time()
print(cal)
from datetime import datetime

with open("Ugz7QFfTWqg2QFyQaMh4AaABAQ.txt", "r") as f:
    data = f.readlines()
line_number = 0
dates = {}
curr_date = None
for line in data:
    line_number += 1
    fields = line.split(" | ")
    if len(fields) < 3 or line[0] == "#":
        continue
    day_of_week = fields[0].split(", ")[0].replace("\x00", "")
    date = datetime.strptime(fields[0].replace("\x00", ""), "%A, %B %d, %Y")
    string_date = date.strftime("%Y-%m-%d")
    if curr_date != string_date:
        curr_date = string_date
        dates[string_date] = {}
    name = fields[1]
    time = fields[2].split(":")
    if len(time) < 2:
        continue
    try:
        time_in_seconds = int(time[0]) * 60 + int(time[1])
    except:
        continue
    dates[string_date][name] = {"day_of_week": day_of_week, "time": time_in_seconds}
with open("nytmini.sql", "w") as f:
    for date in dates:
        for name in dates[date]:
            day_of_week = dates[date][name]["day_of_week"]
            time_in_seconds = dates[date][name]["time"]
            sql_insert = f"insert into times (day_of_week, date, name, time) values ('{day_of_week}', '{date}', '{name}', {time_in_seconds});"
            f.write(sql_insert)
            f.write("\n")

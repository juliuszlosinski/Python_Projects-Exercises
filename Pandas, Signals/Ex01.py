"""
Juliusz Łosiński ~ 24.03.2023
"""

data_file = open("data.csv")
new_file = open("new_data.csv", "w")
new_file.write("t, ax, ay, az, da\n")
t = 0
first_line_with_data = True
last_converted_line = [0, 0, 0, 0, 0]
for line in data_file:
    if line.count("ax,ay,az") == 0:
        splited_line = line.split(",")
        ax = f"{splited_line[0]}"
        ay = f"{splited_line[1]}"
        az = str(splited_line[2].rstrip("\n"))
        if first_line_with_data:
            new_file.write(f"{t}, {ax}, {ay}, {az}, 0\n")
            last_converted_line[0] = t
            first_line_with_data = False
        else:
            t1, t2 = float(last_converted_line[0]), t
            ax1, ay1, az1 = float(last_converted_line[1]), float(last_converted_line[2]), float(last_converted_line[3])
            ax2, ay2, az2 = float(ax), float(ay), float(az)
            r1_t = ax1 + ay1 + az1
            r2_t = ax2 + ay2 + az2
            da = (r1_t + r2_t)/2
            t += 1
            new_file.write(f"{t}, {ax}, {ay}, {az}, {da}\n")
        last_converted_line[0] = t
        last_converted_line[1] = ax
        last_converted_line[2] = ay
        last_converted_line[3] = az

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
i_counter = 0
f_tot = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    new_line = line.rstrip()
    i_pos = new_line.find(':')
    if not i_pos > 0: continue
    new_line_length: int = len(new_line)
    s_num = new_line[i_pos+1: new_line_length]
    f_num = float(s_num)
    i_counter += 1
    f_tot += round(f_num, 5)


print("Average spam confidence: {}".format(round(f_tot / i_counter, 12)))

# print("Counter:{}\tSum:{}\tAverage:{}".format(i_counter, round(f_tot, 5), round(f_tot, 5) / i_counter))

text = "X-DSPAM-Confidence:    0.8475"


def extract_number_from_line(line):
    flt_number = 0.0
    pos = line.find(':')
    int_text_length = len(line)
    try:
        sub_str = line[pos + 1: int_text_length]
        flt_number = float(sub_str.strip())
    except ValueError:
        print("Problem after the colon at position {} with text length {}".format(pos, int_text_length))
        quit()
    return flt_number


print(extract_number_from_line(text))

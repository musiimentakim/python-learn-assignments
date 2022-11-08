string = 'X-DSPAM-Confidence:0.8475'
colon_pos = string.find(':')
string_extract = string[colon_pos+1 :]
float_extract = float(string_extract.strip())


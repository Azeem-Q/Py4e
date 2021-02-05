text = "X-DSPAM-Confidence:    0.8475"
zpos = text.find('0')
ttf = float(text[zpos:])
print(ttf)
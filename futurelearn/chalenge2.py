# Write your code here :-)



answer = ''
clue = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
for code_seq in (clue):
    ascii_code_seq  = (ord(code_seq))
    print (code_seq + str (ord(code_seq)))
    if code_seq in ('y','z'):
        ascii_code_seq = ascii_code_seq - 26
    next_char = chr (ascii_code_seq+2)
    if ascii_code_seq in (32, 39, 46, 40, 41):
        next_char = chr (ascii_code_seq)
    answer = answer + next_char
print (answer)



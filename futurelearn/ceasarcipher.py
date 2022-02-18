
coded = "Ndrhogx Dhgqe DS-BVHFV EDM LUTH VH YOGOH NU D TVRJ ADGVSY DM EOSS DM QJVSUMUQJY, JO EUTBOF VH DMNTUHUGY, DSRJOGY, GDNJOGDNVRM, GOFVRVHO, POUPTDQJY, DHF GDHY UNJOT NUQVRM. JO LORDGO D GOGLOT UA D MRVOHNVAVR QSDRO UA MNZFY RDSSOF NJO JUZMO UA EVMFUG. JVM NTODNVMOM UH GZMVR EOTO NJUZPJN NU LO NJO LOMN EUTBM UH NJO MZLIORN UA GZMVR VH DTDLVR."
print (coded)

replaced = ''

replacements = {
    'A':'F',
    'B':'K',
    'C':'C',
    'D':'A',
    'E':'W',
    'F':'D',
    'G':'M',
    'H':'N',
    'I':'I',
    'J':'H',
    'K':'K',
    'L':'B',
    'M':'S',
    'N':'T',
    'O':'E',
    'P':'G',
    'Q':'P',
    'R':'C',
    'S':'L',
    'T':'R',
    'U':'O',
    'V':'I',
    'W':'W',
    'X':'X',
    'Y':'Y',
    'Z':'U',
    '.':'.',
    ' ':' ',
    '-':'-',
    ',':',',
    '':'',
    '':'',
    '':''
    
    }

for index, letter in enumerate (coded): 
    replaced = replaced + replacements [letter.upper()]

print ('\n', replaced)



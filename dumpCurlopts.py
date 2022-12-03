import sys

CURLOPTTYPE_LONG = 0
CURLOPTTYPE_OBJECTPOINT = 10000
CURLOPTTYPE_FUNCTIONPOINT = 20000
CURLOPTTYPE_OFF_T = 30000

CURLOPTTYPE_STRINGPOINT  = CURLOPTTYPE_OBJECTPOINT
CURLOPTTYPE_SLISTPOINT  = CURLOPTTYPE_OBJECTPOINT


modes = ['enum', 'macro']
output = input("enter output type: (macro or enum): ")

if(output not in modes):
    print("invalid mode")
    sys.exit()

def CURLOPT(opt, val1, val2): 
    if (output == "macro"): print("#define " + opt, val1 + val2)
    else: print("\t" + opt + " = " + str(val1 + val2) + ",")

with open(input("enter curl.h file path: ")) as curlheader:
    b = curlheader.read()

b = b[b.index("All CURLOPT_* values."):]
opts = []
optfuncs = []

while True:
    try:
        opts += [b[b.index("CURLOPT(CURLOPT") : b.index(")") + 1]]
        b = b[b.index(")") + 1:]
    except ValueError: break

for opt in opts:
    if(opt == ""): pass
    else:
        optfuncs += [opt.replace(opt[8:opt.index(",")], '"' + opt[8:opt.index(",")] + '"')]


if (output == "enum"): print("enum CURLoption\n{")

for opt in optfuncs:
    exec(opt)

print("};")

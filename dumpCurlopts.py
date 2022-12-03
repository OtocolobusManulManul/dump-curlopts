CURLOPTTYPE_LONG = 0
CURLOPTTYPE_OBJECTPOINT = 10000
CURLOPTTYPE_FUNCTIONPOINT = 20000
CURLOPTTYPE_OFF_T = 30000

CURLOPTTYPE_STRINGPOINT  = CURLOPTTYPE_OBJECTPOINT
CURLOPTTYPE_SLISTPOINT  = CURLOPTTYPE_OBJECTPOINT

def CURLOPT(opt, val1, val2): print("#define " + opt, val1 + val2)

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
    if(opt == ""): opts.remove("")
    else:
        optfuncs += [opt.replace(opt[8:opt.index(",")], '"' + opt[8:opt.index(",")] + '"')]

for opt in optfuncs:
    exec(opt)
# a dictionary to store the attr as per learning style
# order of array elements should be maintained
lsDictionary = {
    'vv': ['videostay', 'pdfstay', 'pptstay'],
    'ar': ['forumpost', 'forumstay', 'teststay', 'testcount', 'contentstay', 'contentcount'],
    'si': ['teststay', 'contentstay', 'contentcount', 'total_attempt']
}


#   extract attr from
def extractAttr(data, keyArray):
    arr = []
    for o in data:
        ele = {}
        for key in keyArray:
            ele.__setitem__(key, o[key])
        arr.append(ele)
    return arr


#   to transform the data as per model required
def transformToModelInput(data, attrlist):
    arr = []
    for d in data:
        temp = []
        for attr in attrlist:
            if attr == "contentstay":
                temp.append(d['videostay']+d['pdfstay']+d['pptstay'])
            elif attr == "contentcount":
                temp.append(d['videocount'] + d['pdfcount'] + d['pptcount'])
            else:
                temp.append(d[attr])
        arr.append(temp)
    return arr


def labelOutput(e, ls):
    if ls == 'vv':
        return "visual" if e else "verbal"
    if ls == 'ar':
        return "reflective" if e else "active"
    if ls == 'si':
        return "sensing" if e else "intuitive"

#   to insert the learning style in output
def insertLS(source, target, ls):
    for i, e in enumerate(source):
        target[i].__setitem__(ls, labelOutput(e, ls))
    return target

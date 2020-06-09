import json

main_arr = ['/home/test/ds/pretest', '/reading/ds/1/1', '/slide/ds/1/2', '/slide/ds/1/3', '/video/ds/1/4',
            '/video/ds/1/5', '/video/ds/1/6', '/home/test/ds/quiz1',
            '/video/ds/2/1', '/video/ds/2/2', '/video/ds/2/3', '/video/ds/2/4', '/video/ds/2/5', '/video/ds/2/6',
            '/video/ds/2/7', '/slide/ds/2/8', '/reading/ds/2/9', '/home/test/ds/quiz2',
            '/video/ds/3/1', '/video/ds/3/2', '/slide/ds/3/3', '/video/ds/3/4', '/video/ds/3/5', '/slide/ds/3/6',
            '/reading/ds/3/7', '/home/test/ds/quiz3',
            '/reading/ds/4/1', '/slide/ds/4/2', '/video/ds/4/3', '/video/ds/4/4', '/video/ds/4/5', '/video/ds/4/6',
            '/home/test/ds/quiz4',
            '/video/ds/5/1', '/video/ds/5/2', '/video/ds/5/3', '/slide/ds/5/4', '/reading/ds/5/5',
            '/home/test/ds/quiz5',
            '/home/test/ds/finaltest'
            ]

filter_arr = ['/', '/logout', '/manual', '/glossary', '/forum', '/exam', '/dashboard']

# user_data = [{'path': '[{"timestay":7.602083333333334,"_id":"5ea9dbaed684c93ffb2680f7","url":"/glossary",'
#                       '"type":"glossary","timestamp":1588190126202},{"timestay":1.7187,'
#                       '"_id":"5ea9dd76d684c93ffb2680f8","url":"/home/test/ds/pretest","type":"test",'
#                       '"timestamp":1588190582327},{"timestay":1.1471833333333334,"_id":"5ea9ddedd684c93ffb2680fb",'
#                       '"url":"/reading/ds/1/1","type":"pdf","timestamp":1588190701514},'
#                       '{"timestay":3.0549666666666666,"_id":"5ea9de32d684c93ffb2680fc","url":"/slide/ds/1/2",'
#                       '"type":"ppt","timestamp":1588190770345},{"timestay":3.73845,"_id":"5ea9dee9d684c93ffb2680fd",'
#                       '"url":"/slide/ds/1/3","type":"ppt","timestamp":1588190953643},{"timestay":4.05755,'
#                       '"_id":"5ea9dfc9d684c93ffb2680fe","url":"/video/ds/1/4","type":"video",'
#                       '"timestamp":1588191177950},{"timestay":24.904083333333332,"_id":"5ea9e0bdd684c93ffb2680ff",'
#                       '"url":"/video/ds/1/5","type":"video","timestamp":1588191421403},{"timestay":25.46285,'
#                       '"_id":"5ea9e693d684c93ffb268100","url":"/video/ds/1/6","type":"video",'
#                       '"timestamp":1588192915648},{"timestay":1.5259833333333332,"_id":"5ea9ec8bd684c93ffb268101",'
#                       '"url":"/home/test/ds/quiz1","type":"test","timestamp":1588194443419},'
#                       '{"timestay":14.785983333333334,"_id":"5ea9ecf2d684c93ffb268104","url":"/video/ds/2/1",'
#                       '"type":"video","timestamp":1588194546693},{"timestay":10.048266666666667,'
#                       '"_id":"5ea9f069d684c93ffb268105","url":"/video/ds/2/2","type":"video",'
#                       '"timestamp":1588195433852},{"timestay":13.346833333333333,"_id":"5ea9f2cbd684c93ffb268109",'
#                       '"url":"/video/ds/2/4","type":"video","timestamp":1588196043089},'
#                       '{"timestay":11.893783333333333,"_id":"5ea9f5ffd684c93ffb26810d","url":"/video/ds/2/6",'
#                       '"type":"video","timestamp":1588196863010},{"timestay":10.208833333333333,'
#                       '"_id":"5ea9f8c8d684c93ffb26810e","url":"/video/ds/2/7","type":"video",'
#                       '"timestamp":1588197576637},{"timestay":3.1362666666666668,"_id":"5ea9fb66d684c93ffb268111",'
#                       '"url":"/video/ds/2/7","type":"video","timestamp":1588198246272},'
#                       '{"timestay":5.046983333333333,"_id":"5ea9fc53d684c93ffb268113","url":"/reading/ds/2/9",'
#                       '"type":"pdf","timestamp":1588198483517},{"timestay":2.0725,"_id":"5ea9fd82d684c93ffb268114",'
#                       '"url":"/home/test/ds/quiz2","type":"test","timestamp":1588198786336},'
#                       '{"timestay":10.708116666666667,"_id":"5ea9fe36d684c93ffb268119","url":"/video/ds/3/1",'
#                       '"type":"video","timestamp":1588198966765},{"timestay":8.308016666666667,'
#                       '"_id":"5eab0e139d622207cd1e1359","url":"/video/ds/3/4","type":"video",'
#                       '"timestamp":1588268563285},{"timestay":8.1125,"_id":"5eab10059d622207cd1e135a",'
#                       '"url":"/video/ds/3/5","type":"video","timestamp":1588269061766},'
#                       '{"timestay":3.7583166666666665,"_id":"5eab11fc9d622207cd1e135c","url":"/reading/ds/3/7",'
#                       '"type":"pdf","timestamp":1588269564224},{"timestay":3.2601166666666668,'
#                       '"_id":"5eab12dd9d622207cd1e135d","url":"/home/test/ds/quiz3","type":"test",'
#                       '"timestamp":1588269789723},{"timestay":18.4334,"_id":"5eab13d39d622207cd1e1366",'
#                       '"url":"/forum","type":"forum","timestamp":1588270035707},{"timestay":16.774066666666666,'
#                       '"_id":"5eab18259d622207cd1e1368","url":"/logout","type":"logout","timestamp":1588271141711},'
#                       '{"timestay":13.590683333333333,"_id":"5eab1c2d9d622207cd1e1370","url":"/video/ds/4/3",'
#                       '"type":"video","timestamp":1588272173810},{"timestay":10.023533333333333,'
#                       '"_id":"5eab1f629d622207cd1e1374","url":"/video/ds/4/4","type":"video",'
#                       '"timestamp":1588272994829},{"timestay":7.195,"_id":"5eab21bd9d622207cd1e1376",'
#                       '"url":"/video/ds/4/5","type":"video","timestamp":1588273597583},'
#                       '{"timestay":15.737016666666667,"_id":"5eab23779d622207cd1e1379","url":"/video/ds/4/6",'
#                       '"type":"video","timestamp":1588274039013},{"timestay":1.3194333333333332,'
#                       '"_id":"5eab273d9d622207cd1e137c","url":"/home/test/ds/quiz4","type":"test",'
#                       '"timestamp":1588275005844},{"timestay":12.24795,"_id":"5eab27929d622207cd1e137f",'
#                       '"url":"/video/ds/5/1","type":"video","timestamp":1588275090164},'
#                       '{"timestay":7.1075333333333335,"_id":"5eab2a799d622207cd1e1384","url":"/slide/ds/5/4",'
#                       '"type":"ppt","timestamp":1588275833775},{"timestay":7.974283333333333,'
#                       '"_id":"5eab2c2e9d622207cd1e1388","url":"/video/ds/5/2","type":"video",'
#                       '"timestamp":1588276270390},{"timestay":6.49515,"_id":"5eab2e1cab538a7fd67f0aef",'
#                       '"url":"/video/ds/5/3","type":"video","timestamp":1588276764036},{"timestay":4.2128,'
#                       '"_id":"5eab2fa1ab538a7fd67f0af0","url":"/home/test/ds/quiz5","type":"test",'
#                       '"timestamp":1588277153745},{"timestay":3.4103166666666667,"_id":"5eab30c7ab538a7fd67f0af5",'
#                       '"url":"/home/test/ds/finaltest","type":"test","timestamp":1588277447219}]', 'forumstay':
#                   18.4334, 'forumcount': 1, 'forumpost': 2, 'videostay': 218.23670000000004, 'videocount': 19,
#               'pdfstay':
#                   9.952483333333333, 'pdfcount': 3, 'pptstay': 13.90095, 'pptcount': 3, 'teststay': 17.519849999999998,
#               'testcount': 7, 'total_attempt': 8, '_id': '5ede4d084fe7df405fb487f0',
#               'uid': '5ea9c548d684c93ffb2680e2'}]

# model_output = [{'uid': '5ea9c548d684c93ffb2680e2', 'vv': 'visual', 'ar': 'active', 'si': 'intuitive'},
#                 {'uid': '5ea9c59ad684c93ffb2680e6', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5ea9c6c7d684c93ffb2680ee', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5ea9c670d684c93ffb2680ea', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1bfad66432746fb84e6a7', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1be2766432746fb84e697', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb9313685388922d26f646f', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb92cb285388922d26f6453', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5ea9c711d684c93ffb2680f2', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c34066432746fb84e6df', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1bf7266432746fb84e6a3', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c2d966432746fb84e6d7', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1bf2866432746fb84e69f', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c24c66432746fb84e6cf', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c1e766432746fb84e6c7', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1beeb66432746fb84e69b', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb9300a85388922d26f645b', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c02d66432746fb84e6af', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c29c66432746fb84e6d3', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb9328c85388922d26f6483', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1bfea66432746fb84e6ab', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c31666432746fb84e6db', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb930d885388922d26f6467', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c21e66432746fb84e6cb', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb9320785388922d26f647b', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c1b766432746fb84e6c3', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb9318185388922d26f6473', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb9305385388922d26f645f', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c16966432746fb84e6bf', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c11e66432746fb84e6bb', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb9310885388922d26f646b', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb92fcb85388922d26f6457', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c06d66432746fb84e6b3', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb9309e85388922d26f6463', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c37366432746fb84e6e3', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb1c0bc66432746fb84e6b7', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb9323c85388922d26f647f', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'},
#                 {'uid': '5eb931b985388922d26f6477', 'vv': 'verbal', 'ar': 'reflective', 'si': 'sensing'}]


def getFilterPath(path):
    url_path = []
    for i in range(0, len(path)):
        url = path[i]['url']
        if url not in filter_arr:
            url_path.append(path[i]['url'])
    return calSeqPer(url_path, main_arr)


def calSeqPer(userPath, mainPath):
    count = 0
    j = 0
    i = 0
    userPath_len = len(userPath)
    while i < len(userPath):
        if userPath[i] == mainPath[j]:
            if j < (len(mainPath) - 1):
                j += 1
            i += 1
        else:
            index = findUrl(userPath[i], mainPath)
            if index != -1:
                count += 1
                j = index
            else:
                i += 1
                userPath_len -= 1
    if userPath_len == 0:
        return None
    return round(((userPath_len-count)/userPath_len)*100, 2)


def findUrl(url, mainPath):
    for i in range(0, len(mainPath)):
        if mainPath[i] == url:
            return i
    return -1


def getUserPath(data, output):
    new_output = []
    for i in range(0, len(output)):
        ele = output[i]
        for j in range(0, len(data)):
            if output[i]['uid'] == data[j]['uid']:
                path = json.loads(data[j]['path'])
                if path is not None:
                    ele.__setitem__('sg', getFilterPath(path))
                else:
                    ele.__setitem__('sg', None)
                new_output.append(ele)
    return new_output

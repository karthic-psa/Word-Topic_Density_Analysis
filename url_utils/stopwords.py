def stop_filter():
    fo = open("stopwords.txt", 'r')
    stopw={}
    for word in fo:
        w = word.rstrip('\n')
        if w in stopw:
            continue
        else:
            stopw[w] = 1
    return stopw
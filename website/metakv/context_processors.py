def pluralize(count, string, plural=None):
    if float(count) == 1:
        return u"%s %s" % (count, string)
    else:
        return u"%s %s" % (count, plural if plural else string+"s")

def processor(request):
    context = {
            'request': request,
            'pluralize': pluralize,
            'len': len,
            'str': str,
            'dir': dir,
            'zip': zip,
    }
    return context


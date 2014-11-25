def json_encode(data):
    if isinstance(data, bool):
        if data:
            return "True"
        else:
            return "False"
    elif isinstance(data, (int, float)):
        return str(data)
    elif isinstance(data, str):
        return "'"+escape_string(data)+"'"
    elif isinstance(data, list):
        return "[" + ", ".join(json_encode(d) for d in data) + "]"
    elif isinstance(data,dict):
#	return str(data)
	return "{" + ", ".join(json_encode(d)+':'+json_encode(i) for d,i in data.items()) + "}"
    else:
        raise TypeError("%s is not JSON serializable" % repr(data))

def escape_string(s):
    """Escapes double-quote, tab and new line characters in a string."""
    s = s.replace('"', '\\"')
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s
a=json_encode({'a':True,'b':2})
print a
print type(a)
a=json_encode([1,2,3])
print a

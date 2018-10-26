words = ['hi', 'solo', 'learn']
more = [x*len(x) for x in words]
print(len(max(more, key = len)))
print(len(min(more, key = len)))

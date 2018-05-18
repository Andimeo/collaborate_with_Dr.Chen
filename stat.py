users = []

with open('userFeature.data', 'r') as f:
    count = 0
    for line in f:
        user = {}
        attribs = line.split('|')
        for attrib in attribs:
            parts = attrib.split(' ')
            if len(parts) == 2:
                user[parts[0]] = parts[1]
            else:
                user[parts[0]] = parts[1:]
        users.append(user)
        count += 1
        if count % 500000 == 0:
            print("%d has been handled..." % count)

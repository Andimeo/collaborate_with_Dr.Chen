wf = open('userFeature.csv', 'w')

keys_set = set()
keys = []
c = 0
with open('userFeature.data', 'r') as rf:
    for line in rf:
        c += 1
        attribs = line.split('|')
        for attrib in attribs:
            parts = attrib.split(' ')
            key = parts[0]
            value = ','.join(parts[1:])
            if key not in keys_set:
                keys.append(key)
                keys_set.add(key)
        if c % 500000 == 0:
            print('%d keys handled...' % c);

# write header
wf.write('\t'.join(keys) + '\n')

c = 0
with open('userFeature.data', 'r') as rf:
    for line in rf:
        c += 1
        attribs = line.split('|')
        d = {}
        for attrib in attribs:
            parts = attrib.split(' ')
            key = parts[0]
            value = ','.join(parts[1:])
            d[key] = value
        vl = []
        for key in keys:
            if key not in d:
                vl.append('')
            else:
                vl.append(d[key].strip())
        wf.write('\t'.join(vl) + '\n')
        if c % 500000 == 0:
            print('%d values handled...' % c)

wf.close()
            
                
            

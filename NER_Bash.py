from lxml import etree
import re
import os


def find_date(w, a):
    try:
        attr = a.attrib['trans']
        subtag = etree.Element('date')
        M = re.compile('([1234567890]+?(-|—|-)[1234567890]+?)')
        m = M.search(attr)
        if 'type' not in a.attrib:
            if 'trans' in a.attrib and a.attrib['trans'] in arr:
                a.attrib['type'] = 'date'
                subtag = etree.Element('date')
                if w.getprevious() != None:
                    for b in w.getprevious():
                        if b.tail[0] != None and b.tail[0] in string:
                            b.attrib['type'] = 'date'
                            if w.getprevious() != subtag and w.getparent().tag != subtag:
                                w.addprevious(subtag)
                            subtag.append(b.getparent())
                if w.getnext() != None:
                    for d in w.getnext():
                        if d.attrib['lex'][0] in string:
                            d.attrib['type'] = 'date'
                            if w.getprevious() != subtag and w.getparent().tag != subtag:
                                w.addprevious(subtag)
                            subtag.append(w)
                            if d.getparent().getnext() != None:
                                for q in d.getparent().getnext():
                                    if q.attrib['lex'] != None:
                                        if q.attrib['lex'] in arr:
                                            subtag.append(d.getparent())
                                            subtag.tail = q.getparent().tail
                                            subtag.append(q.getparent())
                                        if q.attrib['lex'] not in arr:
                                            subtag.tail = d.getparent().tail
                                            subtag.append(d.getparent())
                        if d.attrib['lex'][0] not in string:
                            subtag.tail = w.tail
                            subtag.append(w)  
            if m != None:
                if w.getnext() != None:
                    for b in w.getnext():
                        if b.attrib['trans'] != None and b.attrib['trans'] in arr:
                            if w.getprevious() != subtag and w.getparent().tag != subtag:
                                w.addprevious(subtag)
                            a.attrib['type'] = 'date'
                            b.attrib['type'] = 'date'
                            subtag.append(w)
                            if b.getparent().tail != None and b.getparent().tail not in punct:
                                if b.getparent().getnext() != None:
                                    for c in b.getparent().getnext():
                                        if c.tail != None and c.tail[0] in string:
                                            if c.getparent().getnext() != None:
                                                for d in c.getparent().getnext():
                                                    if d.attrib['lex'] != None:
                                                        if d.attrib['lex'] == 'йыл':
                                                            c.attrib['type'] = 'date'
                                                            d.attrib['type'] = 'date'
                                                            subtag.append(b.getparent())
                                                            subtag.append(c.getparent())
                                                            subtag.tail = d.getparent().tail
                                                            subtag.append(d.getparent())
                                                        if d.attrib['lex'] != 'йыл':
                                                            subtag.tail = b.getparent().tail
                                                            subtag.append(b.getparent())
                                        if c.tail == None or c.tail[0] not in string:
                                            subtag.tail = b.getparent().tail
                                            subtag.append(b.getparent())
                                if b.getparent().getnext() == None:
                                    subtag.tail = b.getparent().tail
                                    subtag.append(b.getparent())
                            if b.getparent().tail in punct:
                                subtag.tail = b.getparent().tail
                                subtag.append(b.getparent())
                        if  b.attrib['lex'] != None and b.attrib['lex'] == 'йыл':
                            subtag.tail = b.getparent().tail
                            subtag.append(b.getparent())
    except TypeError:
        None
    except KeyError:
        None
    except ValueError:
        None
    return()


def find_name_with_initials(w, a):
    try:
        if a.tail == None:
            None
        if a.tail != None:
            if len(a.tail) == 1 and a.tail in capitals and 'type' not in a.attrib:
                parent = a.getparent()
                if parent != None and parent.tail[0] == '.':
                    subtag = etree.Element('names')
                    if w.getprevious() != subtag and w.getparent().tag != subtag:
                        w.addprevious(subtag)
                    subtag.append(w)
                    a.attrib['type'] = 'names'
                    if w.getnext() != None:
                        for p in w.getnext():
                            if p.tail != None:
                                pnextag = p.getparent().getnext()
                                if len(p.tail) == 1 and p.tail in capitals:
                                    if p.getparent().tail[0] == '.':
                                        subtag.append(p.getparent())
                                        p.attrib['type'] = 'names'
                                        if pnextag != None:
                                            for pp in pnextag:
                                                if pp.tail != None and pp.tail[0] in capitals:
                                                    subtag.tail = pp.getparent().tail
                                                    subtag.append(pp.getparent())
                                                    pp.attrib['type'] = 'names'
                                if len(p.tail) != 1 and p.tail[0] in capitals:
                                    subtag.tail = p.getparent().tail
                                    subtag.append(p.getparent())
                                    p.attrib['type'] = 'names'
                            else:
                                subtag.tail = w.tail
                                w.tail = None
    except TypeError:
        None
    except ValueError:
        None
    return()

def sets(file):
    array = []
    f = open(file, 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    text = text.split('\n')
    for a in text:
        array.append(a)
    wordset = set(array)
    return(wordset)

def find_homonimy(w, a):
    try:
        if a.attrib['trans'] in cities_result \
           and a.attrib['trans'] in names_result:
            a.attrib['type'] = 'homonimy'
            subtag = etree.Element('homonimy')
            if w.getprevious() != subtag and w.getparent().tag != subtag:
                w.addprevious(subtag)
            subtag.tail = w.tail
            subtag.append(w)
        if a.attrib['trans'] in cities_result \
           and a.attrib['trans'] in snames_result:
            a.attrib['type'] = 'homonimy'
            subtag = etree.Element('homonimy')
            if w.getprevious() != subtag and w.getparent().tag != subtag:
                w.addprevious(subtag)
            subtag.tail = w.tail
            subtag.append(w)
    except IndexError:
        None
    except KeyError:
        None
    except ValueError:
        None
    return()

def find_name(w, a):
    try:
        if 'type' not in a.attrib:
            if (a.attrib['trans'] != None and a.attrib['trans'] in names_result) or (a.tail != None and a.tail in names_result):
                subtag = etree.Element('names')
                a.attrib['type'] = 'names'
                if w.getprevious() != subtag and w.getparent().tag != subtag:
                    w.addprevious(subtag)
                if w.getnext() == None:
                    subtag.tail = '\n'
                    w.tail = None
                    subtag.append(w)
                if w.getnext() != None:
                    if w.tail[0] not in punct:
                        for b in w.getnext():
                            if (b.attrib['trans'] != None and b.attrib['trans'] in names_result) or (b.tail != None and b.tail in names_result):
                                b.attrib['type'] = 'names'
                                subtag.append(w)
                                if b.getparent().tail != None and b.getparent().tail not in punct:
                                    if b.getparent().getnext() == None:
                                        subtag.tail = '\n'
                                        subtag.append(b.getparent())
                                    if b.getparent().getnext() != None:
                                        for c in b.getparent().getnext():
                                            if 'lex' in c.attrib and (c.attrib['lex'] == 'ул' or c.attrib['lex'] == 'ҡыҙ'):
                                                subtag.append(b.getparent())
                                                c.attrib['type'] = 'names'
                                                subtag.append(c.getparent())
                                                if c.getparent().getnext() == None:
                                                    c.attrib['type'] = 'names'
                                                    subtag.tail = '\n'
                                                    subtag.append(c.getparent())
                                                if c.getparent().getnext() != None:
                                                    for d in c.getparent().getnext():
                                                        if d.attrib['trans'] != None and d.attrib['trans'] in snames_result:
                                                            subtag.append(c.getparent())
                                                            d.attrib['type'] = 'names'
                                                            subtag.tail = '\n'
                                                            subtag.append(d.getparent())
                                                        if d.attrib['trans'] != None and d.attrib['trans'] not in snames_result:
                                                            if d.attrib['trans'][-2:] == 'ов' and d.attrib['trans'][0] in capitals:
                                                                subtag.append(c.getparent())
                                                                d.attrib['type'] = 'names'
                                                                subtag.append(d.getparent())
                                                                subtag.tail = '\n'
                                                            if d.attrib['trans'][-3:] == 'ова' and d.attrib['trans'][0] in capitals:
                                                                subtag.append(c.getparent())
                                                                d.attrib['type'] = 'names'
                                                                subtag.tail = '\n'
                                                                subtag.append(d.getparent())
                                                            if d.attrib['trans'][0] in capitals and (d.attrib['trans'][-2:] == 'ев' \
                                                                                                     or d.attrib['trans'][-2:] == 'ин'):
                                                                subtag.append(c.getparent())
                                                                d.attrib['type'] = 'names'
                                                                subtag.tail = '\n'
                                                                subtag.append(d.getparent())
                                                            if d.attrib['trans'][0] in capitals and (d.attrib['trans'][-3:] == 'ева' \
                                                                                                     or d.attrib['trans'][-3:] == 'ина'):
                                                                subtag.append(c.getparent())
                                                                d.attrib['type'] = 'names'
                                                                subtag.tail = '\n'
                                                                subtag.append(d.getparent())
                                                            else:
                                                                subtag.append(c.getparent())
                                                                subtag.tail = '\n'
                            if b.attrib['trans'] != None and b.attrib['trans'] in snames_result:
                                b.attrib['type'] = 'names'
                                subtag.append(w)
                                subtag.append(b.getparent())
                                subtag.tail = '\n'
                            if b.attrib['trans'] != None and b.attrib['trans'] not in snames_result:
                                if b.attrib['trans'][-2:] == 'ов' and b.attrib['trans'][0] in capitals:
                                    subtag.append(w)
                                    b.attrib['type'] = 'names'
                                    subtag.append(b.getparent())
                                    subtag.tail = '\n'
                                if b.attrib['trans'][-3:] == 'ова' and b.attrib['trans'][0] in capitals:
                                    subtag.append(w)
                                    b.attrib['type'] = 'name'
                                    subtag.append(b.getparent())
                                    subtag.tail = '\n'
                                if b.attrib['trans'][0] in capitals and (b.attrib['trans'][-2:] == 'ев' or b.attrib['trans'][-2:] == 'ин'):
                                    subtag.append(w)
                                    b.attrib['type'] = 'names'
                                    subtag.append(b.getparent())
                                    subtag.tail = '\n'
                                if b.attrib['trans'][0] in capitals and (b.attrib['trans'][-3:] == 'ева' or b.attrib['trans'][-3:] == 'ина'):
                                    subtag.append(w)
                                    b.attrib['type'] = 'names'
                                    subtag.append(b.getparent())
                                    subtag.tail = '\n'
                            else:
                                subtag.append(w)
                                subtag.tail = '\n'
    except IndexError:
        None
    except KeyError:
        None
    except TypeError:
        None
    except ValueError:
        None
    return()

def find_geo(w, a):
    try:
        if 'type' not in a.attrib:
            if a.attrib['trans'] in cities_result:
                subtag = etree.Element('geo')
                if w.getprevious() != subtag and w.getparent().tag != subtag:
                    w.addprevious(subtag)
                if w.getnext() != None:
                    for b in w.getnext():
                        attr = b.attrib['trans']
                        if attr != None and attr in geoarr:
                            subtag.append(w)
                            subtag.tail = b.getparent().tail
                            subtag.append(b.getparent())
                        else:
                            subtag.tail = w.tail
                            subtag.append(w)
                if w.getnext() == None:
                    subtag.tail = w.tail
                    subtag.append(w)
            if a.attrib['trans'] not in cities_result:
                if a.tail in cities_result:
                    subtag = etree.Element('geo')
                    if w.getprevious() != subtag and w.getparent().tag != subtag:
                        w.addprevious(subtag)
                    if w.getnext() != None:
                        for c in w.getnext():
                            attr = c.attrib['trans']
                            if attr != None and attr in geoarr:
                                subtag.append(w)
                                subtag.tail = c.getparent().tail
                                c.getparent().tail = None
                                subtag.append(c.getparent())
                            else:
                                subtag.tail = w.tail
                                subtag.append(w)
                    if w.getnext() == None:
                        subtag.tail = w.tail
                        subtag.append(w)
    except IndexError:
        None
    except KeyError:
        None
    except ValueError:
        None
    return()

def delete_attributes(tree):
    for w2 in tree.xpath('//w'):
        for c in w2:
            try:
                del c.attrib['type']
            except:
                None
    return()


def folders():
    for root, dirs, files in os.walk('BashCorpus'):
        for folder in dirs:
            path = 'Recognised/' + str(root) + '/' + str(folder)
            if not os.path.exists(path):
                os.makedirs(path)
        for fname in files:
            if fname[-5:] == 'xhtml':
                try:
                    tree = etree.parse(root + '/' + fname)
                    for w in tree.xpath('//w'):
                        for a in w:
                            if 'ana' in a.tag:
                                find_date(w, a)
                                find_homonimy(w, a)
                                find_name_with_initials(w, a)
                                find_name(w, a)
                                find_geo(w, a)
                    delete_attributes(tree)
                    path1 = 'Recognised/' + str(root) + '/' + str(fname)
                    et = tree.write_c14n(path1, with_comments = True, compression = 0, inclusive_ns_prefixes = None)
                except SyntaxError:
                    None
            else:
                continue        
    return()


arr = ['йыл', 'ғинуар', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
       'август', 'сентябрь', 'октябрь', 'ноябрь' 'декабрь', 'январь']
geoarr = ['республика', 'город', 'край', 'область', 'федерация', 'река',
          'озеро', 'гора', 'колхоз', 'район']
string = '0123456789'
punct = ',.!?:;'
capitals = 'ЙФЯЦЫЧУВСКАМЕПИНРТГОШЛБЩДЮЗЖХЭӘӨҮҠҢҒҘҺҪ'
cities = 'Cities.txt'
namesfile = 'NamesCapitalised.txt'
snamesfile = 'SnamesCapitalised.txt'
cities_result = sets(cities)
names_result = sets(namesfile)
snames_result = sets(snamesfile)
folders()

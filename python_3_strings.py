<<<<<<< HEAD
# python3 -c "..." wäre kurz, besser: Datei-skript
# Führe das in /home/gseraria/Repo_Work/NFDI4Memory_Measure1_Task4 aus
import re, sys, json
s = open('index.html', encoding='utf-8').read()
m = re.search(r'const\s+fileFormatsJSONString\s*=\s*`(.*?)`;', s, re.S)
if not m:
    print('ERROR: fileFormatsJSONString nicht gefunden')
    sys.exit(2)
js = m.group(1)
try:
    json.loads(js)
    print('JSON OK')
except Exception as e:
    print('JSON ERROR:', e)
    pos = getattr(e, 'pos', None)
    if pos is None and hasattr(e, 'args') and len(e.args) > 1:
        pos = e.args[1]
    if pos is not None:
        start = max(0, pos-80); end = min(len(js), pos+80)
        print('\\nContext around error (showing markers):\\n')
        snippet = js[start:end]
        print(snippet.replace('\\n','\\n'))
=======
# python3 -c "..." wäre kurz, besser: Datei-skript
# Führe das in /home/gseraria/Repo_Work/NFDI4Memory_Measure1_Task4 aus
import re, sys, json
s = open('index.html', encoding='utf-8').read()
m = re.search(r'const\s+fileFormatsJSONString\s*=\s*`(.*?)`;', s, re.S)
if not m:
    print('ERROR: fileFormatsJSONString nicht gefunden')
    sys.exit(2)
js = m.group(1)
try:
    json.loads(js)
    print('JSON OK')
except Exception as e:
    print('JSON ERROR:', e)
    pos = getattr(e, 'pos', None)
    if pos is None and hasattr(e, 'args') and len(e.args) > 1:
        pos = e.args[1]
    if pos is not None:
        start = max(0, pos-80); end = min(len(js), pos+80)
        print('\\nContext around error (showing markers):\\n')
        snippet = js[start:end]
        print(snippet.replace('\\n','\\n'))
>>>>>>> fdd74a8b9d39603df3cafb5e207381f7c034b94f
    sys.exit(3)
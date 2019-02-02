import re
import urllib.request

# Get list of Clang warnings from docs
url = 'https://clang.llvm.org/docs/DiagnosticsReference.html'
r = urllib.request.urlopen(url)
data = r.read().decode('utf-8')


def line_iter(s):
    return iter(s.splitlines())


out = []
for line in line_iter(data):
    m = re.search('>-W(.*?)<', line)
    if m:
        out.append(m.group().strip('>').strip('<'))

# Remove everything after '=' from some warning strings
clang_warnings = []
for w in out:
    if len(w) > 2 and '=' in w:
        clang_warnings.append(w.split('=')[0])
    elif len(w) > 2:
        clang_warnings.append(w)

# Prettyprint
for i in range(len(clang_warnings)):
    if i == 0:
        print("clang_warnings = ['" + clang_warnings[i] + "',")
    elif i < len(clang_warnings) - 1:
        print("                  '" + clang_warnings[i] + "',")
    else:
        print("                  '" + clang_warnings[i] + "']")

import subprocess

# Get huge list of warnings directly from GCC
out = subprocess.run(['gcc -Q --help=warning', '-l'],
                     capture_output=True, shell=True)
out = out.stdout.decode('utf-8')
out = [word for word in out.split() if word.startswith('-W')]

# Remove everything after '=' from some warning strings
gcc_warnings = []
for w in out:
    if len(w) > 2 and '=' in w:
        gcc_warnings.append(w.split('=')[0])
    elif len(w) > 2:
        gcc_warnings.append(w)

# Prettyprint
for i in range(len(gcc_warnings)):
    if i == 0:
        print("gcc_warnings = ['" + gcc_warnings[i] + "',")
    elif i < len(gcc_warnings) - 1:
        print("                '" + gcc_warnings[i] + "',")
    else:
        print("                '" + gcc_warnings[i] + "']")

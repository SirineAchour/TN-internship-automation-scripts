import os
import glob

pwd = os.getcwd()
directory = pwd[:len(pwd) - 7] + "site\\TN-Nodejs-Production"
files = {}

# create list of all filenames
for file in glob.iglob(directory + '**/**', recursive=True):
    if "node_modules" in file or "Docker" in file or ("package" in file and 'json' in file):
        continue
    if os.path.isfile(file):
        files[file] = False

for file in files:
    if not file.endswith(".ico") and not file.endswith(".jar") and not file.endswith(".jpg") and not file.endswith(
            ".png"):
        for ff in files:
            if file != ff:
                index_filename = ff.rfind('\\')
                filename = ff[index_filename + 1:]
                if ff.endswith('.js') and 'server' not in ff:
                    filename = filename.split('.js')[0]
                with open(file) as f:
                    for line in f:
                        if filename in line:
                            files[ff] = True

i = 0
for file in files:
    if not files[file]:
        print(file)
        i = i + 1

print(i)
print(len(files))

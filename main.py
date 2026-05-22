import os
import sys
import subprocess

#http://cvsman.com/cvs-1.12.12/cvs_119.php#SEC119

def empty():
    pass

func_dict = {
    "add":empty,
    "admin":empty,
    "annotate":empty,
    "checkout":empty,
    "commit":empty,
    "diff":empty,
    "edit":empty,
    "editors":empty,
    "export":empty,
    "history":empty,
    "import":empty,
    "init":empty,
    "kserver":empty,
    "log":empty,
    "login":empty,
    "logout":empty,
    "pserver":empty,
    "rannotate":empty,
    "rdiff":empty,
    "release":empty,
    "remove":empty,
    "rlog":empty,
    "rtag":empty,
    "server":empty,
    "status":empty,
    "tag":empty,
    "unedit":empty,
    "update":empty,
    "version":empty,
    "watch":empty,
    "watchers":empty,
}

def parse(ini):
    x = 0
    for i in range(len(ini)):
        if ini[i] not in func_dict.keys():
            x+=1
        else:
            break
    yield ini[1:x]
    while True:
        y=1
        for i in range(len(ini[x+1:])):
            if ini[x+1:][i] not in func_dict.keys():
                y+=1
            else:
                break
        yield ini[x:x+y]
        x=x+y

def version(start):
    print("""Fake CVS (Emulating CVS 1.12.13 ("Latest")):
To address security concerns, as well as to bring version control
to the modern age, this wrapper exists to emulate the most recent
version of CVS through Git, which through services such as Gitlab
, allow for automatic checks and builds not otherwise possible.""")

stout = subprocess.STDOUT
predicate = ""

def main(start):
    #-b ❌
    #-d root✅
    #-e editor✅
    #-f
    #-H / --help✅
    #-R 
    #-n ❌
    #-Q ✅
    #-q ✅
    #-r
    #-s variable=value
    #-T tempdir
    #-t
    #-v / --version✅
    #-w
    #-x ❌
    #-z gzip-level ✅
    if "-v" in start or "--version" in start:
        version()
        sys.exit(0)
    if "-H" in start or "--help" in start:
        print("""If youre asking for help, its best to learn Git:
https://git-scm.com/cheat-sheet
However, a CVS reference may be found at the following link:
http://cvsman.com/cvs-1.12.12/cvs_174.php#SEC174""")
        sys.exit(0)
    if "-Q" in start:
        stout = subprocess.DEVNULL
    if "-t" in start:
        #GIT_TRACE=true git lga
        predicate += "GIT_TRACE=true GIT_TRACE_SETUP=true"
    if "-e" in start:
        predicate += "GIT_EDITOR=" + str(start[start.index("-e")+1])
        

def add(start): #[options] [files…]
    #-k kflag
    #-m msg

def diff(start): #[options] [files…]
    #-D date1
    #-D date2
    #-l
    #-N
    #-r tag1[:date1]
    #-r tag2[:date2]

def editors(start): #[options] [files…]
    #-l

def init(start):
    pass

def login(start):
    pass

def logout(start):
    pass

def release(start): #[options] directory
    #-d Delete the given directory

def remove(start): #[options] [files…]
    #-f
    #-l

def status(start): #[options] [files…]
    #-l
    #-v

def unedit(start): #[options] [files…]
    #-l

def watch(start): #[on|off|add|remove] [options] [files…]
    #-a actions
    #-l

def watchers(start):
    #-l

if __name__ == "__main__":
    f = open("w", ".gitignore")
    f.write("""
    
    """)
    f.close()

    g = parse(sys.argv)
    main(next(g))
    temp = next(g)
    func_dict[temp[0]](temp[1:])

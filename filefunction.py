import os
import shutil

def filemove(src_, dest_):
    for filename in os.listdir(src_):
        src = os.path.join(src_, filename)
        dest = os.path.join(dest_, filename)
        shutil.move(src, dest)

filemove(rsrc_, rdest_)

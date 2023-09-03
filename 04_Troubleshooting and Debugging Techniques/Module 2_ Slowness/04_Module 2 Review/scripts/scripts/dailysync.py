#!/usr/bin/env python3

import multiprocessing 
import subprocess
import os

home_path = os.path.expanduser('~')
# home_path = os.path.relpath("..")

src = "data/prod"
dest = "data/prod_backup"

src_path = os.path.join(home_path, src)

def run(src, dest):
  subprocess.call(["rsync", "-avv", f"{src}/", dest])
  # print(f'subprocess.call(["rsync", "-arq", {src}/, {dest}])')


if __name__ == "__main__":
  # print(src_path, dest)
  with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
    for root, dirs, files in os.walk(src_path):
      print(root, dirs, files)
      src_p = root
      dest_p = src_p.replace(src, dest)
      pool.apply(run, (src_p, dest_p))

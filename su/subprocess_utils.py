import subprocess


def sprun(args, cwd=None):
    if pp:
        return subprocess.run(args, shell=True, cwd=pp)
    return subprocess.run(args, shell=True)

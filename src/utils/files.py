import time
import hashlib

from django.utils.deconstruct import deconstructible


def hash_file_name(file_fullname:str, with_ext=False):
    a = str(file_fullname)
    negative_point_pos = -a[::-1].find(".") - 1
    file_name = a[:negative_point_pos] + str(time.time())
    hash_file_name = hashlib.md5(file_name.encode()).hexdigest()
    if with_ext == True:
        return hash_file_name + a[negative_point_pos:]
    return hash_file_name


@deconstructible
class path_and_rename(object):
    def __init__(self, sub_path):
        self.path = sub_path
    def __call__(self, instance, filename:str ):
        return self.path + hash_file_name(filename,with_ext=True)

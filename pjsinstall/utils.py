import os
import platform
import re
import shutil
import sys
import tarfile
from zipfile import ZipFile

if sys.version[0] == '2':
    from urllib2 import urlopen
    input = raw_input
elif sys.version[0] == '3':
    from urllib.request import urlopen

PKG_INSTALL_CMD = {
    'win': ('', ),
    'mac': ('', ),
    'debian': ('sudo', 'apt-get', '-y', 'install', ),
    'fedora': ('sudo', 'yum', '-y', 'install', ),
    'rhel': ('sudo', 'yum', '-y', 'install', ),
}

if os.name == 'nt' or platform.system() == 'Windows':
    SYS_OS = 'win'
elif os.name == 'mac' or platform.system() == 'Darwin':
    SYS_OS = 'mac'
else:
    import ld
    SYS_OS = ld.base()

if SYS_OS == 'win':
    EXE_NAME = 'phantomjs.exe'
else:
    EXE_NAME = 'phantomjs'

if sys.maxsize > 2**32:
    SYS_ARCH = 'x64'
else:
    SYS_ARCH = 'x32'


def normalize_version(v_str):
    v_list = list(v_str)
    optional_endings = ('.', '0')

    while v_list[-1] in optional_endings:
        v_list.pop()
    while v_list[0] == '0':
        v_list.pop(0)

    return ''.join(v_list)


def get_archive_ext(url):
    match = re.search(r'(\.[0-9a-z]{1,4})+$', url, re.I)
    if match:
        return match.group(0)
    return None


def get_root_dirname(path):
    last_path = ''

    while True:
        temp_path = os.path.dirname(path)

        if temp_path == path:
            return last_path
        else:
            last_path = path
            path = temp_path


def fetch_file(url, file_path):

    req = urlopen(url)
    with open(file_path, 'wb') as f:
        while True:
            chunk = req.read(20480)
            if not chunk:
                break
            f.write(chunk)
            f.flush()


def extract_from_archive(archive_path, file_path, member_text):
    archive_ext = get_archive_ext(archive_path)

    if archive_ext.endswith('.zip'):

        with ZipFile(archive_path) as archive,\
                open(file_path, 'wb') as f:

            filenames = archive.namelist()
            if len(filenames) == 1:
                f.write(archive.read(filenames[0]))

            for file in filenames:
                if member_text in file:
                    f.write(archive.read(file))
                    break

    elif archive_ext.startswith('.tar'):
        compression = archive_ext[5:]

        with tarfile.open(archive_path, 'r:{}'.format(compression)) as archive:
            for tar_info in archive:
                member_name = tar_info.name

                if member_text in member_name:
                    dir_path = os.path.dirname(archive_path)
                    temp_path = os.path.join(dir_path, member_name)

                    archive.extractall(dir_path, [tar_info])
                    shutil.copy(temp_path, file_path)

                    member_root_dir = get_root_dirname(member_name)
                    shutil.rmtree(os.path.join(dir_path, member_root_dir))

                    break

                # Reset members to avoid high RAM usage
                archive.members = []


def get_input(raw_string, message):
    temp = 0
    while not temp:
        temp = input(message)
        if not re.match(raw_string, temp):
            temp = 0
        else:
            return temp

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from .utils import (
    EXE_NAME, PKG_INSTALL_CMD, SYS_ARCH, SYS_OS,
    extract_from_archive, fetch_file, get_archive_ext, normalize_version,
)
from .versions import CURRENT_VERSION, PJS_VERSION_DATA


class PhantomJSInstaller:
    def __init__(self, dir_path, version=None, method=None):

        self.executable_path = os.path.join(dir_path, EXE_NAME)
        self.temp_dir = os.path.join(tempfile.gettempdir(), 'PhantomJS_install')

        try:
            os.mkdir(self.temp_dir)

        # If an error occurred previously, remove old temp dir
        except:
            shutil.rmtree(self.temp_dir)
            os.mkdir(self.temp_dir)

        os.chdir(self.temp_dir)

        self.version_data = PJS_VERSION_DATA.copy()

        version = version or CURRENT_VERSION
        version = normalize_version(version)

        for key in self.version_data:
            if version == normalize_version(key):
                self.version_data = self.version_data[key][SYS_OS]
                break
        else:
            print('\n\nUnsupported version\n\n')
            self.cleanup()
            sys.exit()

        self.method = method or self.version_data['methods']['default']
        if self.method not in self.version_data['methods']['all']:
            print('\n\nCurrent version does not support this method of installation\n\n')
            self.cleanup()
            sys.exit()

        try:
            os.remove(self.executable_path)
        except:
            pass

    def cleanup(self):
        try:
            os.chdir(os.path.dirname(self.executable_path))
            shutil.rmtree(self.temp_dir)
        except:
            pass

    def install_deps(self):
        deps = self.version_data.get('{}_deps'.format(self.method), None)

        if deps is None:
            return

        pkg_install_cmd = list(PKG_INSTALL_CMD[SYS_OS])
        pkg_install_cmd.extend(deps)

        print('\n\nInstalling dependencies...\n')
        subprocess.call(pkg_install_cmd)

    def run(self):

        try:
            if self.method == 'download':
                print('\n\nFetching archive...\n')

                url = self.version_data['archive_urls'][SYS_ARCH]
                archive_ext = get_archive_ext(url)
                archive_path = os.path.join(
                    self.temp_dir, 'phantomjs{}'.format(archive_ext)
                )

                fetch_file(url, archive_path)

                print('\nExtracting executable from archive...\n')

                member_text = '/bin/{}'.format(EXE_NAME)
                extract_from_archive(archive_path, self.executable_path, member_text)

                self.install_deps()

            else:
                self.install_deps()

                print('\nCompiling...\n')

                build_cmds = self.version_data['build_cmds']

                for cmd in build_cmds:
                    print('\n>>> Running command: {}\n\n'.format(' '.join(cmd)))
                    if cmd[0] == 'cd':
                        os.chdir(cmd[1])
                        continue
                    subprocess.call(cmd)

                shutil.move('bin/phantomjs', self.executable_path)

            print('\n\nInstall successful!\n\n')
            self.cleanup()

        except:
            print('\n\nAn error occurred, automatic installation failed.\n\n')
            self.cleanup()
            raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', required=True, dest='dir')
    parser.add_argument('-v', '--version', dest='version')
    parser.add_argument('-m', '--method', choices=['build', 'download'], dest='method')

    c_args = vars(parser.parse_args())
    installer = PhantomJSInstaller(c_args['dir'], c_args['version'], c_args['method'])
    installer.run()

if __name__ == '__main__':
    main()

import json
import os

PJS_VERSION_DATA = {
    '2.0.0': {
        'win': {
            'methods': {
                'default': 'download',
                'all': ['download', ],
            },
            'archive_urls': {
                'x64': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.0.0-windows.zip',
                'x32': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.0.0-windows.zip',
            },
        },
        'mac': {
            'methods': {
                'default': 'download',
                'all': ['download', ],
            },
            'archive_urls': {
                'x64': 'https://github.com/eugene1g/phantomjs/releases/download/2.0.0-bin/phantomjs-2.0.0-macosx.zip',
                'x32': 'https://github.com/eugene1g/phantomjs/releases/download/2.0.0-bin/phantomjs-2.0.0-macosx.zip',
            },
        },
        'debian': {
            'methods': {
                'default': 'build',
                'all': ['build', ],
            },
            'build_deps': [
                'build-essential', 'g++', 'flex', 'bison', 'gperf', 'ruby', 'perl',
                'libsqlite3-dev', 'libfontconfig1-dev', 'libicu-dev', 'libfreetype6',
                'libssl-dev', 'libpng-dev', 'libjpeg-dev', 'ttf-mscorefonts-installer',
            ],
            'build_cmds': [
                ['git', 'clone', 'git://github.com/ariya/phantomjs.git', ],
                ['cd', 'phantomjs', ],
                ['git', 'checkout', '2.0', ],
                ['./build.sh', ],
            ],
        },
        'fedora': {
            'methods': {
                'default': 'build',
                'all': ['build', ],
            },
            'build_deps': [
                'gcc', 'gcc-c++', 'make', 'flex', 'bison', 'gperf', 'ruby',
                'openssl-devel', 'freetype-devel', 'fontconfig-devel',
                'libicu-devel', 'sqlite-devel', 'libpng-devel', 'libjpeg-devel',
            ],
            'build_cmds': [
                ['git', 'clone', 'git://github.com/ariya/phantomjs.git', ],
                ['cd', 'phantomjs', ],
                ['git', 'checkout', '2.0', ],
                ['./build.sh', ],
            ],
        },
        'rhel': {
            'methods': {
                'default': 'build',
                'all': ['build', ],
            },
            'build_deps': [
                'gcc', 'gcc-c++', 'make', 'flex', 'bison', 'gperf', 'ruby',
                'openssl-devel', 'freetype-devel', 'fontconfig-devel',
                'libicu-devel', 'sqlite-devel', 'libpng-devel', 'libjpeg-devel',
            ],
            'build_cmds': [
                ['git', 'clone', 'git://github.com/ariya/phantomjs.git', ],
                ['cd', 'phantomjs', ],
                ['git', 'checkout', '2.0', ],
                ['./build.sh', ],
            ],
        },
    },
    '2.1.1': {
        'win': {
            'methods': {
                'default': 'download',
                'all': ['download', ],
            },
            'archive_urls': {
                'x64': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip',
                'x32': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip',
            },
        },
        'mac': {
            'methods': {
                'default': 'download',
                'all': ['download', ],
            },
            'archive_urls': {
                'x64': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-macosx.zip',
                'x32': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-macosx.zip',
            },
        },
        'debian': {
            'methods': {
                'default': 'download',
                'all': ['build', 'download', ],
            },
            'build_deps': [
                'build-essential', 'g++', 'flex', 'bison', 'gperf', 'ruby', 'perl',
                'libsqlite3-dev', 'libfontconfig1-dev', 'libicu-dev', 'libfreetype6',
                'libssl-dev', 'libpng-dev', 'libjpeg-dev', 'libx11-dev', 'libxext-dev',
                'ttf-mscorefonts-installer',
            ],
            'build_cmds': [
                ['git', 'clone', 'git://github.com/ariya/phantomjs.git', ],
                ['cd', 'phantomjs', ],
                ['git', 'checkout', '2.1.1', ],
                ['git', 'submodule', 'init', ],
                ['git', 'submodule', 'update', ],
                ['python', 'build.py', '--confirm', ],
            ],
            'archive_urls': {
                'x64': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2',
                'x32': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-i686.tar.bz2',
            },
            'download_deps': ['libfontconfig1-dev', ],
        },
        'fedora': {
            'methods': {
                'default': 'download',
                'all': ['build', 'download', ],
            },
            'build_deps': [
                'gcc', 'gcc-c++', 'make', 'flex', 'bison', 'gperf', 'ruby',
                'openssl-devel', 'freetype-devel', 'fontconfig-devel',
                'libicu-devel', 'sqlite-devel', 'libpng-devel', 'libjpeg-devel',
            ],
            'build_cmds': [
                ['git', 'clone', 'git://github.com/ariya/phantomjs.git', ],
                ['cd', 'phantomjs', ],
                ['git', 'checkout', '2.1.1', ],
                ['git', 'submodule', 'init', ],
                ['git', 'submodule', 'update', ],
                ['python', 'build.py', '--confirm', ],
            ],
            'archive_urls': {
                'x64': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2',
                'x32': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-i686.tar.bz2',
            },
            'download_deps': ['fontconfig-devel', ],
        },
        'rhel': {
            'methods': {
                'default': 'download',
                'all': ['build', 'download', ],
            },
            'build_deps': [
                'gcc', 'gcc-c++', 'make', 'flex', 'bison', 'gperf', 'ruby',
                'openssl-devel', 'freetype-devel', 'fontconfig-devel',
                'libicu-devel', 'sqlite-devel', 'libpng-devel', 'libjpeg-devel',
            ],
            'build_cmds': [
                ['git', 'clone', 'git://github.com/ariya/phantomjs.git', ],
                ['cd', 'phantomjs', ],
                ['git', 'checkout', '2.1.1', ],
                ['git', 'submodule', 'init', ],
                ['git', 'submodule', 'update', ],
                ['python', 'build.py', '--confirm', ],
            ],
            'archive_urls': {
                'x64': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2',
                'x32': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-i686.tar.bz2',
            },
            'download_deps': ['fontconfig-devel', ],
        },
    },
}

CURRENT_VERSION = '2.1.1'

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, 'versions.json'), 'w') as f:
        f.write(json.dumps(PJS_VERSION_DATA))

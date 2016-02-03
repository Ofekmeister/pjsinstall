PJSinstall - PhantomJS universal installer
==========================================

This command line tool attempts to install PhantomJS to the directory of your choice.

Requirements:
- Python with pip installed

Usage:

pjsinstall -d DIR [-v VERSION] [-m {build,download}]


The default version is the current one (located in versions.py) at the time of
this package's last commit. The default method is to download a pre-compiled
binary if available.


TODO:
- Add FreeBSD support
- Add tests

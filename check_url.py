#!/usr/bin/env python

import argparse
import sys
import os
from urlparse import urlparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wrapper for check_http. Calls check_http with port 80 or 443 depending on URL type, unless there is a port in the URL. In case of https, adds -S option.')
    req = parser.add_argument_group('required arguments')
    req.add_argument('-u', '--url', action='store', dest='url', required=True,
            help='URL to test')
    parser.add_argument('-t', '--timeout', action='store', dest='timeout',
            help='timeout')
    parser.add_argument('-d', '--debug', action='store_true', dest='debug',
            help='debug mode')

    param = parser.parse_args()

    exopt = ""

    if param.timeout is not None:
       exopt = " -t " + param.timeout

    if param.debug:
       exopt = exopt + " -v "

    url = param.url

    res = urlparse(url)

    if res.scheme == 'http':
        port = "80"
    elif res.scheme == 'https':
        port = "443"
        exopt += " -S"
    else:
        print("URL contains unsupported protocol: " + res.scheme)
        sys.exit(3)

    if res.netloc != '':
        if len(res.netloc.split(':')) == 2:
            host, port = res.netloc.split(':')
        else:
            host = res.netloc
    else:
        print("Invalid URL: " + url)
        sys.exit(3)

    retval=os.system("/usr/lib64/nagios/plugins/check_http -H " + host + " -p " + port + exopt)

    exit(os.WEXITSTATUS(retval))



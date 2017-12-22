
Wrapper for check_http. Calls check_http with port 80 or 443 depending on URL
type, unless there is a port in the URL. In case of https, adds -S option.

optional arguments:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        timeout
  -d, --debug           debug mode

required arguments:
  -u URL, --url URL     URL to test

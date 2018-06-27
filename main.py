import sys
from siteParser import URLparser


def main():
    try:
        if len(sys.argv) == 2:
            urlname = sys.argv[-1]
        else:
            urlname = raw_input("Please Enter single URL:")
            if ' ' in urlname:
                raise Exception("InputError")
            else:
                print urlname
        site_sent = URLparser(urlname)
        site_data = site_sent.site_parser()
        print site_data
    except Exception:
        print "Something went wrong, please check URL inputs"
        print "1. InputError: Too many URls or"
        print "2. Extra whitespace at end of URL"
        print ">>> Exiting program"

        # url_input =


if __name__ == "__main__":
    main()

import sys
from url_utils.filterContent import Filter
from url_utils.linked_list import Node, LinkedList


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
        site_sent = Filter(urlname)
        site_data = site_sent.filter_data()
        llist = LinkedList()
        for i in site_data:
            new_node = Node(site_data[i], i)
            llist.sortedInsert(new_node)
        # llist.printList()
    except Exception:
        print "Something went wrong, please check URL inputs"
        print "1. InputError: Too many URls or"
        print "2. Extra whitespace at end of URL"
        print ">>> Exiting program"

        # url_input =


if __name__ == "__main__":
    main()

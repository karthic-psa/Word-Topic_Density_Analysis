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
        # print(site_data[0])
        # temp_data = site_data[0]
        # print('in main')
        for j in range(len(site_data)):
            temp_dict = site_data[j]
            llist = LinkedList()
            for i in temp_dict:
                # print(i)
                new_node = Node(temp_dict[i], i)
                llist.sortedInsert(new_node)
            if j == 0:
                print('\n General Top Words - Density/Frequency: ')
                llist.printList()
            if j == 1:
                print('\n Common Topics in page (with weight): ')
                llist.printList()
            if j == 2:
                print('\n Common Words in page (with weight): ')
                llist.printList()
            if j == 3:
                print('\n Phrases in page (with weight): ')
                llist.printList()
            # llist.printList()
            # del llist
            # del new_node
        # llist = LinkedList()
        # for i in temp_data:
        #     # print(i)
        #     new_node = Node(temp_data[i], i)
        #     llist.sortedInsert(new_node)
        # llist.printList()


    except Exception:
        print "Something went wrong, please check URL inputs"
        print "1. InputError: Too many URls or"
        print "2. Extra whitespace at end of URL"
        print ">>> Exiting program"

        # url_input =


if __name__ == "__main__":
    main()

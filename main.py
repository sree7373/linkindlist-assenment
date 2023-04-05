#from linkedlistat_start import *
#from linkedlist_middle import *
#from del_linked import *
#from end_linked import *
import linkedlistat_start
linkedlistat_start.l.insertstartat("jonny")
linkedlistat_start.l.display()
print("insert at start")

import linkedlist_middle
#linkedlist_middle.linkedlist.inseratatmiddle(second,"dog")
linkedlist_middle.linkedlist.display()
print("insert at middle")

import end_linked
end_linked.linked_list.insertatend("when")
end_linked.linked_list.display()
print("insert at end")

import del_linked
del_linked.linked_list.display()
print("deleting data in linked list")
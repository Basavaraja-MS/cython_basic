cdef extern from "linkedlist.c":
    cdef struct linkedist_struct:
        int data 
        linkedist_struct *next
    int count(linkedist_struct* head, int data)
    linkedist_struct* add(linkedist_struct* head, int data)

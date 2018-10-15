
cimport cythonlinkedlist as cll # can be used as it is as

cdef class LinkedList:
    cdef cll.LinkedListStruct *_head
    
    def  __cinit__ (self):
         # It seems sometimes not done with __init__ 
        # http://docs.cython.org/src/userguide/special_methods.html
        self._head = NULL
    
    cpdef add (self, int data): # cpdef void add (~~~~ No
        self._head = cll.add(self._head, data)
        if self._head is NULL:
            raise MemoryError()

    cpdef count (self, int data): # cpdef int count (~~~~ even like a good 
        return cll.count (self._head, data)
    
    def  __iter__ (self):
         # After all , if you also set this special method to def # cpdef, an error
        cdef cll.LinkedListStruct*ptr = self._head
        while ptr is  not NULL:
             yield ptr.data # Implicit type conversion from C int to Python int 
             ptr = ptr.next

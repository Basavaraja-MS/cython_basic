cimport pcipy_h
from libc.stdint cimport *

"""
import sys
def _displayhook(o):
    if type(o).__name__ in ('int', 'long'):
        print(hex(o))
        __builtins__._ = o
    else:
        sys.__displayhook__(o)

def hexon():
    sys.displayhook = _displayhook
def hexoff():
    sys.displayhook=sys.__displayhook__
"""
"""
def display_as_hex(item):
    if isinstance(item, int):
        print(hex(item))
    else:
        print(repr(item))
import sys
sys.displayhook = display_as_hex
"""
cdef class pci:
    cdef pcipy_h.pci_access *pacc
    cdef pcipy_h.pci_dev *cdev
    cdef pcipy_h.pci_dev *rp_dev
    cdef pcipy_h.pci_dev *ep_dev
    cdef int count

    def __cinit__(self):
        self.pacc = pcipy_h.pci_alloc()
        pcipy_h.pci_init(self.pacc)
        pcipy_h.pci_scan_bus(self.pacc)

    def __dealloc__(self):
        pcipy_h.pci_cleanup(self.pacc)

    def get_device(self, domain, bus, dev, func):
        if self.count == 0:
            self.rp_dev = pcipy_h.pci_get_dev(self.pacc, domain, bus, dev, func)
        elif self.count == 1:
            self.ep_dev = pcipy_h.pci_get_dev(self.pacc, domain, bus, dev, func)
        else:
            print("ERROR in get device")
        self.count = self.count + 1
        return self.count
    def dev_info(self):
        self.cdev = self.pacc.devices
        pcipy_h.pci_fill_info(self.cdev, 0xFF)
    def dev_info_next(self):
        self.cdev = self.cdev.next
        pcipy_h.pci_fill_info(self.cdev, 0xFF)

    #TODO Need to truncate reg value to respective numbers
    def read_byte(self, dev, reg):
        if dev == 1:
            cdev = self.rp_dev
            c = pcipy_h.pci_read_byte(cdev, reg)
        elif dev == 2:
            cdev = self.ep_dev
            c = pcipy_h.pci_read_byte(cdev, reg)
        return c

    def read_word(self, dev, reg):
        if dev == 1:
            cdev = self.rp_dev
            c = pcipy_h.pci_read_word(cdev, reg)
        elif dev == 2:
            cdev = self.ep_dev
            c = pcipy_h.pci_read_word(cdev, reg)
        return c

    def read_long(self, dev, reg):
        if dev == 1:
            cdev = self.rp_dev
            c = pcipy_h.pci_read_long(cdev, reg)
        elif dev == 2:
            cdev = self.ep_dev
            c = pcipy_h.pci_read_long(cdev, reg)
        return c

    def read_block(self, dev, pos, buf, len):
        if dev == 1:
            cdev = self.rp_dev
            c = pcipy_h.pci_read_block(cdev, pos, buf, len)
        elif dev == 2:
            cdev = self.ep_dev
            c = pcipy_h.pci_read_block(cdev, pos, buf, len)
        return c

    def read_vpd(self, dev, pos, buf, len):
        if dev == 1:
            cdev = self.rp_dev
            c = pcipy_h.pci_read_vpd(cdev, pos, buf, len)
        elif dev == 2:
            cdev = self.ep_dev
            c = pcipy_h.pci_read_vpd(cdev, pos, buf, len)
        return c

    def write_byte(self, dev, pos, data):
        if dev == 1:
            cdev = self.rp_dev
            c = pcipy_h.pci_write_byte(cdev, pos, data)
        elif dev == 2:
            cdev = self.ep_dev
            c = pcipy_h.pci_write_byte(cdev, pos, data)
        return c

    def write_word(self, dev, pos, data):
        if dev == 1:
            cdev = self.rp_dev
            c = pcipy_h.pci_write_word(cdev, pos, data)
        elif dev == 2:
            cdev = self.ep_dev
            c = pcipy_h.pci_write_word(cdev, pos, data)
        return c

    def write_long(self, dev, pos, data):
        if dev == 1:
            cdev = self.rp_dev
            c = pcipy_h.pci_write_long(cdev, pos, data)
        if dev == 2:
            cdev = self.ep_dev
            c = pcipy_h.pci_write_long(cdev, pos, data)
        return c

    def write_block(self, dev, pos, buf, len):
        if dev == 1:
            cdev = self.rp_dev
            c = pcipy_h.pci_write_block(cdev, pos, buf, len)
        elif dev == 2:
            cdev = self.ep_dev
            c = pcipy_h.pci_write_block(cdev, pos, buf, len)
        return c
"""
print ("Itshould print`:wq!")
var = pci()
var.dev_info()
print ("Its not comming here")
i = 20
while i:
    if i == 0:
        break
    var.dev_info_next()
    print ("0x%x" %var.read_word(0x0))
    i = i - 1

print ("Done with this :)")
#var.write_byte(0xc, 16)
ar = pci()
print ar.read_byte(0x0)

print "Its not printing here"
#var = pci()
ar.dev_info_next()
print ar.read_byte(0x18)
#var.write_byte(0xc, 16)
print ar.read_byte(0xc)
#print configuration info
"""

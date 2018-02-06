cimport pcipy_h

cdef class pci:
	cdef pcipy_h.pci_access *pacc
	cdef pcipy_h.pci_dev *dev

	def __cinit__(self):
		self.pacc = pcipy_h.pci_alloc()
		pcipy_h.pci_init(self.pacc)
		pcipy_h.pci_scan_bus(self.pacc)

	def __dealloc__(self):
		pcipy_h.pci_cleanup(self.pacc)

	cdef pcipy_h.pci_dev *fill_info(self):
		self.dev = self.pacc.devices
		pcipy_h.pci_fill_info(self.dev, 0xFF)
		return self.dev

	cpdef void test_function(self):
		print "Invoked test funtion"

	cdef int read_byte(self, reg):
		cdef int c = pcipy_h.pci_read_byte(self.dev, reg)
		return c

var = pci()
var.test_function()
var.fill_info()
#print var.read_byte(0x032)


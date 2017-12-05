cdef extern from "$(SRC_PATH)/lib/pci.h":
	cdef enum pci_access_type:
		PCI_ACCESS_AUTO
		PCI_ACCESS_SYS_BUS_PCI
		PCI_ACCESS_PROC_BUS_PCI
		PCI_ACCESS_I386_TYPE1
		PCI_ACCESS_I386_TYPE2
		PCI_ACCESS_FBSD_DEVICE
		PCI_ACCESS_AIX_DEVICE
		PCI_ACCESS_NBSD_LIBPCI
		PCI_ACCESS_OBSD_DEVICE
		PCI_ACCESS_DUMP
		PCI_ACCESS_MAX

	cdef struct pci_methods:
		pass
	cdef struct pci_dev:
		pass

	cdef struct pci_access:
		unsigned int method
		int writeable
		int buscentric

		char *id_file_name
		int free_id_name
		int numeric_ids

		unsigned int id_lookup_mode

		int debugging

		struct pci_dev *devices

		struct pci_methods *methods
		struct pci_param *params
		struct id_entry **id_hash
		struct id_bucket *current_id_bucket
		int id_load_failed
		int id_cache_status
		int fd
		int fd_rw
		int fd_pos
		int fd_vpd
		struct pci_dev *cached_dev


	cdef struct pci_access *pci_alloc()
	cdef void pci_init(struct pci_access *)
	cdef void pci_cleanup(struct pci_access *)

	cdef void pci_scan_bus(struct pci_access *acc)
	cdef struct pci_dev *pci_get_dev(struct pci_access *acc, int domain, int bus, int dev, int func)

	cdef void pci_free_dev(struct pci_dev *)


		#Look up methods on next commit 

	cdef struct pci_param:
		struct pci_param *next
		char *param
		char *value
		int value_malloced
		char *help

	cdef char *pci_get_param(struct pci_access *acc, char *param)
	cdef int pci_set_param(struct pci_access *acc, char *param, char *value)
	cdef struct pci_param *pci_walk_params(struct pci_access *acc, struct pci_param *prev)

	cdef struct pci_dev:
		struct pci_dev *next
		u16 domain
		u8 bus
		u8 dev
		u8 func
		int known_fields
		u16 vendor_id
		u16 device_id
		u16 device_class
		int irq
		pciaddr_t base_addr[6]
		pciaddr_t size[6]
		pciaddr_t rom_base_addr
		pciaddr_t rom_size
		struct pci_cap *first_cap
		char *phy_slot
		struct pci_access *access
		struct pci_methods *methods
		u8 *cache
		int cache_len
		int hdrtype
		void *aux

	cdef u8 pci_read_byte(struct pci_dev *, int pos)
	cdef u16 pci_read_word(struct pci_dev *, int pos)
	cdef u32 pci_read_long(struct pci_dev *, int pos)
	cdef int pci_read_block(struct pci_dev *, int pos, u8 *buf, int len)
	cdef int pci_read_vpd(struct pci_dev *d, int pos, u8 *buf, int len)
	cdef int pci_write_byte(struct pci_dev *, int pos, u8 data)
	cdef int pci_write_word(struct pci_dev *, int pos, u16 data)
	cdef int pci_write_long(struct pci_dev *, int pos, u32 data)
	cdef int pci_write_block(struct pci_dev *, int pos, u8 *buf, int len)

	cdef int pci_fill_info(struct pci_dev *, int flags)

	cdef struct pci_cap:
		struct pci_cap *next
		u16 id
		u16 type
		unsigned int addr

	cdef struct pci_cap *pci_find_cap(struct pci_dev *, unsigned int id, unsigned int type)
	cdef struct pci_filter:
		int domain
		int bus
		int slot
		int func
		int vendor
		int device

	cdef void pci_filter_init(struct pci_access *, struct pci_filter *)
	cdef char *pci_filter_parse_slot(struct pci_filter *, char *)
	cdef char *pci_filter_parse_id(struct pci_filter *, char *)
	cdef int pci_filter_match(struct pci_filter *, struct pci_dev *)

	#PCI.id Fetch on next commit


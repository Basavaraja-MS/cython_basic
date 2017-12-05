/*
 *	The PCI Library -- Access to i386 I/O ports on GNU Hurd
 *
 *
 *	Can be freely distributed and used under the terms of the GNU GPL.
 */

#include <sys/io.h>

static inline int
intel_setup_io(struct pci_access *a UNUSED)
{
  return (ioperm (0, 65535, 1) == -1) ? 0 : 1;
}

static inline int
intel_cleanup_io(struct pci_access *a UNUSED)
{
  ioperm (0, 65535, 0);

  return -1;
}
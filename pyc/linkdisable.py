import common
from pcipy import pci

plib = pci()
#rp = find_pci_rp(plib, 0x2e108086)
#rp = find_pci_rp(plib, 0x8086)
#if rp == 0:
#    print("errormsg1")
rp = find_pci_ep(plib, 0x8086)
#if ep == 0:
#    print("errormsg2")

rp_cap = find_extended_cap(plib, cap_id)
#ep_cap = find_extended_cap(ep, cap_id)

rp_ctl = plib.read_word(rp_cap + PCI_EXP_LNKCTL)
if ((rp_cap == 0)  or (rp_cap == 0)):
    print("errormsg3")
if rp_ctl & PCI_EXP_LNKCTL_DISABLE :
    print("Link is Diable")
    #rb.write_word(rp_caps + PCI_EXP_LNKCTL, rp_ctl & ~PCI_EXP_LNKCTL_DISABLE)
else:
    print("Link is Enable")
    #rb.write_word(rp_caps + PCI_EXP_LNKCTL, rp_ctl | PCI_EXP_LNKCTL_DISABLE)


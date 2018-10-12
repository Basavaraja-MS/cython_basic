#!/usr/bin/env python
#

from pcipy import pci

PCI_VENDOR_ID = 0x0
CAPS_OFFSET = 0x34
PCI_EXP_LNKCTL = 0x10
PCI_EXP_LNKCTL_DISABLE = 0x0010 
ENXIO = 0


def find_pci(plib, vendor_id):
    print ("12")
    while True:
        if plib.dev_info_next() != 0x0:
            print ("13")
            if plib.read_word(PCI_VENDOR_ID) == vendor_id:
                break
        else:
            print ("14")
            vendor_id = 0
            break
    return vendor_id


def find_pci_ep(plib, vendor_id):
    plib.dev_info()
    print ("11")
    if find_pci(plib, vendor_id) == vendor_id:
        return vendor_id
    else:
        return ENXIO

def find_pci_rp(plib, vendor_id):
    plib.dev_info()
    print (plib.read_word(PCI_VENDOR_ID))
    if plib.read_word(PCI_VENDOR_ID) == vendor_id:
        return vendor_id
    else:
        return ENXIO


def find_extended_cap(plib, ext_cap_id):
    print("Printing here123123")
    offset = plib.read_word(CAPS_OFFSET)
    print(offset)
    while offset != 0x0:
        regval = plib.read_word(offset)
        if (regval & 0xFF) == ext_cap_id:
            break
        offset = regval & 0xFF00
        offset = offset >> 8
    print ("0x%x" %offset)
    return offset

    
plib = pci()

print ("1")

#rp = find_pci_rp(plib, 0x2e108086)
#rp = find_pci_rp(plib, 0x8086)
#if rp == 0:
#    print("errormsg1")
rp = find_pci_ep(plib, 0x8086)
#if ep == 0:
#    print("errormsg2")

cap_id = 0x10
rp_cap = find_extended_cap(plib, cap_id)
#ep_cap = find_extended_cap(ep, cap_id)

print ("2")
print(rp_cap)
rp_ctl = plib.read_word(rp_cap + PCI_EXP_LNKCTL)

if ((rp_cap == 0)  or (rp_cap == 0)):
    print("errormsg3")

if rp_ctl & PCI_EXP_LNKCTL_DISABLE :
    print("Link is Diable")
    #rb.write_word(rp_caps + PCI_EXP_LNKCTL, rp_ctl & ~PCI_EXP_LNKCTL_DISABLE)
else:
    print("Link is Enable")
    #rb.write_word(rp_caps + PCI_EXP_LNKCTL, rp_ctl | PCI_EXP_LNKCTL_DISABLE)


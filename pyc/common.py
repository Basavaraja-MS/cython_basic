############!/usr/bin/env python


from pcipy import pci
import time
#import logging
from pciheader import *
DEBUG = False
#logging.basicConfig(level=logging.INFO)
#log = logging.getLogger(__name__)
def log_info(*args):
    #print( "INFO:"+" ".join(map(str,args)))
    print(args)

def log_debug(*args):
    if DEBUG == True:
        print( "DEBUG:"+" ".join(map(str,args)))

"""When we want to  redirect logs through file"""
#handler = logging.FileHandler('pcie_stress_test.log')
#handler.setLevel(log.INFO)
#log.addHandler(handler)


"""
PCI_VENDOR_ID = 0x0
PCI_EXP_LNKCTL = 0x10
PCI_EXP_LNKCTL_DISABLE = 0x0010
ENXIO = 0

def file_value(self):
    print ("Added support for the file")

def find_pci(plib, vendor_id):
    while True:
        if plib.dev_info_next() != 0x0:
            if plib.read_long(PCI_VENDOR_ID) == vendor_id:
                break
        else:
            vendor_id = 0
            break
    return vendor_id


def find_pci_ep(plib, vendor_id):
    plib.dev_info()
    if find_pci(plib, vendor_id) == vendor_id:
        return vendor_id
    else:
        print("No EP Device Found")
        return ENXIO

def find_pci_rp(plib, vendor_id):
    plib.dev_info()
    print (plib.read_word(PCI_VENDOR_ID))
    if plib.read_word(PCI_VENDOR_ID) == vendor_id:
        return vendor_id
    else:
        print("No RP Device Found")
        return ENXIO
def link_disable_test(plib, rp_dev, ep_dev, rp_cap, ep_cap):
    rp_ctl = plib.read_byte(rp_dev, rp_cap + PCI_EXP_LNKCTL)
    if (rp_ctl & PCI_EXP_LNKCTL_DISABLE):
        consol_print("Link in Disabled state")
        if show_only == True and Toggle == False:
            return 0
        plib.write(rp_dev, rp_cap + PCI_EXP_LNKCTL, rp_ctl & ~PCI_EXP_LNKCTL_DISABLE)
        consol_print("Link moved to Enabled state")
    else:
        consol_print("Link in Enabled state")
        if show_only == True and Toggle == False:
            return 0
        plib.write(rp_dev, rp_cap + PCI_EXP_LNKCTL, rp_ctl & ~PCI_EXP_LNKCTL_DISABLE)
        consol_print("Link moved to disabled state")
    return 0
"""

PCI_PM_CAP_FLAGS = 0x2
PCIE_POWER_CAPS_ID = 0x1

#Function returns the tuples of rpD1 rpD2 epD1 and epD2 states
def pcipm_get_Dx_stat_t(plib, rp_dev, ep_dev, rp_cap, ep_cap):
    rp_pmc = plib.read_byte(rp_dev, rp_cap + PCI_PM_CAP_FLAGS)
    ep_pmc = plib.read_byte(ep_dev, ep_cap + PCI_PM_CAP_FLAGS)
    rp_D1_support = 1 if (rp_pmc & PCI_PM_CAP_D1) else 0
    rp_D2_support = 1 if (rp_pmc & PCI_PM_CAP_D2) else 0
    ep_D1_support = 1 if (ep_pmc & PCI_PM_CAP_D1) else 0
    ep_D2_support = 1 if (ep_pmc & PCI_PM_CAP_D2) else 0
    log_info("RP D1 %d D2 \n EP D1 %d D2 %d",
                                rp_D1_support, rp_D2_support,
                                ep_D1_support, ep_D2_support)
    return rp_D1_support, rp_D2_support, ep_D1_support, ep_D2_support


def pcipm_get_curr_power_stat_t(plib, rp_dev, ep_dev, rp_cap, ep_cap):
    rp_pmc_ctl = plib.read_byte(rp_dev, rp_cap + PCI_PM_CTRL) & PCI_PM_CTRL_STATE_MASK
    ep_pmc_ctl = plib.read_byte(ep_dev, ep_cap + PCI_PM_CTRL) & PCI_PM_CTRL_STATE_MASK
    log_info("Current power state RP:D%d EP:D%d", rp_pmc_ctl, ep_pmc_ctl)
    return rp_pmc_ctl, ep_pmc_ctl

def pcipm_set_power_stat_t(plib, ep_dev, ep_cap, pcipm):
    pmc_ctl = plib.read_word(ep_dev, ep_cap + PCI_PM_CTRL)
    plib.write_word(ep_dev, ep_cap + PCI_PM_CTRL, pmc_ctl | pcipm)
    log_info("Current power state changed to :D%d", pmc_ctl)

def aspm_get_power_stat(plib, rp_dev, ep_dev, rp_cap, ep_cap):
    rp_lnk_cap = plib.read_word(rp_dev, rp_cap + PCI_EXP_LNKCAP)
    ep_lnk_cap = plib.read_word(ep_dev, ep_cap + PCI_EXP_LNKCAP)
    rp_lnk_cap = rp_lnk_cap & PCI_EXP_LNKCAP_ASPM
    rp_aspm_cap = rp_lnk_cap >> 9
    ep_lnk_cap = ep_lnk_cap & PCI_EXP_LNKCAP_ASPM
    ep_aspm_cap = ep_lnk_cap >> 9
    return rp_aspm_cap, ep_aspm_cap

def aspm_set_power_stat(plib, dev, cap, aspm):
    lnk_ctl = plib.read_word(dev, cap + PCI_EXP_LNKCTL)
    plib.write_word(dev, cap + PCI_EXP_LNKCTL, lnk_ctl | aspm)

def get_link_speed_ep(plib, ep_dev, ep_cap):
    ep_lnk_cap = plib.read_word(ep_dev, ep_cap + PCI_EXP_LNKCAP)\
                                            & PCI_EXP_LNKCAP_SPEED
    return ep_lnk_cap

def get_link_speed_rp(plib, rp_dev, rp_cap):
    rp_lnk_cap = plib.read_word(rp_dev, rp_cap + PCI_EXP_LNKCAP)\
                                            & PCI_EXP_LNKCAP_SPEED
    return rp_lnk_cap

def set_link_speed_ep(plib, ep_dev, ep_cap, link_speed):
    ep_lnk_cap = plib.read_word(ep_dev, ep_cap + PCI_EXP_LNKCTL2)
    plib.write_word(ep_dev, ep_cap + PCI_EXP_LNKCTL2, ep_lnk_cap | link_speed)

def set_link_speed_rp(plib, rp_dev, rp_cap, link_speed):
    rp_lnk_cap = plib.read_word(rp_dev, rp_cap + PCI_EXP_LNKCTL2)
    plib.write_word(rp_dev, rp_cap + PCI_EXP_LNKCTL2, rp_lnk_cap | link_speed)

def set_link_retrain(plib, rp_dev, rp_cap):
    rp_lnk_ctl = plib.read_word(rp_dev, rp_cap + PCI_EXP_LNKCTL)
    plib.write_word(rp_dev, rp_cap + PCI_EXP_LNKCTL, rp_lnk_ctl | PCI_EXP_LNKCTL_RETRAIN)

def check_link_retrain_complet(plib, rp_dev, rp_cap):
    rp_lnk_stat = plib.read_word(rp_dev, rp_cap + PCI_EXP_LNKSTA)
    return rp_lnk_stat & PCI_EXP_LNKSTA_TRAIN

def clear_link_equ(plib, ep_dev, ep_cap):
    link_stat2 = plib.read_word(ep_dev, ep_cap + PCI_EXP_LNKSTA2)
    plib.write_word(ep_dev, ep_cap + PCI_EXP_LNKSTA2, link_stat2 | PCI_EXP_LINKSTA2_EQU_REQ)

def perform_link_equ(plib, rp_dev, rp_ext_cap):
    link_ctl3 = plib.read_word(rp_dev, rp_ext_cap + PCI_EXP_LNKCTL3)
    plib.write_word(rp_dev, rp_cap + PCI_EXP_LNKCTL, link_ctl3 | PCI_EXP_PERFORM_EQU)

def check_equ_status(plib, ep_dev, ep_cap):
    link_stat2 = plib.read_word(ep_dev, ep_cap + PCI_EXP_LNKSTA2)
    if (link_stat2 & PCI_EXP_EQU_COMPLETE):
        log_info("Link Equalization complete\n")
    else:
        log_info("Error: Link Equalization fail\n")
    if (link_stat2 & PCI_EXP_EQU_PHASE_1_SUCC):
        log_info("Link Equalization Phase 1 successfull\n")
    else:
        log_info("Link Equalization Phase 1 failure\n")
    if (link_stat2 & PCI_EXP_EQU_PHASE_2_SUCC):
        log_info("Link Equalization Phase 2 successfull\n")
    else:
        log_info("Link Equalization Phase 2 failure\n")
    if (link_stat2 & PCI_EXP_EQU_PHASE_3_SUCC):
        log_info("Link Equalization Phase 3 successfull\n")
    else:
        log_info("Link Equalization Phase 3 failure\n")


"""
If the Data Link Layer Link Active Reporting Capable field returned
1, then continuously read the Data Link Layer Link Active field
in the Link Status register, and when it returns 1, go on to the
next step. If the Data Link Layer Link Active field does not return
1 before the [RTT] reaches 1 second, then report this as a link
training failure, and skip the remaining steps.
"""
def pci_check_DLL_link_active(plib, rp_dev, rp_cap):
    rp_lnk_cap = plib.read_long(rp_dev, rp_cap + PCI_EXP_LNKCAP)
    if rp_lnk_cap & PCI_EXP_LNKCAP_DLLA:
        time.sleep(1)
        rp_lnk_stat = plib.read_word(rp_dev, rp_cap + PCI_EXP_LNKSTA)
        if rp_lnk_stat & PCI_EXP_LNKSTA_DL_ACT:
            log_info("DLL Link Active")
            return True
        log_info("DLL Link Failure")
        return False


def pci_read_vendor_device_id(plib, ep_dev):
    vendor_id = plib.read_word(ep_dev, PCI_VENDOR_ID)
    device_id = plib.read_word(ep_dev, PCI_DEVICE_ID)
    log_info("vendor id 0x%x device id 0x%x", vendor_id, device_id)
    return vendor_id, device_id

def find_pcie_cap(plib, dev, pci_cap_id):
    offset = plib.read_word(dev, PCI_CAPABILITY_LIST)
    log_debug(offset)
    while offset != 0x0:
        regval = plib.read_word(dev, offset)
        log_info(regval)
        if (regval & 0xFF) == pci_cap_id:
            break
        offset = regval & 0xFF00
        offset = offset >> 8
    log_debug("ofset: 0x%x" %offset)
    return offset

def check_device_status(plib, rp_dev, ep_dev, rp_cap, ep_cap, dev_test):
    if(dev_test["id"] == True):
        vid, did = pci_read_vendor_device_id(plib, ep_dev)
        if (vid == 0xFFFF and did == 0xFFFF):
            log_info("Check DID VID Failed")
            return -1
    if(dev_test["aer_chk"] == True):
        log_info("Yet to impliment")
    if(dev_test["dll_active_chk"] == True):
        pci_check_DLL_link_active(plib, rp_dev, rp_cap)
    return 0

def pci_pm_test(plib, rp_dev, ep_dev, rp_cap, ep_cap, test_param):
    log_info("PCIe PM Test:")
    rp_d1, ep_d1, rp_d2, ep_d2 = pcipm_get_Dx_stat_t(plib,
                                    rp_dev, ep_dev, rp_cap, ep_cap)
    pcipm_get_curr_power_stat_t(plib, rp_dev, ep_dev, rp_cap, ep_cap)
    if (test_param["print_only"] == True):
        return

    d1_test = test_param["d1"]
    d2_test = test_param["d2"]
    if (rp_d1 == ep_d1 == d1_test):
        d1_test = True
    else:
        d1_test = False
    if (ep_d2 == rp_d2 == d2_test):
        d2_test = True
    else:
        d2_test = False

    #dev_test = dict{}
    count = test_param["pcipm_test_count"]
    while (count):
        new_pm = count%4 # Generats a number for set aspm
        if(new_pm == 1 and d1_test == True):
            pcipm_set_power_stat_t(plib, ep_dev, ep_cap, new_pm)
        elif(new_pm == 2 and d2_test == True):
            pcipm_set_power_stat_t(plib, ep_dev, ep_cap, new_pm)
        else: #For D3hot and D0
            pcipm_set_power_stat_t(plib, ep_dev, ep_cap, new_pm)

        time.sleep(1)
        ret = check_device_status(plib, rp_dev, ep_dev, rp_cap, ep_cap, test_param)
        if ret:
            return ret
        count = count - 1


def pci_aspm_test(plib, rp_dev, ep_dev, rp_cap, ep_cap, test_param):
    log_info("PCIe ASPM Test:")
    rp_aspm_cap, ep_aspm_cap = aspm_get_power_stat(plib,
                                    rp_dev, ep_dev, rp_cap, ep_cap)
    log_info("RP:ASPM:Supports")
    if(rp_aspm_cap == 0x0):
        log_info("No ASPM")
    elif(rp_aspm_cap == 0x1):
        log_info("L0s")
    elif(rp_aspm_cap == 0x2):
        log_info("L1")
    elif(rp_aspm_cap == 0x3):
        log_info("L0s and L1")

    log_info("EP:ASPM:Supports")
    if(ep_aspm_cap == 0x0):
        log_info("No ASPM")
    elif(ep_aspm_cap == 0x1):
        log_info("L0s")
    elif(ep_aspm_cap == 0x2):
        log_info("L1")
    elif(ep_aspm_cap == 0x3):
        log_info("L0s and L1")
    if (test_param["print_only"] == True):
        return

    max_aspm = test_param["max_aspm"]
    if (ep_aspm_cap < max_aspm or ep_aspm_cap == 0x0):
        log_info("Invalid ASPM set value, Curr ASPM state%d", ep_aspm_cap)
    count = test_param["aspm_test_count"]
    #dev_test = dict{}
    #dev_test["id"] = 1
    #dev_test["aer"] = test_param["aer_chk"]
    #dev_test["dll_active"] = test_param["dll_active_chk"]
    while (count):
        new_aspm = count % max_aspm # Generats a number for set aspm
        aspm_set_power_stat(plib, ep_dev, ep_cap, new_aspm)
        time.sleep(1)
        ret = check_device_status(plib, rp_dev, ep_dev, rp_cap, ep_cap, test_param)
        if ret:
            return ret
        count = count - 1



def main_test_fun(test_param_dict):
    log_info("Cadence PCIe Application level stress test")
    plib = pci()
    #rp_dev = plib.get_device(seg = 0, bus = 0, dev = 1, fun = 0)
    seg = test_param_dict["segrp"]
    bus = test_param_dict["busrp"]
    dev = test_param_dict["devrp"]
    fun = test_param_dict["funrp"]
    rp_dev = plib.get_device(seg, bus, dev, fun)
    seg = test_param_dict["segep"]
    bus = test_param_dict["busep"]
    dev = test_param_dict["devep"]
    fun = test_param_dict["funep"]
    ep_dev = plib.get_device(seg, bus, dev, fun)
    rp_cap = find_pcie_cap(plib, rp_dev, PCI_CAP_ID_EXP)
    ep_cap = find_pcie_cap(plib, ep_dev, PCI_CAP_ID_EXP)
    rp_pm_cap = find_pcie_cap(plib, rp_dev, PCI_CAP_ID_PM)
    ep_pm_cap = find_pcie_cap(plib, ep_dev, PCI_CAP_ID_PM)
    vendor_id, device_id = pci_read_vendor_device_id(plib, rp_dev)
    log_info("%x- %x"  %(vendor_id, device_id))
    if (test_param_dict["pcipm_test"] == True):
        pci_pm_test(plib, rp_dev, ep_dev, rp_cap, ep_cap, test_param_dict)
    if (test_param_dict["aspm_test"] == True):
        pci_aspm_test(plib, rp_dev, ep_dev, rp_cap, ep_cap, test_param_dict)
"""
#test_param = dict{}
test_param_dict = {
    "pcipm_test": True,
    "aspm_test": True,
    "test_count": 10,
    "aer_chk": False,
    "dll_active_chk": False,
    "print_only": False,
    "d1": False,
    "d2": False,
    "id": True,
    "max_aspm": 1
    }

main_test_fun(test_param_dict)
"""
if "__init__" == "__main__":
    log_info("Cadence PCIe Application level stress test")
    plib = pci()

    rp_dev = plib.get_device(seg = 0, bus = 0, dev = 1, fun = 0)
    ep_dev = plib.get_device(seg = 0, bus = 1, dev = 0, fun = 0)
    rp_cap = find_pcie_cap(plib, rp_dev, cap_id = PCI_CAP_ID_EXP)
    ep_cap = find_pcie_cap(plib, ep_dev, cap_id = PCI_CAP_ID_EXP)
"""
    link_disable_test(plib, rp_dev, ep_dev, rp_cap, ep_cap)
    link_retrian_test(plib, rp_dev, ep_dev, rp_cap, ep_cap)
    aspm_power_test(plib, rp_dev, ep_dev, rp_cap, ep_cap)
    pcipm_power_test(plib, rp_dev, ep_dev, rp_cap, ep_cap)
    link_speed_test(plib, rp_dev, ep_dev, rp_cap, ep_cap)

    rp_ext_cap = find_pcie_ext_cap(plib, rp_dev, ext_cap_id)
    ep_ext_cap = find_pcie_ext_cap(plib, ep_dev, ext_cap_id)
"""

"""
def link_disable():
    show_only = 0
    plib = pci()

#rp = find_pci_rp(plib, 0x2e108086)
#rp = find_pci_rp(plib, 0x8086)
#if rp == 0:
#    print("errormsg1")
    rp = find_pci_ep(plib, 0x10D38086)
#if ep == 0:
#    print("errormsg2")

    cap_id = 0x10
    rp_cap = find_extended_cap(plib, cap_id)
#ep_cap = find_extended_cap(ep, cap_id)

    rp_ctl = plib.read_word(rp_cap + PCI_EXP_LNKCTL)

    if ((rp_cap == 0)  or (rp_cap == 0)):
        print("errormsg3")

    if rp_ctl & PCI_EXP_LNKCTL_DISABLE :
        print("Link is Diable")
        if (show_only == 1):
            return
        plib.write_word(rp_caps + PCI_EXP_LNKCTL, rp_ctl & ~PCI_EXP_LNKCTL_DISABLE)
        print("Entering to Link Enable state")
    else:
        print("Link is Enable")
        if(show_only == 1):
            return
        plib.write_word(rp_cap + PCI_EXP_LNKCTL, rp_ctl | PCI_EXP_LNKCTL_DISABLE)
        print("Entering to Link Disabled state")

link_disable()
"""

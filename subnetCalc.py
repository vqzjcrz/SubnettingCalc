import os
import re
os.system("clear")

#Get/Verify CIDR
def getCIDR(ipInput):
    splitIp = [int(x) for x in ipInput]
    if 1 <= splitIp[0] <= 126:
        _uclass = 8
        _class = 30
        c = "A"
        octR = "1 - 126"
    elif 128 <= splitIp[0] <= 191:
        _uclass = 16
        _class = 30
        c = "B"
        octR = "128 - 191"
    elif 192 <= splitIp[0] <= 223:
        _uclass = 24
        _class = 30
        c = "C"
        octR = "192 - 223"
    else:
        print("IDK how classes D and E work")
        exit()
    
    cidr = int(input(f'Please enter a proper CIDR between {_uclass} and {_class}: '))
    os.system("cls")
    if _uclass <= cidr <= _class:
        bIP = [((8 - len(format(int(ipInput[i]), "b"))) * "0") + str(format(int(ipInput[i]), "b")) for i in range(0, len(ipInput))]
        subnetMaskB = cidr * "1" + (32 - cidr) * "0"
        hostB = (32 - cidr)
        sA = [int(subnetMaskB[i : i + 8], 2) for i in range(0, len(subnetMaskB), 8)]
        nID = ".".join([str(int(ipInput[i]) & int(sA[i])) for i in range(0, len(ipInput))])
        bIP = ".".join([((8 - len(format(int(ipInput[i]), "b"))) * "0") + str(format(int(ipInput[i]), "b")) for i in range(0, len(ipInput))])
        subnetMask = ".".join([str(int(subnetMaskB[index : index + 8], 2)) for index in range(0, len(subnetMaskB), 8)])
        subnetMaskB = ".".join([subnetMaskB[i : i + 8] for i in range(0, len(subnetMaskB), 8)])
        iSubMask = [abs(255 - sA[i]) for i in range(0, len(sA))]
        iSubMaskB = ".".join([format(int(iSubMask[i]), "b") for i in range(0, len(iSubMask))])
        lRange = ".".join([str(int(re.findall("\d+", nID)[i]) + int(iSubMask[i])) for i in range(0, len(iSubMask))])
        luRange = lRange[:-1] + str(int(lRange[len(lRange) - 1]) - 1)
        iSubMask = ".".join([str(iSubMask[i]) for i in range(0, len(iSubMask))])
        subBits = cidr % 8
        maxSubs = 2**subBits
        os.system("cls")
        print(f'Provided Input\n---------------\n| IP: {".".join(ipInput)}\n| CIDR Notation: /{cidr}\n\nSubnet Info\n------------\n\
☆| Subnet Class: {c}\n☆| First Octet Range: {octR}\n☆| Binary IP: {bIP}\n\
☆| Subnet Mask: {subnetMask}\n☆| Binary Subnet Mask: {subnetMaskB}\n\
☆| Wildcard Mask: {iSubMask}\n☆| Binary Wildcard Mask: {iSubMaskB}\n\
☆| Network ID: {nID}\n☆| Default Gateway: {nID[:-1] + "1"}\n☆| Mask Bits: {cidr}\n\
☆| Host Bits: {hostB}\n☆| Subnet Bits: {subBits}\n☆| Max Subnets: {maxSubs}\n\
☆| Usable IP Range: {nID[:-1] + "1"} - {luRange}\n☆| Broadcast ID: {lRange}\n\
☆| Total Hosts: {"{:,}".format(2**hostB)}\n☆| Usable Hosts: {"{:,}".format((2**hostB) - 2)}\n')
        
    else: 
        print("Improper CIDR, try again.")
        getCIDR()

#Verify IP
def getIp():
    ip = str(input("Please enter a proper IP: "))
    os.system("cls")
    ip = re.findall("\d+\.\d+\.\d+\.\d+", ip)
    if ip:
        splitIp = re.findall("\d+", ip[0])
        if len(splitIp) == 4:
            getCIDR(splitIp)
        else:
            print("Improper IP, try again")
            getIp()
    else:
        print("Improper IP, try again")
        getIp()


#Ask for continuation
os.system("cls")
while n := input("Would you like to calculate a subnet? (yes/no)").lower() != "no" :
    getIp()


class tcolors:
	DEST_C = '\033[92m' #GREEN
	SRC_C = '\033[93m' #YELLOW
	PRO_C = "\033[36m" #CYAN
    	RESET = '\033[0m' #RESET COLOR
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[36m' #RED
    RESET = '\033[0m' #RESET COLOR

tcolors.DEST_C +         + tcolors.RESET
tcolors.SRC_C +         + tcolors.RESET
tcolors.PRO_C +         + tcolors.RESET




print(bcolors.OK + "File Saved Successfully!" + bcolors.RESET)
print(bcolors.WARNING + "Warning: Are you sure you want to continue?" + bcolors.RESET)
print(bcolors.FAIL + "Unable to delete record." + bcolors.RESET)

# O(4^n * n) time | O(4^n * n) space
def PhoneNumberMnemonics(phoneNumber):
	currentMnemonic = ['0']*len(phoneNumber)
	mnemonicsFound = []
	PhoneNumberMnemonicsHelper(0,phoneNumber, currentMnemonic, mnemonicsFound)
	return mnemonicsFound

def PhoneNumberMnemonicsHelper(idx, phoneNumber, currentMnemonic,mnemonicsFound):
	if idx == len(phoneNumber):
		mnemonic = "".join(currentMnemonic)
		mnemonicsFound.append(mnemonic)
	else:
		digit = phoneNumber[idx]
		letters = DIGIT_LETTERS[digit]
		for letter in letters:
			currentMnemonic[idx] = letter
			PhoneNumberMnemonicsHelper(idx+1, phoneNumber, currentMnemonic,mnemonicsFound)	

DIGIT_LETTERS = {
	"0":["0"],
	"1":["1"],
	"2":["a","b","c"],
	"3":["d","e","f"],
	"4":["g","h","i"],
	"5":["j","k","l"],
	"6":["m","n","o"],
	"7":["p","q","r","s"],
	"8":["t","u","v"],
	"9":["w","x","y","z"]
}
print(PhoneNumberMnemonics("7"))
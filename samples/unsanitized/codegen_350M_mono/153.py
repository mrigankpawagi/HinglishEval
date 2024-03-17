
def Strongest_Extension(class_name, extensions):
    """
    Aapko ek class ka naam (ek string) aur ek extensions ki list di jayegi.
    Extensions ko additional classes ko class me load karne ke liye use kiya jata hai. Extension ki
    strength is prakar hai: Maan lijiye CAP extension ke naam me uppercase
    letters ki sankhya hai, aur SM extension ke naam me lowercase letters 
    ki sankhya hai, strength ka nirdharan CAP - SM ke fraction se hota hai. 
    Aapko sabse strong extension dhundhni hai aur is 
    format me ek string return karni hai: ClassName.StrongestExtensionName.
    Agar do ya do se adhik extensions ki strength same ho, to aapko
    list me sabse pehle aane wale extension ko chunna chahiye.
    Udaharan ke liye, agar aapko "Slices" class di gayi hai aur extensions ki list me
    hai: ['SErviNGSliCes', 'Cheese', 'StuFfed'] to aapko
    'Slices.SErviNGSliCes' return karna chahiye kyunki 'SErviNGSliCes' sabse strong extension 
    hai (iska strength -1 hai).
    Udaharan:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) =='my_class.AA'
    """
    # print('Input :')
    # inputString = input().upper()
    # listOfStrings = inputString.split()
    # strengthOfExtensions = int(listOfStrings[-1])

    # strengthOfExtensions = listOfStrings[-1].replace('.CAP', '')
    stringLength = len(extensions)

    # while(True):
    for k in range(stringLength - 1, 0, -1):
        # print('Iteration : ', k)

        # Get extension from list of extension with index k (k-1)

import reverse
def orGate(x,y):
            return x|y

def andGate(x,y):
            return x&y

def xorGate(x,y):
            return x^y

def BinaryAddition(number1,number2):
            cin=0
            arrayList=[]
            for i in range(len(number1)-1,-1,-1):
                        x=int(number1[i])
                        y=int(number2[i])
                        bSum=xorGate(cin,(xorGate(x,y)))
                        cout_first=andGate(cin,(xorGate(x,y)))
                        cout_second=andGate(x,y)
                        cout_last=orGate(cout_first,cout_second)
                        cin=cout_last
                        arrayList.append(bSum)
            arrayList2=reverse.reverse(arrayList)
            return arrayList2
        

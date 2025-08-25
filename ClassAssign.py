class AllFunctions():
    def subfields():
        print("Sub-fields in AI are:")
        Subfields=["Machine Learning",
                  "Neural Networks",
                  "Vision",
                  "Robotics",
                  "Speech Processing",
                  "Natural Language Processing",]
        for field in Subfields:
            print(field)

    def OddEven():
        num=int(input("Enter a number:"))
        if (num%2==0):
            print(num,"is Even number")
        else:
            print(num,"is Odd number")

    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="male" and age>=21):
            print("ELIGIBLE")
        elif(gender=="female" and age>=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        S1=int(input("Subject1="))
        S2=int(input("Subject2="))
        S3=int(input("Subject3="))
        S4=int(input("Subject4="))
        S5=int(input("Subject5="))
    
        total=S1+S2+S3+S4+S5
        percentage=(total/500)*100
        print("Total:",total)
        print("Percentage:",percentage)

    def Triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        area=(height*breadth)/2
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle",area)

        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        perimeter=Height1+Height2+Breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",perimeter)
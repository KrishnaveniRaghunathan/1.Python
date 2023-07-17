class multipleFunctions:
  def Subfields():
    AI_Sub_Fields = """Sub-fields in AI are:
    Machine Learning
    Neural Networks
    Vision
    Robotics
    Speech Processing
    Natural Language Processing"""
    print(AI_Sub_Fields)
  # return AI_Sub_Fields
  #---------------------------------------------------------------------------------------------------
  def oddEven():
    num = int(input("Enter a number: "))
    if(num%2==0):
      prn = "%d is Even Number" % (num)
    else:
      prn = "%d is Odd Number" % (num)
    return prn
  #---------------------------------------------------------------------------------------------------
  def Elegible():
    Gen = input("Enter Your Gender: ")
    Age = int(input("Enter Your Age: "))
    print("Your Gender: ",Gen)
    print("Your Age: ",Age)
    if(Gen.upper()=='MALE'):
      if(Age>=26):
        print("ELIGIBLE FOR MARRIAGE")
      else:
        print("NOT ELIGIBLE FOR MARRIAGE")
    elif(Gen.upper()=='FEMALE'):
      if(Age>=21):
        print("ELIGIBLE FOR MARRIAGE")
      else:
        print("NOT ELIGIBLE FOR MARRIAGE")
    else:
      print("Enter Either Male or Female")
    #return 1
  #---------------------------------------------------------------------------------------------------
  def percentage():
    S1 = int(input("Please Enter Subject1 Mark: "))
    S2 = int(input("Please Enter Subject2 Mark: "))
    S3 = int(input("Please Enter Subject3 Mark: "))
    S4 = int(input("Please Enter Subject4 Mark: "))
    S5 = int(input("Please Enter Subject5 Mark: "))
    tot = S1+S2+S3+S4+S5
    per = (S1+S2+S3+S4+S5)/5
    #perd = print('%.2f' % a) print("{0:.3f}".format(a))
    print("Subject1   = ",S1)
    print("Subject2   = ",S2)
    print("Subject3   = ",S3)
    print("Subject4   = ",S4)
    print("Subject5   = ",S5)
    print("Total      = ",tot)
    print("Percentage = ",'%.15f'%per)
  #---------------------------------------------------------------------------------------------------
  def triangle():
    Height = int(input("Enter Height Value: "))
    Breadth = int(input("Enter Breadth Value: "))
    AreaFormula = "Area Formula : (Height*Breadth)/2"
    print("Height : ",Height)
    print("Breadth : ",Breadth)
    print(AreaFormula)
    print("Area of Triangle: ",(Height*Breadth)/2)
    Height1 = int(input("Enter Height1 Value: "))
    Height2 = int(input("Enter Height2 Value: "))
    Breadth = int(input("Enter Breadth Value: "))
    print("Perimeter Formula : Height1 + Height2 + Breadth")
    TPerimeter = Height1 + Height2 + Breadth
    print("Perimeter of Triangle: ",TPerimeter)
   #---------------------------------------------------------------------------------------------------
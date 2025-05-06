def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height*height)
    print("BMI = " + str(bmi))
    if (bmi<18.5):
        print("Under Weight")
        print("-1")
        return
    elif (bmi>=18.5 or bmi<=25.0):
        print("Normal Weight")
        print("0")
        return
    else:
        print("Over Weight")
        print("+1")
        return
       
    
    
calculate_bmi(weight=57, height=1.73)
 
    
  






    



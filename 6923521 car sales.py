#Cars available in SIMAK dealership

#all car prices
Xm5=10000.00
BMW3Series=20000.00
BMWX1=30000.00
BMWX5=40000.00
BMWX7=50000.00
BMWX2=60000.00
Series6=70000.00
XM=80000.00
GranCoupe=90000.00
Convertible=140000.00

C250=50000.00
C320=60000.00
AMGGT=70000.00
Coupe=80000.00
GLS=90000.00
GLECoupe=100000.00
EQE=110000.00
EQB=120000.00
CLS=130000.00
CLA=140000.00

Aventador=50000.00
Huracan=60000.00
Gallardo=70000.00
Urus=80000.00
Countach=90000.00
Murcielago=100000.00
Centenario=110000.00
Diablo=120000.00
Sesto=130000.00
Sian=140000.00


from tabulate import tabulate
print('Welcome To SIMAK Car Dealership')
print('Brands Available')
print('(1)BMW \
      (2)Mercedes \
      (3)Lamborghini ')
    
    
brand=str(input('Specify car Brand with integer attached: '))   


if brand=='1':
    print('These are the BMW Cars Available')
    data = [[1,"Xm5", 2023,], 
        [2,"BMW3Series", 2020], 
        [3,"BMWX1", 2023],
        [4,"BMWX5", 2020],
        [5,"BMWX7", 2013],
        [6,"BMWX2", 2017],
        [7,"Series6", 2018],
        [8,"XM", 2019],
        [9,"GranCoupe", 2012],
        [10,"Convertible", 2016]]
    col_names = ["NO","Cars", "Model"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
    totype=str(input('Specify Car using number attached : '))
    if totype=='1':
     print('this car costs GHS {} To confirm this purchase head to the payment office'.format(Xm5))
    elif totype=='2':
      print('this car costs GHS {} To confirm this purchase head to the payment office'.format(BMW3Series))
    elif totype=='3':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(BMWX1))
    elif totype=='4':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(BMWX5))
    elif totype=='5':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(BMWX7))
    elif totype=='6':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(BMWX2))
    elif totype=='7':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(Series6))
    elif totype=='8':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(XM))
    elif totype=='9':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(GranCoupe))    
    elif totype=='10':
         print('this car costs GHS {} To confirm this purchase head to the payment office'.format(Convertible))  
    else:
         print()
         print('Invalid Selection, Please Run The Program Again')



elif brand=='2':
    print('These are the MERCEDES Cars Available')
    data = [[1,"C250", 2023], 
        [2,"C320", 2023], 
        [3,"AMGGT", 2023], 
        [4,"Coupe", 2023],
        [5,"GLS", 2023],
        [6,"GLECoupe", 2023],
        [7,"EQE", 2023],
        [8,"EQB", 2023],
        [9,"CLS", 2023],
        [10,"CLA", 2023]]
    col_names = ["NO","Cars", "Model"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
    totype=str(input('Specify Car using number attached : '))
    if totype=='1':
     print('this car costs GHS {} To confirm this purchase head to the payment office'.format(C250))
    elif totype=='2':
      print('this car costs GHS {} To confirm this purchase head to the payment office'.format(C320))
    elif totype=='3':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(AMGGT))
    elif totype=='4':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(Coupe))
    elif totype=='5':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(GLS))
    elif totype=='6':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(GLECoupe))
    elif totype=='7':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(EQE))
    elif totype=='8':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(EQB))
    elif totype=='9':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(CLS))    
    elif totype=='10':
         print('this car costs GHS {} To confirm this purchase head to the payment office'.format(CLA)) 
    else:
        print()
        print('Invalid Selection, Please Run The Program Again')





elif brand=='3':
    print('These are the Lamborghini Cars Available')
    data = [[1,"Aventador", 99], 
        [2,"Huracan", 2022], 
        [3,"Gallardo", 2022], 
        [4,"Urus", 2022],
        [5,"Countach", 2022],
        [6,"Murcielago", 2022],
        [7,"Centenario", 2022],
        [8,"Diablo", 2022],
        [9,"Sesto", 2022],
        [10,"B100", 2022]]
    col_names = ["NO","Cars", "Model"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
    totype=str(input('Specify Car using number attached : '))
    if totype=='1':
     print('this car costs GHS {} To confirm this purchase head to the payment office'.format(Aventador))
    elif totype=='2':
      print('this car costs GHS {} To confirm this purchase head to the payment office'.format(Huracan))
    elif totype=='3':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(Gallardo))
    elif totype=='4':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(Urus))
    elif totype=='5':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(Countach))
    elif totype=='6':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(Murcielago))
    elif totype=='7':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(Centenario))
    elif totype=='8':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(Diablo))
    elif totype=='9':
        print('this car costs GHS {} To confirm this purchase head to the payment office'.format(Sesto))    
    elif totype=='10':
         print('this car costs GHS {} To confirm this purchase head to the payment office '.format(Sian))
    else:
        print()
        print('Invalid Selection, Please Run The Program Again')
 
         
    
else:
    print()
    print('Invalid Selection Run The Program Again')
    print('Please use integer attached to Brand name')

    




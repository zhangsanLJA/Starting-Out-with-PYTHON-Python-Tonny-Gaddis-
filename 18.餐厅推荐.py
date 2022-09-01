nou1=input('Is anyone in your party a vegetarain? : ')
nou2=input('Is anyone in your party a vegan? : ')
nou3=input('Is anyone in your party a gluten-free? : ')
if nou1=='no' and nou2=='no' and nou3=='no':
    print("Joe's Gountmet Burgers")
elif nou1=='yes' and nou2=='no' and nou3=='yes':
    print('Main Street Pizza Company')
elif nou1=='yes' and nou2=='yes' and nou3=='yes':
    print('Coener Cafe')
elif nou1=='yes' and nou2=='no' and nou3=='yes':
    print("Manma's Fine Italian")
elif nou1=='yes' and nou3=='yes' and nou3=='yes':
    print("The Chef's Kitchen")
else:
    print('ERROR')

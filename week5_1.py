class Society:
    a_type=25000
    b_type=20000 #class attributes 
    c_type=15000
    d_type=0
    def __init__(self,society_name,house_no,no_of_members,flat,income): #constructor method parametler eklenir
        self.society_name=society_name
        self.house_no=house_no
        self.no_of_members=no_of_members  #obje atttibutes
        self.flat=flat
        self.income=income
        
    
    def allocate_flat():       
        if object_1.income>=object_1.a_type:
             return (f'{object_1.flat}: A Type')
        elif object_1.income> object_1.b_type<object_1.a_type:
            return (f'{object_1.flat}: B Type')
        elif object_1.income>object_1.c_type<object_1.b_type:
            return (f'{object_1.flat}: C Type')
        elif object_1.income<object_1.c_type:
            return (f'{object_1.flat}: D Type')
    
       
    def input_data():
        return (f'society name:{object_1.society_name} \nhouse no:{object_1.house_no} \nno of members:{object_1.no_of_members}\nflat {Society.allocate_flat()}\nincome:{object_1.income}')
        
        
    
object_1=Society('Karadeniz',1,10,"",16000) #object is created

print(Society.input_data())
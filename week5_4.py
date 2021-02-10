class Customer():
    
    
    def __init__(self,name,last_name,adress):
        self.name = name
        self.last_name=last_name
        self.adress=adress   
    def get_cust_info(self):        
        return f'{self.name}  {self.last_name}\n{self.adress}'
    
class Items(Customer):           
    def __init__(self):
        self.shopping_list=[]
    products={"watch":1000,'Ring':2000,'earring':3000}
    
    def calculate_discount(self): 
    
        for i in self.shopping_list:                             
                self.item_price=(self.products[i]*self.shopping_list.count(i))
                if self.item_price>=4000:
                    self.price_tobe_paid=(self.item_price)-(self.item_price* 25/100)
                    self.discount=(self.item_price* 25/100)
                elif self.item_price>=2000:
                    self.price_tobe_paid=(self.item_price)-(self.item_price* 15/100)
                    self.discount=(self.item_price* 15/100) 
                elif self.item_price<2000:
                    self.price_tobe_paid=(self.item_price)-(self.item_price* 10/100)
                    self.discount=(self.item_price* 10/100)  
                    
                    
                return f"Your shoping cart;                        Total Per Item\
                    \n{i}           ${self.products[i]}          {self.shopping_list.count(i)}                 ${self.item_price}\
                    \nDiscount:                                       ${self.discount} \
                    \nTotal:                                          ${self.item_price-self.discount}"                                                                                                                          
             
               
    def shopping_cart(self,value):       
       
        return self.shopping_list.append(value)        
        
        
    
         
cst_1=Customer(input('Name:'),input('Last name:'),input("Adress:"))
prd_1=Items()
while len(prd_1.shopping_list)<1:
    print(f"{Items.products}Lutfen urun secin")
    prd_1.shopping_cart(input(''))
    

print(cst_1.get_cust_info())
print(prd_1.calculate_discount())

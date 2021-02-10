class Product:
    
    def __init__(self,product_id,product_name,product_purchase_price,product_sale_price):
        self.product_id=product_id
        self.product_name=product_name
        self.product_purchase_price=product_purchase_price
        self.product_sale_price=product_sale_price
        
    def set_remarks(self):
        if  self.product_sale_price-self.product_purchase_price<0:
            return ' is negative' 
        else:
            return " is positive"
        
        
        
        
    def get_details(self):
       return (f'product id:{self.product_id}\nproduct name:{self.product_name}\npurchasa price:{self.product_purchase_price}\nsale price:{self.product_sale_price}\nMargin{self.set_remarks()}')
         
        
    
obj_1=Product('1234','Watch',10.30,8.50)
print(obj_1.get_details())

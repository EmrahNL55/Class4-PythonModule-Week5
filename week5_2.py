class Iteminfo:
    discount=''
    net_price=''
    
    def __init__(self,item_code,item,price,qty):
        self.item_code=item_code
        self.item=item
        self.price=price
        self.qty=qty
        
        
    
    def calculate_discount(self):
        
        if self.qty>=11 and self.qty<=20:
            self.discount=15
            return (f'net price:{(self.price*self.qty)-(self.price*self.qty*self.discount/100)}') 
        elif self.qty>20:
            self.discount=20
            return(f'net price:{(self.price*self.qty)-( self.price*self.qty*self.discount/100)}')             
        elif self.qty<=10:
            self.discount=0
            return (f'net price:{( self.price*self.qty)}')
            
            
    def show_all(self):
        if self.qty>=11 and self.qty<=20:
             self.discount=15
        elif self.qty>20:
             self.discount=20
        elif self.qty<=10:
             self.discount=0
        return (f'item code:{ self.item_code}\nitem:{ self.item}\nprice:{self.price}\nqty:{self.qty}\ndiscount:{self.discount}\n{object_buy.calculate_discount()}')
        
        
    
object_buy=Iteminfo(item_code=55,item='Puskevit',price=120,qty=8)

print(object_buy.show_all())
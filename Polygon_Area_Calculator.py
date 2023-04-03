class Rectangle: 
      
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def set_width(self):
        return self.width
        
    def set_height(self):
          return self.height  
    
    def  set_get_amount_inside(self,shape):
            self.width = shape
            self.height = shape 
    def get_amount_inside(self):      
            w = []
            for i in range(1,self.width+1):
                 if i % 2 == 0:
                     w.append(i)
            return (len(w))             
        
    def get_area(self):
        return  self.width * self.height
        
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
        
    def get_diagonal(self): 
        return ((self.width ** 2 + self.height ** 2) ** .5)    
        
    def get_picture(self):    
        if self.width > 50 or   self.height > 50:
           return  "Too big for picture."
        else:
           for i in range(0, self.height):
               print('*'*self.width)
                      
class Square(Rectangle):
      
    def __init__(self,width):
        self.width = width
        self.height = 9
           
    def get_area(self):
        return  self.width * self.height 

    def set_side(self, side):
        self.width = side
        self.height = side
       
    def get_picture(self):    
        if self.width > 50 or   self.height > 50:
           return  "Too big for picture."
        else:
           for i in range(0, self.height):
               print('*'*self.width)
        
rect = Rectangle(10, 5) 
print(rect.get_area())
rect.height = 3 
print(rect.get_perimeter())
print('Rectangle(width=10, height=3)')
rect.get_picture()
print('\n')
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print('Square(side=4)')
sq.get_picture()
print('\n')
rect.set_get_amount_inside(16)
print(rect.get_amount_inside())





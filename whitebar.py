from bar import *
import sys
import ast

class whitebar(bar): 
    def __init__(self,w,mtr):
        self.w = w
        self.ps,self.pt = int(self.w/32*3/4),int(self.w/20*0.75)   #padding sides, padding top
        self.fz = int(self.w/20)     #font size
        self.hg = int(18/16*self.fz) #hnnghhh...no, it's gap between lines
        self.fs = int(4/16*self.fz) #full stop height (Me: blah You: bruh Nobody: bruh22)
        
        self.start = (self.ps,self.pt*3/5)  #where the first text is written
        self.img = Image.open("white.png")
        
        super().__init__(w,mtr)
        super().splatter()
        super().writelines(self.texty)

    def out(self,fn):
        self.img.save(fn)
    

if __name__ == "__main__":
    bob = whitebar(int(sys.argv[1]),ast.literal_eval(join(sys.argv[2:-1]))) #width, text
    bob.out(sys.argv[-1:][0])    #out file
    #bob = ast.literal_eval(sys.argv[2])

class Interface:
    
    def __init__(self):
    
    def line (self,size = 42)-> str:
        return '-'* size
    
    def title (self, txt: str) -> str:
        print(line())
        print(txt.center(42))
        print(line())
    
    def menu (self, op: list) -> str:
        
        c = 1
        for i in op:
            print(f'{c} - {i}')
    
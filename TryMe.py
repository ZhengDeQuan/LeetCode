from typing import List , Tuple
Mytype = Tuple[int,float]
def zq(a :int, b:float,d:List[Mytype] = [(9,9.0)], c="I love you") -> None :
    print(a,b,c)
    print(d)



if __name__ == "__main__":
    print(zq(7,8.0,[("hello",8.0)]))
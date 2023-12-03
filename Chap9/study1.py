class Critter(object):
    """ 가상 펫 """
    total = 0
# 1. 클래스 정의 
# (기본 클래스 상속)
# 클래스 속성을 0으로 초기화 (모든 인스턴스 간에 공유)
    @staticmethod 

    def status():
       print ("\n 총 크리터 수 :\t", Critter.total)
# 위에 정의한 크리터 클래스 내에 정적 메서드인 스테이터스 정의
#(이때 정적 메서드는 클래스에 바인딩되어, 인스턴스와는 관려이 없다.)

#프린트문, 스테이터스 메서드는 클래스 속성 Critter.total로 총수를 출력  

    def __init__ (self, name):
       print ("크리터가 태어났어여!")
       self.name = name 
       Critter.total +=1
 # __init__ 는 특수한 메서드, 클래스 인스턴스가 생성될 때 호출되는 놈
# self는 생성되는 인스턴스를 나타낸다.

#main 메인이 시작된다.

print("클래스 속성 Critter.total에 접근:\t", end=" ")
print(Critter.total)

Critter.status()
# 클래스의 정적 메서드인 스테이터스 호출 

print("\n 크리터 생성 중 ")
    crit1 = Critter ("Manuel")
    crit2 = Critter ("Johnathan")
    crit3 = Critter ("Tom")

    Critter.status () 

print ("\n 객체를 통한 클래스 속성에 접근\t", end="")
print (crit1.total)

input("\n엔터 키를 눌러 종료 하라우")


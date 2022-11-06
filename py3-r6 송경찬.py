"""
    progrmmer : 송경찬
    Date : 2022.10.28
    File name : py3-r6 송경찬.py
    Description: 거북이 경주
"""
import turtle as t #turtle 모듈 사용
import random as r #random 모듈 사용


t.penup()
t.goto(-100,300)
t.pendown()
t.write("* 두개의 거북이 자동 랜덤 게임 *",font = ('TImes New Roman',20,'bold')) #제목 정하기
class turtle_race(t.Turtle):
    ''' t1,t2 클래스 만들기'''

    def race(self, colors):
        '''색깔을 정하고 위치 (-200,200) 으로 가서 대기 '''
        self.shape("turtle")
        self.color(colors)
        self.pencolor(colors)
        self.penup()
        self.goto(-200, 200)
        self.pendown()
        self.speed(0)
        self.width(3)
    def go(self,a,b):
        ''' penup,pendown,goto 활용'''
        self.penup()
        self.goto(a,b)
        self.pendown()
    def bar(self,Height):
        ''' 그래프 바 그리기'''
        self.begin_fill()
        self.forward(Height)
        self.write(str(Height), font = ('Times New Roman', 10, 'bold'))
        self.right(90)
        self.fd(30)
        self.right(90)
        self.fd(Height)
        self.left(90)
        self.fd(7)
        self.left(90)
        self.end_fill()
t = turtle_race() #turtle_race 인스턴스
t1 = turtle_race() #turtle_race 인스턴스
t2 = turtle_race() #turtle_race 인스턴스
t1.race("red")
t2.race("blue")
a = [0] * 5 # a[1] ~ a[4] 생성
b = [0] * 5 # b[1] ~ b[4] 생성
grape_t1 = [] #t1 그래프에 넣을 리스트
grape_t2 = [] #t2 그래프에 넣을 리스트
while True:
    '''전진과 400 넘으면 회전 600 넘으면 회전 1000 넘으면 회전 1200 넘으면 중단출'''
    a1 = r.randint(140,170)
    a2 = r.randint(140,170)
    a[0] +=a1
    a[1] +=a1
    a[3] +=a1
    b[0] +=a2
    b[1] +=a2
    b[3] +=a2
    grape_t1.append(a1) #랜덤 값 grape_t1 list 에 넣기
    grape_t2.append(a2) #랜덤 값 grape_t2 list 에 넣기
    if a[0] >= 400 and 0 < a[1] < 600 :
        t1.fd(a1-(a[0]-400))
        t1.right(90)
        t1.fd(a[0]-400)
        a[0] = 0
    elif a[1] >= 600:
        t1.fd(a1-(a[1]-600))
        t1.right(90)
        t1.fd(a[1]-600)
        a[1] = - 1000
    elif a[3] >= 1000 and a[4] == 0:
        t1.fd(a1-(a[3]-1000))
        t1.right(90)
        t1.fd(a[3]-1000)
        a[4] = - 1000
    else:
        t1.fd(a1)

    if b[0] >= 400 and 0 < b[1] < 600 :
        t2.fd(a2-(b[0]-400))
        t2.right(90)
        t2.fd(b[0]-400)
        b[0] = 0
    elif b[1] >= 600:
        t2.fd(a2-(b[1]-600))
        t2.right(90)
        t2.fd(b[1]-600)
        b[1] = -1000
    elif b[3] >= 1000 and b[4] == 0:
        t2.fd(a2-(b[3]-1000))
        t2.right(90)
        t2.fd(b[3]-1000)
        b[4] = -1000
    else:
        t2.fd(a2)
    if a[3] >=1200 or b[3] >=1200:
        if a[3] > b[3] :
            t1.write(">> 빨간 거북이가 이겼습니다!")
        elif a[3] == b[3] :
            t1.write(">> 무승부입니다!")
        else :
            t2.write(">> 파랑 거북이가 이겼습니다!")
        break
t.go(-510,-150) # t1 그래프 검정선 그리기
t.width(3)
t.right(90)
t.fd(150)
t.left(90)
t.fd(340)
t1.fd
t1.go(-500,-300)
for d in grape_t1:
    '''t1 막대 그래프 그리기'''
    t1.bar(d)
t1.go(-430,-350)
t1.write("< 빨간 거북이가 달린 거리 > ", font = ('TImes New Roman',10,'bold')) #t1 달린거리 
t1.go(-130,-200)
t1.write("> 빨간 거북이가 달린 총 거리 \n "+ " = " +str(a[3]) + "\n" ,font = ('TImes New Roman',10,'bold')) #t1 총 달린거리 
t2.go(100,-300)
t.go(90,-150) # t2 그래프 검정선 그리기
t.right(90)
t.fd(150)
t.left(90)
t.fd(340)
t.ht()
for d in grape_t2:
    '''t2 막대 그래프 그리기'''
    t2.bar(d)
t2.go(170,-350)
t2.write("< 파란 거북이가 달린 거리 > ",font = ('TImes New Roman',10,'bold')) #t2 달린거리 
t2.go(470,-200)
t2.write("> 파란 거북이가 달린 총 거리 \n "+ " = " +str(b[3]) + "\n" ,font = ('TImes New Roman',10,'bold')) #t2 총 달린거리 

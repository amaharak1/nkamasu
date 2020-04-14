import random
nHP=20#んかいの体力
mHP=20#増田の体力
#んかいの行動
def inazuma():
    global mHP
    mHP=mHP-4
    print("んかいは稲妻を放った！増田に4ダメージ！")

def syokusyu():
    global mHP
    mHP=mHP-3
    print("んかいが触手をくねらせて襲い掛かる！増田に3ダメージ！")

def hayakuti():
    global mHP
    mHP=mHP-2
    print("んかいは早口でアイマスについて語りだした。増田に2ダメージ！")

def sikoru():
    global nHP
    nHP=nHP+4
    print("んかいは純愛モノでシコっている。んかいの体力が4回復した。")

#増田の行動
def kanozyo():
    global nHP
    nHP=nHP-7
    print("増田が彼女ネタでマウントをとっていく……")
    print("クリティカル！んかいに7ダメージ！")

def kobusi():
    global nHP
    nHP=nHP-4
    print("増田の鍛えた拳が炸裂！んかいに4ダメージ！")

def inu():
    global nHP
    nHP=nHP-3
    print("増田は犬を召喚した！んかいに3ダメージ！")

def kora():
    print("増田はんかいのコラ画像を作った。しかし誰も反応しなかった。")

#本文
print("んかいHP：", nHP, "増田HP：", mHP)
while(nHP>0 and mHP>0):#どちらかが死ぬまで繰り返し
    r=[1,2,3,4]
    c=random.choices(r, weights=[1,1,1,1])#1234をそれぞれのdefと連結させてランダムに選ばせている
    if(c==[1]):
        inazuma()
    if(c==[2]):
        syokusyu()
    if(c==[3]):
        hayakuti()
    if(c==[4]):
        sikoru()
    
    r=[1,2,3,4]
    c=random.choices(r, weights=[1,4,3,2])
    if(c==[1]):
        kanozyo()
    if(c==[2]):
        kobusi()
    if(c==[3]):
        inu()
    if(c==[4]):
        kora()
    print("んかいHP：", nHP, "増田HP：", mHP)

if(nHP>0):
    print("増田は死んだ。ぐえー死んだンゴ")
    print("んかいの勝ち！")
elif(mHP>0):
    print("んかいは死んだ。ぐえー死んだンゴ")
    print("増田の勝ち！")
else:
    print("激しい戦いの末、限界を迎えたんかいと増田は重なり合うようにして倒れこんだ。")
    print("互いを抱き合うようにして絶命した二人の表情はどこか幸せそうであった。")
    print("True end.")
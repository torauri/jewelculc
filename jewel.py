import numpy as np

#60ガチャによる節約を行った場合の必要jewel数を計算
def jewel_culc(time,have_jewel):

    return 75000 - have_jewel - time*190

#必要ジュエルに対して必要金額を計算
def money_culc(need_jewel):
    #ジュエルの個数とその値段
    jewel_price =np.array([[8400,9800],[4200,5000],[2650,3200],[1300,1600],[760,960],[360,480],[60,120]],dtype=np.int32)
    need_money=0
    for i in jewel_price:
        need_money += i[1] * (need_jewel//i[0])
        need_jewel = need_jewel % i[1]

    #半端なジュエルが出た場合Aセットを追加購入するためその分金額を増やす
    if(need_jewel!=0):
        need_money += 120

    return need_money


def main():
    print ("ガチャ開催期間(何回60ガチャを回せるか)")
    time = eval(input('>>'))
    print ("持っているjewel")
    have_jewel = eval(input('>>'))

    need_jewel = jewel_culc(time,have_jewel)
    print ("必要jewel:"+str(need_jewel)+"個")

    need_money = money_culc(need_jewel)
    print("必要金額:" + str(need_money) + "円")

if __name__ == "__main__":
        main()

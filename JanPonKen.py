#   1 2 3 points
#  _____________
#   0 1 2 : g(0)
#   3 4 5 : c(1)
#   6 7 8 : p(2)
#   hand = int(i/3)
#   point = (i%3)+1
#  0 win to 1 win to 2 win to 0
#  (myH+1)%3 == oH → I Win!
#  myH == (oH+1)%3 → I lose...

# (1,3)/(2,6)/.../myPoint/oppPoint/w or l or d
f = open('result.txt', 'w')
myCards = [True for i in range(9)]
oppCards = [True for i in range(9)]
now = [1 for i in range(9)]
def main():
    for x in range(3):
        for y in range(9):
            JanPonKen(1, x, y, [True for i in range(9)], [True for i in range(9)], 0, 0, "")


def JanPonKen(times, myH, oppH, myHH, oppHH, mP, oP, s):
    if(times == 9):
        # 終了時: じゃんけんをしてから勝敗判定
        result = JanKen(myH, oppH);
        _s = s+str(myH)+str(oppH)+"/" + str(mP+result[0]) + "_" + str(oP+result[1])
        if(mP+result[0]>oP+result[1]):
            _s += "w"
        elif(mP+result[0]<oP+result[1]):
            _s += "l"
        else:
            _s += "d"
        saveToFile(_s)
    else:
        # じゃんけん: myHH[myH], oppHH[opH] を False(使った) にしてからじゃんけんをする。 次の手をfor分で出しつつ関数を投げる
        _myHH = [myHH[i] for i in range(9)]
        _oppHH = [oppHH[i] for i in range(9)]
        _myHH[myH] = False
        _oppHH[oppH] = False
        result = JanKen(myH, oppH);
        _s = s+str(myH)+str(oppH)
        for m in range(9):
            if _myHH[m]:
                for o in range(9):
                    if _oppHH[o]:
                        JanPonKen(times+1, m, o, _myHH, _oppHH, mP+result[0], oP+result[1], _s)




def JanKen(mI, oI):
    if ((int(mI)/3)+1)%3 == int(oI/3):
        return ((mI%3)+1, 0)
    elif int(mI/3) == int(oI/3):
        return (0, 0)
    else:
        return (0, (oI%3)+1)

def saveToFile(s):
    f.write(s)
    f.write("\n")


if __name__ == '__main__':
    main()

    f.close()

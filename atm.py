def request_money(request, money):
    if request <= money:
        if request <= 0:
            print "you can't request 0 or negative numbers"
        else:
            while request > 0:
                if request >= 100:
                    print "give " + str(100)
                    request -= 100
                elif request < 100 and request >= 50:
                    print "give " + str(50)
                    request -= 50
                elif request < 50 and request >= 10:
                    print "give " + str(10)
                    request -= 10
                elif request < 10 and request >= 5:
                    print "give " + str(5)
                    request -= 5
                else:
                    print "give " + str(request)
                    request -= request

    else:
        print "Dude, you don't have this amount of money!!!"


if __name__ == '__main__':
    money = 500
    request = 277

    request_money(request, money)


#
#
#
#                            ''' hello ''' {^_^}



count=0

while True:

    ip1=int(input("IP Address=>"))
    ip2=int(input("IP Address=>"))
    ip3=int(input("IP Address=>"))
    ip4=int(input("IP Address=>"))

    print(f"IP Address {ip1}.{ip2}.{ip3}.{ip4}")




    #print(g)

    y = int(input("CIRD=>"))

    count = count + 1


    def cird(x):
        user = x - 24
        network = 2 ** user
        print("network=", network)

        host=24+user
        hosto=32-host
        hostou=2**hosto-2

        print("Host=", hostou)

        x1=128
        x2=64
        x3=32
        x4=16
        x5=8
        x6=4
        x7=2
        x8=1

        if user==1:
            yo=x1
            block1=256-yo
            print("Block Size=", block1)

            count = 0

            for i in range(6):
                count = count + block1
                print(f"Broadcast={ip1}.{ip2}.{ip3}.{count - 1}")
                #print()

            print("Block Size=", block1)

        elif user==2:
            yo2=x2+x1
            block2=256-yo2
            count = 0

            for i in range(6):
                count = count + block2
                print(f"Broadcast={ip1}.{ip2}.{ip3}.{count - 1}")
                #print()

            print("Block Size=", block2)
        elif user==3:
            yo3=x3+x2+x1
            block3=256-yo3

            bro = ip4 + block3
            r = ip4 + 1
            b = bro - 2

            count = 0

            for i in range(6):
                count = count + block3
                print(f"Broadcast={ip1}.{ip2}.{ip3}.{count-1}")
                #print()

            print("Block Size=", block3)

        elif user==4:
            yo4=x4+x3+x2+x1
            block4=256-yo4
            print("Block Size=", block4)

            count = 0

            for i in range(6):
                count = count + block4
                print(f"Broadcast={ip1}.{ip2}.{ip3}.{count - 1}")
                #print()

            print("Block Size=", block4)

        elif user==5:
            yo5=x5+x4+x3+x2+x1
            block5=256-yo5
            print("Block Size=", block5)

            count = 0

            for i in range(6):
                count = count + block5
                print(f"Broadcast={ip1}.{ip2}.{ip3}.{count - 1}")
                #print()

            print("Block Size=", block5)




        elif user==6:
            yo6=x6+x5+x4+x3+x2+x1
            block6=256-yo6


            print("Block Size=", block6)

            count = 0

            for i in range(6):
                count = count + block6
                print(f"Broadcast={ip1}.{ip2}.{ip3}.{count - 1}")
                #print()

            print("Block Size=", block6)

        elif user==7:
            yo7=x7+x6+x5+x4+x3+x2+x1
            block7=256-yo7

            print("Block Size=", block7)

            count = 0

            for i in range(6):
                count = count + block7
                print(f"Broadcast={ip1}.{ip2}.{ip3}.{count - 1}")

            print("Block Size=", block7)

        elif user==8:
            yo8=x8+x7+x6+x5+x4+x3+x2+x1
            block8=256-yo8

            count = 0

            for i in range(6):
                count = count + block8
                print(f"Broadcast={ip1}.{ip2}.{ip3}.{count - 1}")
                #print()



            print("Block Size=", block8)

            print(f"Broadcast={ip1}.{ip2}.{ip3}.{count - 1}")
            #print()




        else:
            print("invite input please try again {*_*}")






    cird(y)



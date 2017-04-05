for i in xrange (2**31-1):

    name = raw_input("What is your name? \n")
    if int(name) == int :
        print "error"
    print
    def user_name(user):
        print "Welcome to our company ",user
        print
        print user,",If your computer costs 800 $ or more than 800 $,you will get free anti-virus program "
    user_name(name)
    print
    #
    try:
        how_many_computer = int(input ("How many computers do you want ?\n"))
    except:
        print "Please enter integer value"
        continue
    if how_many_computer == 1:
        print "Please go next step"
    elif how_many_computer > 1:
        print "We will calculate your fee later.Please go next step"
    print
    #These kods (from line 9 to 13) will be used bulk purchase

    storage_select = raw_input("Please write storage device:ssd or hdd? \n")
    if storage_select!="ssd" and storage_select!= "hdd":
        print "Please enter true characters"
        continue

    hdd = 200
    ssd = 300
    def storage_price (fee):
        if storage_select == "hdd":
            fee = 200
            print "You will pay",fee,"$ for",storage_select

        elif storage_select == "ssd":
            fee = 300
            print "You will pay ",fee," $ for ",storage_select
        return fee
    x = storage_price(storage_select)
    print
    try:
        ram_selec = int(input("Please write amount of RAM (enter a numerical value): \n"))
    except:
        print "Please enter integer value"
        continue
    each_ram = 25
    cost = each_ram * ram_selec

    def ram_price (fee):
        print "You will pay ",fee, "$ for ",ram_selec,"RAM"
        return fee
    y = ram_price(cost)
    print


    print "Finally you are going to choose CPU and GPU.\n" \
          "We have a special offer for you.\n" \
          "If you select Intel CPU,then 5% discount on Intel GPU\n" \
          "If you select AMD CPU,then 10% discount on ATI GPU"
    print
    #
    gpu_intel_price = 100
    discount_intel = 5.0/100
    def cpu_intel():
        cpu_intel = 320.0
        return cpu_intel


    def gpu_intel ():
        if cpu_select == "intel":
            cost_intel = gpu_intel_discount()
        elif cpu_select == "amd"  :
            cost_intel = gpu_intel_price
        elif cpu_select == "ibm":
            cost_intel = gpu_intel_price
        return cost_intel


    def gpu_intel_discount ():
        gpu_intel_discount = gpu_intel_price -(gpu_intel_price * discount_intel)
        return gpu_intel_discount
    #These kods (from line 48 to 69) was used for functions of intel cpu and intel gpu and constant numbers defined all kods above


    #
    gpu_amd = 145.0
    discount_amd = 10.0/100
    def cpu_amd ():
        cpu_amd = 300.0
        return cpu_amd


    def gpu_ati ():
        if cpu_select == "amd":
            cost_ati = gpu_ati_discount()
        elif cpu_select == "intel":
            cost_ati = gpu_amd
        elif cpu_select == "ibm":
            cost_ati = gpu_amd
        return cost_ati


    def gpu_ati_discount ():
        gpu_ati_discount = gpu_amd - (gpu_amd * discount_amd)
        return gpu_ati_discount

    #These kods (from line 72 to 94) was used for functions of amd cpu and ati gpu and constant numbers defined all kods above

    def cpu_ibm ():
        cpu_ibm = 290.0
        return cpu_ibm


    def gpu_nvidia ():
        gpu_nvidia = 150
        return gpu_nvidia


    cpu_select = raw_input("Please write CPU :intel,amd,ibm\n")
    if cpu_select != "intel" and cpu_select!="amd" and cpu_select!="ibm":
        print "Please enter true characters"
        continue

    def cpu_price (fee):
        if cpu_select == "intel":
            fee = cpu_intel()
            print "You will pay ",fee,"$ for",cpu_select
        elif cpu_select == "amd":
            fee = cpu_amd ()
            print "You will pay ",fee,"$ for",cpu_select
        elif cpu_select == "ibm":
            fee = cpu_ibm ()
            print "You will pay ",fee,"$ for",cpu_select
        return fee
    z = cpu_price(cpu_select)
    print

    gpu_select =raw_input("Please write GPU : Intel,ati,nvidia\n")
    if gpu_select != "Intel" and gpu_select != "ati" and gpu_select != "nvidia":
        print "Please enter true characters"
        continue

    def gpu_price ():
        if gpu_select == "Intel":
            price = gpu_intel()
            print "You will pay ",price,"$ for gpu"
        elif gpu_select == "ati":
            price = gpu_ati()
            print "You will pay ",price, "$ for gpu"
        elif gpu_select == "nvidia":
            price = gpu_nvidia()
            print "You will pay ",price,"$ for gpu"
        return price
    q = gpu_price()
    print

    def totally_price():
        total_price = q + z + y + x
        return total_price
    print "Totally one computer you will pay ",totally_price(),"$"
    print

    if totally_price() >= 800 :
        print "Congratulations!!! You have an free anti-virus program"
    print

    def bulk_purchase ():
        sum=0
        for i in range(how_many_computer):
            sum = sum + totally_price()
        return sum

    print "For",how_many_computer,"computers you will pay",bulk_purchase(),"$"
    print
    print "If you want to exit this program please write below 'exit'.\n" \
          "If you do not,please click enter"
    exit_program = raw_input()
    if exit_program == "exit":
        print "See you later"
        exit()

#Mehmet Ozan Guven
#Student ID:220201036
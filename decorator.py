def dec1(function):
    def executor():
        print("Execting now")
        function()
        print('Executed')
    return executor


@dec1
def IPaddress():
    print("IP adress is 127.0.0.1")

IPaddress()

@dec1
def IPaddress2():
    print("IP adress is 127.0.0.2")

IPaddress2()
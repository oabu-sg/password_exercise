def IsCommon(Pass):
    with open('Passtext.txt') as File:
        if Pass in File.read():
            return True
        else:
            return False


if IsCommon("password"):
    print("Password is weak")
else:
    print("Its okay")

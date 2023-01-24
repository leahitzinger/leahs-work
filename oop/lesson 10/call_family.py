from family import Family
from famile_members import FamilyMembers


def main():
    member1=FamilyMembers('itzinger',21,True)
    member2=FamilyMembers('cohen',25,True)
    members=[member1,member2]
    my_family=Family('pines', 'Israel', 'fun',members)

    print(my_family)
main()


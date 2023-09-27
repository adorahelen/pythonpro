import random
import pdb
import mymodule

Hero_HP = random.randint(50, 101)
trol_HP = random.randint(50, 101)

Hero_att = random.randint(-10, 21)
trol_att = random.randint(-10, 21)

while Hero_HP >=0 or trol_HP >= 0:
     Hero_HP  =  Hero_HP - trol_att
     trol_HP  =  trol_HP - Hero_att

     

     damage_string = "hero(HP: %d, attck: %d)"  %(Hero_HP, Hero_att)

     default_string = "hero HP: %d, monster HP: %d" %(Hero_HP, trol_HP) 
     print(damage_string)


     damage2_string = "monster(HP: %d, attck: %d)" %(trol_HP, trol_att)

     if Hero_att > 0 and trol_att > 0  :
        print (damage_string + "success"+ " <-> " + damage2_string + "success")

     elif Hero_att > 0 and trol_att < 0 :
        print (damage_string + "success" + " <-> " + damage2_string + "fail")

     elif Hero_att < 0 and trol_att > 0 :
        print (damage_string + "fail"  + " <->" +  damage2_string + "success")

     elif Hero_att < 0 and trol_att < 0 :
        print (damage_sting + "fail" + "<->"  + damage2_string + "fail")

print("--------------------------------------------------------")
print("")
print("")

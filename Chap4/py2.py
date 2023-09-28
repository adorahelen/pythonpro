import random

Hero_HP = random.randint(50, 101)
trol_HP = random.randint(50, 101)
count = 0

print("Battle Start:")
default_string = "hero HP: %d, monster HP: %d" %(Hero_HP, trol_HP)
print(default_string)

while Hero_HP >0 and trol_HP > 0:


    trol_att = random.randint(-10, 21)
    Hero_att = random.randint(-10, 21)

    Hero_HP  =  Hero_HP - trol_att
    trol_HP  =  trol_HP - Hero_att
    count +=1

    damage_string = "hero(HP: %d, attck: %d)"  %(Hero_HP, Hero_att)

    damage2_string = "monster(HP: %d, attck: %d)" %(trol_HP, trol_att)

    if Hero_att > 0 and trol_att > 0  :
     print (damage_string + "success"+ " <-> " + damage2_string + "success")

    elif Hero_att > 0 and trol_att < 0 :
     print (damage_string + "success" + " <-> " + damage2_string + "fail")

    elif Hero_att < 0 and trol_att > 0 :
     print (damage_string + "fail"  + " <->" +  damage2_string + "success")

    elif Hero_att < 0 and trol_att < 0 :
     print (damage_string + "fail" + "<->"  + damage2_string + "fail")

print("--------------------------------------------------------")

end = "Total phase %d," %(count)
print(end)

if Hero_HP <= 0 :
  print("Troll WIN")
elif trol_HP <=0 :
  print("HERO WIN")

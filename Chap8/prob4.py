import pickle, shelve
# 모듈을 사용하여 객체를 직렬화

print ("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]
# 리스트 생성 후 밑에 이진 파일로 저장
f = open ("pickles1.dat", "wb")

pickle.dump (variety, f)
pickle.dump (shape, f)
pickle.dump (brand, f)
f.close ()
# 덤프를 사용해 리스트를 파일에 쓴다. (상기 이진 파일)

# 파일을 열어 다시 리스트를 읽어온다.
# 함수를 사용하여 파일에서 객체를 읽어온다.

print ("\nUnpickling lists.")
f = open ("pickles1.dat", "rb")
variety = pickle.load (f)
shape = pickle.load (f)
brand = pickle.load (f)

print (variety)
print (shape)
print (brand)

f.close ()

## Shele 를 사용하여 데이터를 저장한다.
## 이때 shelve는 딕셔너리처럼 동작하여 리스트에 랜덤 액세스를 제공한다. 

print ("Shelving Lists")



shelf = shelve.open ("pickles2.dat")

shelf["variety"] = ["sweet", "hot", "dill"]
shelf["shape"] = ["whole", "spear", "chip"]
shelf["brand"] = ["Claussen", "Heinz", "Vlassic"]

shelf.sync () 


print("\nRetrieving lists from a shelved file:\t")
print ("variety - ", shelf["variety"])
print ("shape - ", shelf["shape"])
print ("brand - ", shelf["brand"])

shelf.close ()

input ("\nPress Enter key to exit")

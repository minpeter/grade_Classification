from func import *

exit = True

total = []

print("⚠️  종료시 0을 입력하세요.")

while exit:
  answer = input("학번과 이름을 입력하세요. (학년 반 번호 이름): ")
  if answer == "0":
    print("⛔ 입력을 종료합니다.")
    exit = False
  
  else:
    info_list = answer.split(" ")
    try:
      info = {
          "grade": "",
          "class": "",
          "number": "",
          "name": "",
      }
      info["grade"] = int(info_list[0])
      info["class"] = int(info_list[1])
      info["number"] = int(info_list[2])
      info["name"] = info_list[3]
      total.append(info)
    except:
      print("⚠️ 입력이 잘못되었습니다.")
      continue

    print("✅ 입력이 정상적으로 처리되었습니다.")


one = []
two = []
three = []
etc = []

for t in total:
  if t["grade"] == 1:
    one.append(t)
  elif t["grade"] == 2:
    two.append(t)
  elif t["grade"] == 3:
    three.append(t)
  else:
    etc.append(t)

oneMax = checkMax(one)
twoMax = checkMax(two)
threeMax = checkMax(three)
etcMax = checkMax(etc)

onelist = classification(one, oneMax)
twolist = classification(two, twoMax)
threelist = classification(three, threeMax)
etclist = classification(etc, etcMax)

print("🧩 결과 출력")

print("==== 1학년 ====")
print_list(onelist, oneMax)

print("==== 2학년 ====")
print_list(twolist, twoMax)

print("==== 3학년 ====")
print_list(threelist, threeMax)

if etcMax != 0:
  print("==== 기타 ====")
  print_list(etclist, etcMax)


input("아무키나 누르면 종료된다! made by minpeter")
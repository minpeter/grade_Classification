def checkMax(list):
  max=0
  for l in list:
    if l["class"] > max:
      max = l["class"]
  return max

def classification(list, max):
  return_list = [[] for i in range(max)]

  for l in list:
    for i in range(len(return_list)):
      if l["class"] == i+1:
        return_list[i].append(l)
  return return_list

def print_list(list, max):
  for i in range(max):
    if len(list[i]) == 0:
      continue
    else:
      print(f"{i+1}반: 총 {len(list[i])}명")
      for l in list[i]:
        print(f"{l['number']}번 {l['name']}")
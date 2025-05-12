# 리스트
numbers = [1,2,3,4,5,6]
# count(x):리스트에 포함된 요소 x의 개수
print(numbers.count(1)) # 1

numbers1 = [2,3,1,3,4,6,5]
numbers1.sort()
print(numbers1)
#sort():리스트의 요소를 순서대로 정렬
strings = ['aa','cc','hh','bb']
strings.sort()
print(strings) # aa, bb, cc, hh
#reverse(): 리스트를 거꾸로 뒤집기
numbers.reverse()
print(numbers) #6,5,4,3,2,1
# index(요소):리스트에 속한 요소의 인덱스를 알려줌
print(numbers.index(6)) # 첫번째 0
#insert(인덱스, 삽입할 값): 리스트의 인덱스 i 위치에 새로운 요소 삽입
numbers.insert(1, 'hii')
print(numbers)
#remove(요소):리스트에서 첫 번째로 나오는 해당요소를 삭제
numbers.remove(1)
print(numbers)
#pop(인덱스):리스트에 인덱스에 해당하는 요소를 돌려주고 리스트에서 삭제
poped1 = numbers.pop(2)
print(poped1)#pop한 요소
print(numbers)

poped2 = numbers.pop(3)
print(poped2) #pop한 요소
print(numbers)

favorite_food = ['ramen', 'kimchi', 'cola']
poped3 = favorite_food.pop(1)
print(poped3)
print(favorite_food) #['ramem','cola']

# 리스트 연습 33
color = ['red', 'orange', 'yellow', 'green']
print(color.count('red')) # 1 문자열 리스트의 'red'값이 '몇개가 있는지' 알려준다.
color.sort() 
print(color) # 2 문자열 알파벳 순서대로 '정렬한다'.
color.reverse()
print(color) # 3 문자열 알파벳을 '뒤집는다'.
print(color.index('red')) # 4 문자의 '인덱스'를 알려준다.
color.insert(2, 'pink')
print(color) # 5 '인덱스 + 값' 를 사용해 원하는 위치에 값을 추가한다.
color.remove('red') # 8 '값' 첫번째의 값을 제거한다.
print(color)
color.pop(2) # 7 '인덱스'에 포함하는 '값을 돌려주고 제거'한다.
print(color)
color.extend(['purple', 'blue']) # 8 color '리스트에 리스트를 추가'한다.
print(color)

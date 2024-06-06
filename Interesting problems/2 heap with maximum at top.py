"""
Дан список чисел, записанных через пробел. Реализуйте кучу с максимумом в вершине для этого списка.

Далее программе на вход будут поступать команды:

insert <число> – добавить число в кучу;
pop – удалить вершину и напечатать ее;
end – завершить выполнение программы.
Ввод:

nums – список чисел записанных через пробел
Список команд.
Вывод:

Результаты работы программы

Sample Input 1:
1 5 2 6 3 7 4 8
insert 20
pop
insert 0
pop
insert 4
pop
end

Sample Output 1:
20
8
7


Sample Input 2:
100 101 102
insert 0
pop
insert 10
pop
insert 20
pop
insert 103
pop
insert 104
pop
insert 105
pop
pop
pop
pop
end

Sample Output 2:
102
101
100
103
104
105
20
10
0


Sample Input 3:
100
pop
end

Sample Output 3:
100
"""

from heapq import heapify, heappush, heappop

heap = []
heapify(heap)

numbers = list(map(lambda x: -int(x), input().split()))

for i in numbers:
    heappush(heap, i)
    
message = 'start'
while message != 'end':
    message = input()
    if message == 'pop':
        print(-heappop(heap))
    elif message[:6] == 'insert':
        heappush(heap, -int(message[7:]))
    
# print(heap)

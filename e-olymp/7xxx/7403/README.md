# [Включить лампу](https://www.e-olymp.com/en/problems/7403)

Степан разрабатывает электронную схему на прямоугольной сетке размером n * m. Всего n * m квадратных плиток. Два (из четырёх) противоположных угла каждой плитки соединены проводом.

Источник питания подсоединен к левому верхнему углу сетки, лампа - к правому нижнему. Для того чтобы включить лампу можно повернуть любую плитку на 90 градусов в обоих направлениях.

На изображении лампа выключена. Если повернуть любую плитку во второй колонке справа, то лампа включится.

![prb7403](1429979277.png)

Напишите программу, которая найдет минимальное количество плиток, которое надо перевернуть для того, чтобы включить лампу.

## Входные данные

Первая строка содержит два целых числа n и m (1 ≤ n, m ≤ 500) - размеры сетки. Далее следуют n строк по m символов - \ или /, характеризующие направление провода на данной плитке.

## Выходные данные

Вывести ответ к задаче, или сообщение "NO SOLUTION", если включить лампу невозможно.

_Time limit 1 second_

_Memory limit 122.17 MiB_

## Input example #1
```
3 5
\\/\\
\\///
/\\\\
```

## Output example #1
```
1
```
# **Пакет, решающий задачу "Про ПСП"**

<img height="100" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Parentesi_Tonde.svg/1200px-Parentesi_Tonde.svg.png" width="50"/>

Для понимания ПСП прочитайте
[эту статью](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D0%B1%D0%BE%D1%87%D0%BD%D0%B0%D1%8F_%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C)

## **Описание задачи**

ПСП – правильная скобочная последовательность – последовательность из открывающих «(« и закрывающих «)» круглых скобок,
удовлетворяющая следующему набору правил:
- «()» есть правильная скобочная последовательность;
- если s – правильная скобочная последовательность, то «(» + s + «)» – правильная скобочная последовательность;
- если s и t – правильные скобочные последовательности, то s + t – правильная скобочная последовательность.
Проверить последовательность скобочек из N символов (где открывающих и закрывающих скобок ровно по N // 2) на
соответствие ПСП достаточно просто за один проход по строке. Однако более интересной задачей может стать нахождение
количества изменений в строке из скобок, после чего строка становится подобна ПСП. За один раз мы можем изменить
строку одним из способов: ровно одну скобку можно передвинуть в конец или в начало строки.

Функция```is_cbs``` проверяет является ли полученная строка ПСП
Функция```need_to_move``` находить количество изменений, которые нужно совершить, чтобы получить ПСП из полученной строки


### **Пример 1**
 «()()», «(())()», «(())» и «()» являются правильными скобочными последовательностями,
а «)(», «()(» и «)))» – нет.

### **Пример 2**
в строке «())()()(» достаточно последний символ перенести в начало строки.




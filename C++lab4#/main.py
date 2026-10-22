import operator as oper

comparators = {
    "==": oper.eq,
    "!=": oper.ne, 
    ">":  oper.gt,
    "<":  oper.lt,
    ">=": oper.ge,
    "<=": oper.le,
}

# print([int(num) for num in input("Введите числа через пробел:").split()])
def User_Int_List_Input () -> list:
    numData:list = input("Введите числа через пробел:").split()
    return [int(num) for num in numData]

def main() -> int:

    a:list = User_Int_List_Input()
    print(a)

    print("Выберите функцию:")
    print("1.сумму чисел",
        "2.общее количество чисел",
        "3.количество чисел, равных заданному",
        "4.количество чисел, удовлетворяющих условию, например, 'больше, чем n»'",
        "5.заменить все нули средним арифметическим (взять целую часть)",
        "6.добавить к каждому элементу вектора сумму всех чисел из заданного интервала этого же вектора (не числовой оси, а вектора)",
        "7.заменить все числа, модуль которых есть четное число, на разность максимального и минимального элемента этого вектора",
        "8.удалить из последовательности все равные по модулю числа, кроме первого из них.", sep=";\n", end="\n\n")


    match int(input()):
        case 1:
            print(sum(a))

        case 2:
            print(len(a))

        case 3:
            print(a.count(int(input("Введите число для подсчета количества вхождений в список: "))))

        case 4:
            userNum:int = int(input("Выберете число для сравнения: "))
            print("Выберете одну из след. операций ==, !=, >, <, >=, <= для сравнения с числом", userNum, ": ", end='')
            userCmp:str = input()
            if userCmp in comparators:
                counter:int = 0
                for elem in a:
                    if comparators[userCmp](userNum, elem):
                        counter += 1
                print(counter)
            else:
                print("Использован неизвестный компаратор!")

        case 5:
            average:int = sum(a) // len(a)
            for i, item in enumerate(a):
                if item == 0:
                    a[i] = average
            print(a)

        case 6:
            print("Введите крайние индексы списка")
            firstInd:int = int(input("Введите индекс левого края:"))
            lastInd:int = int(input("Введите индекс правого края:"))

            partListSum:int = sum(a[firstInd : lastInd + 1])
            
            for i in range(len(a)):
                a[i] += partListSum
            print(a)

        case 7:
            diff:int = max(a) - min(a)
            for i, item in enumerate(a):
                if (item % 2) == 0:
                    a[i] = diff
            print(a)

        case 8:
            noDuplicate:set = set()
            i:int = 0
            lenght:int = len(a)
            while(i<lenght):
                if abs(a[i]) not in noDuplicate:
                    noDuplicate.add(abs(a[i]))
                    i += 1
                else:
                    a.pop(i)
                    lenght -= 1
            print(a)

        case _:
            print("Данная функция отсутствует!")

    print("end")

    return 0


def main2() -> int:
    import os
    print("Текущая папка:", os.getcwd())
    with open(r"d:\myPython\C++lab4#\data.txt", 'rt', encoding="utf-8") as file:
        text:list = file.read().split()
        print(sorted(text))
        searchSymbol:str = input("Введите символ для поиска слов по первой букве: ")
        for word in text:
            if word[0] == searchSymbol:
                print(word)
        searchSymbol = input("Введите символ для удаления слов по первой букве: ")
        for i, word in enumerate(text):
             if word[0] == searchSymbol:
                text.pop(i)
        print(text)

    return 0


def main3() -> int:




    return 0


match int(input("выберите раздел заданий (впишите от 1 до 3)")):
    case 1:
        main()

    case 2:
        main2()

    case 3:
        main3()
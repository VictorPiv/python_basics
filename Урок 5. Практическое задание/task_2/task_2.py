"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("2.txt", "r") as note:
    i = 1
    for fline in note:
        print(f'В {i}-й строке слов: {len(fline.split())}')
        i += 1

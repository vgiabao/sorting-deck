#!/usr/bin/env python3
from argparse import ArgumentParser
from gui import mainly

'''
function nay dung de tao ra
'''


def parser():
    parser = ArgumentParser(prog='sort', usage='sort.py \
[-h] [--algo ALGO] [--gui] N [N ...]')
    parser.add_argument('number', metavar='N', nargs='+', help='an integer\
for the list to sort', type=int)
    parser.add_argument('--algo', metavar='ALGO', help='specify \
which algorithm to use for sorting among [bubble|insert|quick\
|merge]', default='bubble', choices=['bubble', 'insert', 'quick', 'merge'])
    parser.add_argument('--gui', help='visualise the \
algorithm in GUI mode', action='store_true')
    return parser.parse_args()


'''
function nay dung de chay ham bubble sort:
    1: chay frame tu cuoi array trong luc do chay 1 cai check tu 0 den do'
    2: neu ma phan sau lon hon phan tu truoc thi doi cho
    3: frame - 1 va khong xet toi nua vi no da lon nhat
    truong hop tot nhat: day da sap xep
    truong hop xau nhat: day ban dau co thu tu nguoc
'''


def bubble_sort(array):
    frame = len(array) - 1
    list_of_move = []
    detailed_list = []
    while frame != -1:
        for index in range(frame):
            detailed_list.append([index, index + 1])
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                list_of_move.append([index, index + 1])
                print(*array)
        frame -= 1
    return list_of_move, detailed_list


'''
sap xep chen:
    1: chay tu phan tu checking 1 den cuoi', neu phan tu dang chay be hon max
sau no thi bat dau chay nhu sau:
    chay mot bien tu vi tri checking -1 den vi tri 0, de tim vi tri de chen
    chen bang cach vong lap doi cho vi tri checking voi vi tri checking -1
'''


def insertion_sort(array):
    checking_list = []
    list_of_move = []
    detailed_list = []
    limit = 0
    for index in range(1, (len(array))):
        j = index
        list_down = []
        if array[index] < max(array[:index]):
            while j > 0:
                if array[j - 1] > array[j]:
                    array[j - 1], array[j] = array[j], array[j - 1]
                    list_down.append(j - 1)
                j -= 1
            print(*array)
            limit = min(list_down)
            list_of_move.append([index, limit])
        for research in range(index, -1, -1):
            if research >= limit:
                detailed_list.append([index, research])
    return list_of_move, detailed_list


'''
quick sort:
loi dung ham partition de xap sep phan tu 2 ben trai va phai
    partition:
    1:chon pivot la phan tu cuoi
    2: chay phia ben phai tu 0 den cuoi, neu phan tu phai ma nho hon hoac bang
    pivot

'''


def partition(array, start, end):
    a = 0
    left = start
    pivot = array[end]
    for right in range(start, end):
        if array[right] <= pivot:
            array[right], array[left] = array[left], array[right]
            left += 1
    array[left], array[end] = array[end], array[left]
    print('P:', pivot)
    print(*array)
    return left


def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start < end:
        new_limit = partition(array, start, end)
        quick_sort(array, 0, new_limit - 1)
        quick_sort(array, new_limit + 1, end)


def merge(list1, list2):
    sorted_list = []
    while list1 and list2:
        if list1[0] < list2[0]:
            sorted_list.append(list1.pop(0))
        else:
            sorted_list.append(list2.pop(0))
    sorted_list += list1 + list2
    print(*sorted_list)
    return sorted_list


def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        return merge(merge_sort(array[:len(array)//2]),
                     merge_sort(array[len(array) // 2:]))


def checking_without_gui(args):
    if args.algo == 'bubble':
        bubble_sort(args.number)
    elif args.algo == 'insert':
        insertion_sort(args.number)
    elif args.algo == 'quick':
        quick_sort(args.number)
    elif args.algo == 'merge':
        merge_sort(args.number)


def main():
    args = parser()
    first = tuple(args.number)
    if args.gui and len(args.number) > 15:
        print('Input too large')
    elif args.gui and len(args.number) <= 15:
        if args.algo == 'bubble':
            kindly = 'bubble'
            list_of_move, detailed_list = bubble_sort(args.number)
            mainly(first, list_of_move, kindly, detailed_list)
        elif args.algo == 'insert':
            kindly = 'insert'
            list_of_move, detailed_list = insertion_sort(args.number)
            mainly(first, list_of_move, kindly, detailed_list)
        elif args.algo == 'quick':
            quick_sort(args.number)
        elif args.algo == 'merge':
            merge_sort(args.number)
    else:
        checking_without_gui(args)


if __name__ == '__main__':
    main()

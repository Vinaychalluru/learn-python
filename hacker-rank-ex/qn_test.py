if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(*integer_list)
    print(type(integer_list))
    tup = tuple(integer_list)
    print(hash(tup))
l=[3476767,6,3,1,4857,5,7777]

def min_max(l):
    print(f'Min is: {min(l)} and Max is: {max(l)}')

def get_min_max(l):
    l.sort()
    print(f'Min is: {l[0]} and Max is: {l[-1]}')

def get_min_max_2(l):
    c = len(l)
    l.sort()

    print(f'Min is: {l[0]} and Max is: {l[c-1]}')

def min_max_algo(l):
    max_val = -1
    for idx, num in enumerate(l):
        if idx < len(l) - 1:
            # if l[idx] > l[idx + 1]:
            #     l[idx + 1] = l[idx]
            if l[idx] > max_val:
                max_val = l[idx]

    print(max_val)


# min_max(l)

# get_min_max(l)

# get_min_max_2(l)

min_max_algo(l)
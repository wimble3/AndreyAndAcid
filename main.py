def get_minimum_number_of_operations():
    number_of_tanks = int(input())
    volumes = list(map(int, input().split()))
    if len(volumes) != number_of_tanks:
        raise Exception('The number of tanks is incorrect')

    result = 0
    if volumes == sorted(volumes):
        for i in range(len(volumes)-1):
            result += volumes[i+1] - volumes[i]
        return str(result)
    else:
        return '-1'


if __name__ == '__main__':
    print(get_minimum_number_of_operations())

def mountCount(altitudes):
    climbed = 0
    for m in range(1, len(altitudes) - 1):
        if altitudes[m - 1] < altitudes[m] and altitudes[m + 1] < altitudes[m] :
            climbed += 1
    print(climbed)

if __name__ == '__main__':
    altInput = list(map(float, input().split()))
    mountCount(altInput)
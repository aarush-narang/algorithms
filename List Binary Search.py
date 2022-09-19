import random

def findTrialsLighterCoin(listOfNums, trialsCt):
    trialsCt += 1
    listLen = len(listOfNums)
    
    leftList = listOfNums[:listLen // 2]
    rightList = listOfNums[listLen // 2:(listLen // 2) * 2]
    remainder = listOfNums[listLen - 1] if listLen % 2 == 1 else None

    print(leftList, rightList, remainder)

    if(sum(leftList) == sum(rightList)): return trialsCt, remainder
    elif(len(leftList) == 1 and len(rightList) == 1): return trialsCt, max(leftList[0], rightList[0])
    elif(sum(leftList) < sum(rightList)):
        return findTrialsLighterCoin(rightList, trialsCt)
    elif(sum(leftList) > sum(rightList)):
        return findTrialsLighterCoin(leftList, trialsCt)

def main():
    arr = []
    arr_length = int(input("\n\nEnter array length. This program will assign the value of 10 to a random element in a list and will try to find it. "))

    for _ in range(arr_length):
        arr.append(1)
    arr[random.randint(0, arr_length - 1)] = 10
    
    trialsCt = 0
    trials = findTrialsLighterCoin(arr, trialsCt)

    print(trials)
    main()

if __name__ == "__main__":
    main()
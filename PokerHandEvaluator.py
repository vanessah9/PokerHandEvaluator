# October 2019

# instantiation of variables rank and suit
rank = "23456789TJQKA"  
suit = "cdhs"

# evaluate function
# when the evaluate function is called, it checks the given hand
# and determines and returns the poker hand (i.e flush, four of a kind etc..)
# it corresponds to 
def evaluate(hand):
    # dictionary that holds {rank:occurrences}
    count = {}

    # for loop: checks all the characters in the given hand
    # if 'i' is in the string 'rank' then add it to count dictionary
    # checks if 'i' is in the dictionary, if not add a new key with character 'i'
    # if it is, then add 1 to occurrences
    # increase the number of occurrences each time the same character occurs
    for i in hand:
        if i in rank:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
    # print(str(count))  --> this code prints the dictionary

    counter = 0
    # the following code checks if it is a flush; where all suits are the same
    # need 5 of the same suit
    for i in hand:
        temp = hand[1]
        if i in suit:
            if i == temp:
                temp = i
                counter += 1    #increase counter everytime i == temp, 
                                #so when the counter == 5, it's a flush

    # this code determines what poker hand it is and returns a statement
    # checks if the value 4 is in the dictionary count: if it is then it is a four of a kind
    if 4 in count.values():
        statement = "four of a kind"

    # checks if the counter variable equal to 5, if it is not then it is not a flush
    elif counter == 5:
        statement = 'flush'

    # checks if 3 is in the count dicitionary and 2 is not in it
    # if this is true, then it is a three of a kind
    elif 3 in count.values() and 2 not in count.values():
        statement = "three of a kind"

    # checks if 2 is in the count dictionary
    # if 3 is in the count dictionary too then it is a full house
    # else it is just a pair
    elif 2 in count.values():
        if 3 in count.values():
            statement = "full house"
        else:
            statement = "pair"

    # if none of the above, it is a _ high
    # finds the greatest rank
    else:
        high = 0
        for i in hand:
            if i in rank:
                if rank.find(i) > high:
                    high = rank.find(i)
        statement = (rank[high] + ' high')

    return statement

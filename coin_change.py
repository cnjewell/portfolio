# https://www.hackerrank.com/challenges/coin-change/problem

def get_ways_count(to_change, type_count, coin_types):
    pass
    # find the number of ways to make chage for to_change with the values in coin_types
    # note, type_count is just the size of coin_types. Left in because HackerRank input will include it. 

    # Consider degenerate cases, like n = 0, to figure this one out

    
    # for type in coin_types:
        # get modulo remainder and quotient
        # quotient goes to type count
        # modulo get passed in again? 
        # hmmm....


def main():
    n = 4
    m = 3
    c = [1, 2, 3]
    print(get_ways_count(n, m, c))




if __name__ == "__main__":
    main()
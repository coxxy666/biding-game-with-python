bid = {}
biding_end = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''

    for bidder in bidding_record :
      bid_amount =  bidding_record[bidder]

      if  bid_amount > highest_bid :

        highest_bid = bid_amount 

      winner = bidder

    print (f"The winner is {winner} with a bid of ${highest_bid}")

while not biding_end :

        name = input("What is your name ?")

        amount = int(input("How much are you bidding ? $"))

        bid[name] = amount

        should_continue = input("Do we still have a bidder type ' YES ' to continue or 'NO' to stop")
        if should_continue == 'NO' :
            biding_end = True
            highest_bidder(bid)
        elif should_continue == 'YES' :
              biding_end = False







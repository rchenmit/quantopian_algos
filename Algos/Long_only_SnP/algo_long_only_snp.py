import math
# Put any initialization logic here.  The context object will be passed to
# the other methods in your algorithm.
def initialize(context):
    context.vanguardConsumerStaples = sid(25903)
    context.max_notional = 1000000.1 #maximum in DOLLARS
    context.min_notional = -1000000.0
    
# Will be called on every trade event for the securities you specify. 
def handle_data(context, data):
    # Implement your algorithm logic here.

    # data[sid(X)] holds the trade event data for that security.
    # context.portfolio holds the current portfolio state.

    # Place orders with the order(SID, amount) method.

    price = data[context.vanguardConsumerStaples].price
    notional = context.portfolio.positions[context.vanguardConsumerStaples].amount * price
    
    # TODO: implement your own logic here.

    #just buy 100 shares at the start date;
    numshares_tobuy = math.floor(context.max_notional / price)
    
    numshares_vanguardConsumerStaples = context.portfolio.positions[context.vanguardConsumerStaples].amount
    print "Notional today: " + str(notional)
    print "Num shares today: " + str(numshares_vanguardConsumerStaples)
    print "Price today: " + str(price)
    print "Num shares to buy today =floor(context.max_notional/price) = " + str(numshares_tobuy)
    if numshares_vanguardConsumerStaples == 0:
        print "BUY " + str(numshares_tobuy) + " shares " + str(context.vanguardConsumerStaples)
        order(context.vanguardConsumerStaples, int(numshares_tobuy))
    print "Portfolio value: " + str(context.portfolio.portfolio_value)
    print "Positions value: " + str(context.portfolio.positions_value)
    print "Num shares now, after IF statement: " + str(context.portfolio.positions[context.vanguardConsumerStaples].amount)
    print "-------------------------------------"
       
   
    

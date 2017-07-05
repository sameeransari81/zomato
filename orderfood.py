new_restaurants = {
    'restaurants': {
        'pizza hut': {
            'Menu': {
                'cheese pizza': 130,
                'double cheese pizza': 190,
                'veggie pizza': 159
            },
            'Owner name': 'Sameer Ansari',
            'Rating': 4.8
        },
        'Burger king': {
            'Menu': {
                'cheesy burger': 95,
                'chicken burger': 130,
            },
            'Owner name': 'MG',
            'Rating': 3.5

        }
    }
}
input = raw_input('1. owner \n2.Customer')
if input == '1':
    owner_option_choosed = raw_input('Do you want to update\n YES or NO ')
    if owner_option_choosed == 'YES':
        select_restaurant = raw_input('enter the restaurant name in which u have to update')
        if select_restaurant in new_restaurants['restaurants'].keys():
            update_choosed = raw_input('add a new item\npress yes')
            if update_choosed == 'yes':
                updated_item_name = raw_input('enter the food name')
                if updated_item_name in new_restaurants['restaurants'][select_restaurant]['Menu']:
                    print updated_item_name, 'already exist in item list'
                elif updated_item_name not in new_restaurants['restaurants'][select_restaurant]['Menu']:
                    print 'item is updated'
        elif select_restaurant not in new_restaurants['restaurants'].keys():
            print 'restaurant unavailable'
    elif owner_option_choosed == 'NO':
        print 'tata'
elif input == '2':
    print new_restaurants['restaurants'].keys()
    order = raw_input('wants to order \npress yes')
    if order == 'yes':
        restaurant_choosed = raw_input('From which Restaurant you want to order?')
        if restaurant_choosed not in new_restaurants['restaurants'].keys():
            print 'Sorry! Restaurant not available'
        elif restaurant_choosed in new_restaurants['restaurants'].keys():
            customer_order_name = raw_input('Enter your food name')
            if customer_order_name in new_restaurants['restaurants'][restaurant_choosed]['Menu']:
                total = new_restaurants['restaurants'][restaurant_choosed]['Menu'][customer_order_name]
                bill = total + (total * 0.1) + (total * 0.06) + (total * 0.15)
                print 'ordered successfully'
                print 'your price is', bill
            else:
                print 'unavailable food item'
    ordering_method = raw_input('how do you want to order\nby delivery\nwalk in\nPlease enter')
    if ordering_method == 'by delivery':
        print 'Choosen method is DELIVERY'
        print 'amount to be paid' + str(bill)

    elif ordering_method == 'walk in':
        print 'Chosen method is walk-in'
        print 'amount to be paid' + str(bill)
    rating_input = raw_input('PLEASE RATE US\n Press  rate')
    if rating_input == 'rate':
        rating = float(raw_input('your rating is'))
        new_restaurants['restaurants'][restaurant_choosed]['Rating'] = rating
        print 'Thanx for the rating'
else:
    print 'BYE'

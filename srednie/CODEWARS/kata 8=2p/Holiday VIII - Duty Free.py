# def duty_free(price, discount, holiday_cost):   #Maja
#     profit=price*discount/100
#     bottle=int(holiday_cost/profit)
#     return bottle
######################################################
# def duty_free(price, discount, holiday_cost):
#   return holiday_cost * 100 // price // discount
########################################################
# def duty_free(price, discount, holiday_cost):
#   return holiday_cost // (price * (discount / 100))
##########################################################
# def duty_free(price, discount, holiday_cost):
#     return holiday_cost * 100 // (price * discount)
##########################################################
duty_free = lambda p, d, h: h // (p * d / 100)
###########################################################


print(duty_free(12,50,1000))
print(duty_free(17,10,500))

# Test.describe("Basic tests")
# Test.assert_equals(duty_free(12, 50, 1000), 166)
# Test.assert_equals(duty_free(17, 10, 500), 294)
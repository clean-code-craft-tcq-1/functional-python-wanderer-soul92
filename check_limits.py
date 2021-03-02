
import battery_test

if __name__ == '__main__':
    
    assert(battery_test.check_battery_is_ok({'temperature' : 25,'soc' : 70,'charge_rate' : 0.9}) is False) 
    assert(battery_test.check_battery_is_ok({'temperature' : 25,'soc' : 70,'charge_rate' : 0.7}) is True)
    assert(battery_test.check_battery_is_ok({'temperature' : 50,'soc' : 85,'charge_rate' : 0}) is False)

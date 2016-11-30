#checks if bit 4 is on
def check_bit4(x):
    mask = 0b1000
    result = x & mask
    
    if result > 0:
        return "on"
    else:
        return "off"

#turn on 3rd bit
def bit3_on(x):
	mask = 0b100
	result = x | mask
	return result
	
def flip_8bit(x)
	mask = 0b11111111
	result = x ^ mask
	return result

#left shift bit by n
def flip_bit(x, n):
    mask = (0b1 << n - 1)
    result = x ^ mask
    return result
#Average of a list
def average(x):
    sum += x
    average = sum / float(len(x))
    return average

#Variance of a list
def variance(x):
    avg = average(x)
    variance = 0
    for i in x:
        variance += (avg - i) ** 2
    return variance / len(x)

def grades_std_deviation(variance):
    return variance ** 0.5
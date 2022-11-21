def getCAGR(first,last,years):
    return (last/first)**(1/years)-1

cagr = getCAGR(65300,2669000,20)

print("SEC CAGR : {:.2%}".format(cagr))
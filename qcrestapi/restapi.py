#goal of this is to read projects, let you choose which one you want to run a
#backtest on, and then show you the results. All in Python.

#modules
import requests
import json

###
# todo: following should be made into QCRestAPI class
###
#variables
email = ""
password = ""
auth = (email,password)

#some preset values for testing
projectId = '26246'
backtestId = 'fbd7f250268591049d9b3ce1ac305741'

###
# simplified function for accessing QC Rest API.
# input: url, json/data
# output: json from QC
# todo: simplify even further. url should be 'request_type' string.
###
def postQCRestAPI(url, data):
    r = requests.post(url, json.dumps(data), auth=auth, verify=False)
    return json.loads(r.text)

###
# function to print out projects in a readable format.
# input: json data from project read
# output: formatted print to screen
###
def printProjects(data):
    projects = data['projects']
    print ''
    print '===================================='
    print '======== PROJECT PRINT OUT ========='
    print '===================================='
    print ''
    print 'IP: ' + data['ip']
    print 'Errors: ' + str(data['errors'])
    print 'Success: ' + str(data['success'])
    print ''
    print '=========== PROJECTS ==============='
    print ''
    for project in projects:
        print 'Id: ' + str(project['id'])
        print '  Modified: ' + str(project['modified'])
        print '  Name: ' + str(project['name'])
    print '===================================='

###
# function to print out back test results in a readable format.
# input: json data from backtest read
# output: formatted print to screen
###
def printBacktest(data):
    results = data['results']
    statistics = results['Statistics']
    profitloss = results['ProfitLoss']
    orders = results['Orders']
    charts = results['Charts']
    print ''
    print '===================================='
    print '======= BACK TEST PRINT OUT ========'
    print '===================================='
    print ''
    print 'BacktestId: ' + 'fbd7f250268591049d9b3ce1ac305741'
    print 'Success: ' + str(data['success'])
    print 'Errors: ' + str(data['errors'])
    print 'IP: ' + data['ip']
    print 'Processing Time: ' + data['processingTime']
    print 'Progress: ' + data['progress']
    print ''
    print '============ RESULTS ==============='
    print ''
    print '-->STATISTICS'
    print 'Expectancy: ' + statistics['Expectancy']
    print 'Average Loss: ' + statistics['Average Loss']
    print 'Total Trades: ' + statistics['Total Trades']
    print 'Compounding Annual Return: ' + statistics['Compounding Annual Return']
    print 'Average Win: ' + statistics['Average Win']
    print 'Profit-Loss Ratio: ' + statistics['Profit-Loss Ratio']
    print 'Loss Rate: ' + statistics['Loss Rate']
    print 'Information Ratio: ' + statistics['Information Ratio']
    print 'Win Rate: ' + statistics['Win Rate']
    print 'Beta: ' + statistics['Beta']
    print 'Net Profit: ' + statistics['Net Profit']
    print 'Treynor Ratio: ' + statistics['Treynor Ratio']
    print 'Drawdown: ' + statistics['Drawdown']
    print 'Tracking Error: ' + statistics['Tracking Error']
    print 'Annual Standard Deviation: ' + statistics['Annual Standard Deviation']
    print 'Alpha : ' +  statistics['Alpha']
    print 'Sharpe Ratio: ' + statistics['Sharpe Ratio']
    print 'Annual Variance: ' + statistics['Annual Variance']
    print ''
    print '-->Profit/Loss'
    for key in profitloss.keys():
        print 'Date: ' + key
        print '>> $ ' + str(profitloss[key]) + ' <<'
    print ''
    print '-->Orders'
    for key in orders.keys():
        print key + ':'
        orderinfo = orders[key]
        print '  Status: ' + str(orderinfo['Status'])
        print '  Direction: ' + str(orderinfo['Direction'])
        print '  Contingent Id: ' + str(orderinfo['ContingentId'])
        print '  Absolute Quantity: ' + str(orderinfo['AbsoluteQuantity'])
        print '  Symbol: ' + str(orderinfo['Symbol'])
        print '  Value $: ' + str(orderinfo['Value'])
        print '  Price per Share: ' + str(orderinfo['Price'])
        print '  Tag: ' + str(orderinfo['Tag'])
        print '  Broker Id: ' + str(orderinfo['BrokerId'])
        print '  Time: ' + orderinfo['Time']
        print '  Duration: ' + str(orderinfo['Duration'])
        print '  Type: ' + str(orderinfo['Type'])
        print '  Id: ' + str(orderinfo['Id'])
        print '  Quantity: ' + str(orderinfo['Quantity'])
    print ''
    print '-->Charts Available'
    i = 1
    for key in charts.keys():
        print str(i) + '. ' + key
        i += 1
    print ''
    print '====== END BACKTEST INFO ==========='
    print '===================================='


#request projects with requestQCRest()
data_out = postQCRestAPI("https://www.quantconnect.com/api/v1/projects/read",{})
printProjects(data_out)


##create new project
##this section isn't as useful for this script...although could be used.
#create_url = "https://www.quantconnect.com/api/v1/projects/create"
#data = json.dumps({"projectName":"curl_rest_api_test"})
#rcreate = requests.post(create_url, data, auth=auth, verify=False)

#print rcreate.text

print ''
print '=='
print '=> COMPILE'
print '=='
print ''
#compile project with postQCRestAPI()
data_compile = postQCRestAPI("https://www.quantconnect.com/api/v1/compiler/create",
                {"projectId":projectId})
print data_compile
print ''
print '===='
print ''

##LEAVE COMMENTED OUT UNTIL CERTAIN YOU WANT TO USE ONE OF YOUR FIVE
##REST API BACKTESTS FOR THE DAY
##run backtest with postQCRestAPI()
#data_backtest_create = postQCRestAPI("https://www.quantconnect.com/api/v1/backtests/create",
#                {"projectId":"26246","compileId":data_compile["compileId"],
#                "backtestName":"backtesting AGAIN"})
#print data_backtest_create

#read backtest data with postQCRestAPI()
#data_backtest_read = postQCRestAPI("https://www.quantconnect.com/api/v1/backtests/read",
#                {"backtestId":data_backtest_create["backtestId"]})
#print data_backtest_read


#try reading an already run backtest
data_backtest_read = postQCRestAPI("https://www.quantconnect.com/api/v1/backtests/read",
                {"backtestId":backtestId})
#print data_backtest_read
printBacktest(data_backtest_read)

#goal of this is to read projects, let you choose which one you want to run a
#backtest on, and then show you the results. All in Python.

#modules
import requests
import json

class QCRestAPI:

    ###
    # initiate with email and password
    ###
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.auth = (email,password)
        self.baseurl = 'https://www.quantconnect.com/api/v1/'

    ###
    # simplified method for accessing QC Rest API.
    # input: url, json/data
    # output: json from QC
    ###
    def postQCRestAPI(self, url, data):
        r = requests.post(self.baseurl + url, json.dumps(data), auth=self.auth, verify=False)
        print json.dumps(data)
        return json.loads(r.text)

    ###
    # method for requesting list of projects
    # input: none
    # output: list of projects
    ###
    def requestProjects(self):
        return self.postQCRestAPI('projects/read',{})

    ###
    # method for creating a project
    # input: name
    # output: confirmation info
    ###
    def createProject(self, name):
        return self.postQCRestAPI('projects/create',{"projectName":name})

    ###
    # method for deleting a project
    # input: projectId
    # output: confirmation info
    ###
    def deleteProject(self, projectId):
        return self.postQCRestAPI('projects/delete',{"projectId":projectId})

    ###
    # method for updating a project
    # input: projectId, file/code list
    # output: confirmation info
    ###
    def updateProject(self, projectId, fileCodeList):
        return self.postQCRestAPI('projects/update',{"projectId":projectId,
        "files":fileCodeList})

    ###
    # method for updating a project
    # input: projectId
    # output: project file content
    ###
    def readProjectFiles(self, projectId):
        return self.postQCRestAPI('projects/read',{"projectId":projectId})

    ###
    # method for compiling project
    # input: projectId
    # output: confirmation info
    ###
    def compileProject(self,projectId):
        return self.postQCRestAPI('compiler/create',{"projectId":projectId})

    ###
    # method for creating backtest
    # input: projectId, compileId, name
    # output: confirmation info
    ###
    def createBacktest(self, projectId, compileId, backtestName):
        return self.postQCRestAPI('backtests/create',{'projectId':projectId,'compileId':compileId,'backtestName':backtestName})

    ###
    # method for reading backtest
    # input: backtestId
    # output: backtest info
    ###
    def readBacktest(self, backtestId):
        return self.postQCRestAPI('backtests/read',{'backtestId':backtestId})

    ###
    # function to print out projects in a readable format.
    # input: json data from project read
    # output: formatted print to screen
    ###
    def printProjects(self, data):
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
    def printBacktest(self, data):
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

if __name__ == "__main__":

    qc = QCRestAPI('','')
    #print qc.requestProjects()
    #qc.printProjects(qc.requestProjects())
    #print qc.createProject('pythonrest')
    #print qc.compileProject('27385')
    print qc.createBacktest('27385','1126f75e2acd8baf7e927c77305655ff','another backtest')
    #print qc.readBacktest('ae2134e005ec46ec6f82d8564cc30bbe')

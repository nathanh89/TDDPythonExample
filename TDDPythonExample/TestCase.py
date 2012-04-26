from TestResult import TestResult
class TestCase:
    def __init__(self, name):
        self.name= name

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            self.runTest()
        except:
            result.testFailed()
        self.tearDown()

    def runTest(self):
        method= getattr(self, self.name)
        method()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def outputLog(self, log):
        with open("C:/Nathans Python Folder/log.txt", "w") as f:
            f.write(log)
              

from TestSuite import TestSuite
from TestResult import TestResult
from WasRun import WasRun
from TestCase import TestCase
from os import path

class TestCaseTest(TestCase):

    def setUp(self):
        self.result= TestResult()

    def testTemplateMethod(self):
        test= WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown" == test.log)

    def testResult(self):
        test= WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedResult(self):
        self.test= WasRun("testBrokenMethod")
        self.test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())
        

    def checkForLog(self):
        self.test= WasRun("testMethod")
        self.test.run(self.result)
        assert(path.isfile("C:/Nathans Python Folder/log.txt"))

    def testSetUpException(self):
        self.test= TestCase("setUp")
        self.test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())
               
    def testSuite(self):
        suite= TestSuite()
        suite.add(TestCaseTest("testFailedResultFormatting"))
        suite.add(TestCaseTest("setUp"))
        suite.add(TestCaseTest("testTemplateMethod"))
        suite.add(WasRun("testMethod"))
        suite.add(TestCaseTest("testResult"))
        suite.add(WasRun("testBrokenMethod"))
        suite.add(TestCaseTest("testSetUpException"))
        suite.run(self.result)
        assert("6 run, 2 failed" == self.result.summary())
        

result= TestResult()      
POON = TestCaseTest("testSuite")
POON.run(result)
print POON.result.summary()

        

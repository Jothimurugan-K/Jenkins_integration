__author__ = 'Jothimurugan'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


'''
import HtmlTestRunner
import unittest
import os


class SampleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("In SetUP")

    def test_browser(self):
        self.driver.get("https://www.google.com/")

    def test_report(self):
        direct = os.getcwd()
        print(direct)
        outfile = open(direct + "\TestReport.html", "w")
        runner1 = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report',description='Test Results')

        runner1.run(smoke_test)



    def tearDown(self):
        self.driver.quit()


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        sample_test_suite = unittest.TestSuite()
        sample_test_suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(SampleTest.test_browser)])

        direct = os.getcwd()
        outfile = open(direct + "\TestResult.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report',description='Sample Tests')

        runner1.run(sample_test_suite)


if __name__ == '__main__':
    unittest.main()
'''

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.close()
print("Chrome opened successfully...")


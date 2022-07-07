#!/usr/bin/env python3
import unittest
import unittest.mock
import importlib
import random


if __name__ == '__main__':

    class Check(unittest.TestCase):
        POINTS=10

        def setUp(self):
            pass
        def tearDown(self):
            pass

        def correct(self,permissions):
            val = 0
            for idx, shift in enumerate(range(8,-1,-1)):
                val |= (0 if permissions[idx] == '-' else 1) << shift
            return val

        def test_q14(self):
            for case in range(10):
                permissions = '{}{}{}{}{}{}{}{}{}'.format(
                    random.choice('r-'),
                    random.choice('w-'),
                    random.choice('x-'),
                    random.choice('r-'),
                    random.choice('w-'),
                    random.choice('x-'),
                    random.choice('r-'),
                    random.choice('w-'),
                    random.choice('x-'))
                correct = self.correct(permissions)
                with self.subTest(points=1,msg='{} = {} = {}'.format(permissions,correct,oct(correct))):
                    self.assertEqual(student.perms(permissions),correct)
                    


    class GradeTestResult(unittest.TextTestResult):

        def __init__(self,stream,descriptions,verbosity):
            self.successes = 0 
            self.grade = 0
            self.possible = 0
            unittest.TextTestResult.__init__(self,stream,descriptions,verbosity)

        def startTest(self,test):
            self.possible += test.POINTS
            unittest.TextTestResult.startTest(self,test)

        def addSubTest(self,test,subtest,outcome):
            if outcome is None:
                self.successes += subtest.params['points']
            self.grade = self.successes/self.possible * 100
            unittest.TextTestResult.addSubTest(self,test,subtest,outcome)

        def __str__(self):
            return '{}/{} points earned ({:.2f}%)'.format(self.successes,self.possible,self.grade)

    
    class GradeTestRunner(unittest.TextTestRunner):
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)

        def run(self,test):
            result = super().run(test)
            return result

    exammodule = 'deliverable'
    student = importlib.import_module(exammodule)

    runner = GradeTestRunner(resultclass=GradeTestResult)
    test = unittest.main(exit=False,verbosity=9,failfast=False,testRunner=runner)
    print(test.result)

else:
    print('do not import this module')
	

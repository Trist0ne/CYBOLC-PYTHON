#!/usr/bin/env python3
import unittest
import unittest.mock
import importlib
import random
import string


if __name__ == '__main__':

    class Test(unittest.TestCase):
        POINTS=10

        def setUp(self):
            self.possible = string.ascii_letters + string.digits + string.punctuation
            self.meets_all = 'Ul0!___________'

        def tearDown(self):
            pass

        def test_complexity(self):

                # length check
                password_on = ''.join(random.choice(self.possible) for _ in range(random.randint(15,20)))
                password_off = ''.join(random.choice(self.possible) for _ in range(random.randint(8,13)))
                
                submitted = student.complexity(password_on)
                with self.subTest(points=1,pw=password_on,msg='length bit should be set'):
                    self.assertEqual(submitted & 0x1, 0x1)

                submitted = student.complexity(password_off)
                with self.subTest(points=1,pw=password_off,msg='length bit should be unset'):
                    self.assertEqual(submitted & 0x1, 0x0)
                

                # digit check
                password_on = ''.join(random.choice(string.digits) for _ in range(random.randint(16,20)))
                password_off = ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(random.randint(15,20)))
 
                submitted = student.complexity(password_on)
                with self.subTest(points=1,pw=password_on,msg='numeric bit should be set'):
                    self.assertEqual(submitted & 0x2, 0x2)

                submitted = student.complexity(password_off)
                with self.subTest(points=1,pw=password_off,msg='numeric bit should be unset'):
                    self.assertEqual(submitted & 0x2, 0x0)

                
                # upper check
                password_on = ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(15,20)))
                password_off = ''.join(random.choice(string.ascii_lowercase+string.punctuation+string.digits) for _ in range(random.randint(15,20)))
 
                submitted = student.complexity(password_on)
                with self.subTest(points=1,pw=password_on,msg='uppercase bit should be set'):
                    self.assertEqual(submitted & 0x4, 0x4)

                submitted = student.complexity(password_off)
                with self.subTest(points=1,pw=password_off,msg='uppercase bit should be unset'):
                    self.assertEqual(submitted & 0x4, 0x0)

                
                # lower check
                password_on = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(15,20)))
                password_off = ''.join(random.choice(string.ascii_uppercase+string.punctuation+string.digits) for _ in range(random.randint(15,20)))
                
                submitted = student.complexity(password_on)
                with self.subTest(points=1,pw=password_on,msg='lowercase bit should be set'):
                    self.assertEqual(submitted & 0x8, 0x8)

                submitted = student.complexity(password_off)
                with self.subTest(points=1,pw=password_off,msg='lowercase bit should be unset'):
                    self.assertEqual(submitted & 0x8, 0x0)


                # punctuation check
                password_on = ''.join(random.choice(string.punctuation) for _ in range(random.randint(15,20)))
                password_off = ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(random.randint(15,20)))
 
                submitted = student.complexity(password_on)
                with self.subTest(points=1,pw=password_on,msg='punctuation bit should be set'):
                    self.assertEqual(submitted & 0x10, 0x10)
                
                submitted = student.complexity(password_off)
                with self.subTest(points=1,pw=password_off,msg='punctuation bit should be unset'):
                    self.assertEqual(submitted & 0x10, 0x0)



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
	

# -*- coding: utf-8 -*-
"""
@author: user
"""

class A:
    def show(self):
        print("Good coder")
    def start(self):
        print("And Developer")
class B(A):
    def disp(self):
        print("Top of the world ")


ob=B()
ob.show()
ob.start()
ob.disp()

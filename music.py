import pygatt
import time
adapter = pygatt.GATTToolBackend()
adapter.start()
device = adapter.connect('5C:F8:21:B3:0C:3F')
adapter.sendline('char-write-cmd 0x0025 a105852a17a12589c70b2366f2bc7f98b53e32')
adapter.sendline('char-write-cmd 0x0025 a106410a1a1a30b7e320bda291')
adapter.sendline('char-write-cmd 0x0025 a107')
print '-->Initialize'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(1)
print '-->Wait'
adapter.sendline('char-write-cmd 0x0025 a104030401') #tak
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'
adapter.sendline('char-write-cmd 0x0025 a104030401') #tak
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'

adapter.sendline('char-write-cmd 0x0025 a104030401') #tak
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'
adapter.sendline('char-write-cmd 0x0025 a104030701') #tada
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'
adapter.sendline('char-write-cmd 0x0025 a104030401') #tak
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'
adapter.sendline('char-write-cmd 0x0025 a104030401') #tak
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'

adapter.sendline('char-write-cmd 0x0025 a104030401') #tak
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'
adapter.sendline('char-write-cmd 0x0025 a104030701') #tada
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'

adapter.sendline('char-write-cmd 0x0025 a104030401') #tak
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'
adapter.sendline('char-write-cmd 0x0025 a104030401') #tak
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'

adapter.sendline('char-write-cmd 0x0025 a104030401') #tak
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'
adapter.sendline('char-write-cmd 0x0025 a104030701') #tada
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'
adapter.sendline('char-write-cmd 0x0025 a104030401') #tak
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'
adapter.sendline('char-write-cmd 0x0025 a104030701') #tada
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'
adapter.sendline('char-write-cmd 0x0025 a104030401') #tak
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'
adapter.sendline('char-write-cmd 0x0025 a104030701') #tada
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'
adapter.sendline('char-write-cmd 0x0025 a104030701') #tada
time.sleep(0.3)
print '-->F  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
time.sleep(0.2)
print '-->D  code'
adapter.sendline('char-write-cmd 0x0025 a104030001')
adapter.stop()
print '-->Exit'

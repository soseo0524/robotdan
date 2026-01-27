import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/addinedu/Desktop/teamproject/gui/install/lovo_main_server'


"""
sys.modules是import的缓存机制
引入模块时优先从缓存中引入
    """
import sys
# 动态导入模块
module_name = 'json'
json = __import__(module_name)

# 检查 `sys.modules`
print(module_name in sys.modules)  # 输出: True
print(sys.modules[module_name])    
# 输出: <module 'json' from '/usr/lib/python3.9/json/__init__.py'>
json.loads('{}')
sys.modules[module_name].loads('{}')

from urllib3.util.retry import Retry
from requests.packages.urllib3.util.retry import Retry


for package in ("urllib3", "idna"):
    locals()[package] = __import__(package)
    # This traversal is apparently necessary such that the identities are
    # preserved (requests.packages.urllib3.* is urllib3.*)
    for mod in list(sys.modules):
     if mod == package or mod.startswith(f"{package}."):
        #requests.packages模块均指向"urllib3", "idna"
        sys.modules[f"requests.packages.{mod}"] = sys.modules[mod]
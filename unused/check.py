import sys
# def in_venv():
#     return sys.prefix != sys.base_prefix

# print(sys.prefix)
# print(sys.base_prefix)
# print(vars())
import urllib.parse
msg = """We are failing over MIS today from Bastrop to Taylor, beginning at 17:00. I posted the following operator message to the MUI: 

ERCOT will have a planned system maintenance of the Market Information System (MIS) today, January 18, 2024, from 17:00 until 19:30 CPT. During the maintenance, the CRR application can be accessed directly using this URL: https://mis.ercot.com/mui-ercot-ihedge/.

Thanks,

CRR Team
"""
print(urllib.parse.quote(msg))
import requests
r = requests.get('http://127.0.0.1:5000/api/classify/?img=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,81,21,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,14,200,49,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,0,1,0,0,0,162,184,165,20,0,1,1,3,4,1,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,2,0,120,183,154,206,32,0,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,3,0,76,227,151,139,158,0,0,0,0,0,66,23,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,55,224,162,143,121,204,236,144,21,74,90,190,8,0,0,0,0,0,0,0,0,0,0,1,0,0,0,42,228,160,148,125,165,223,208,221,246,211,174,151,0,0,0,0,0,1,3,0,1,0,3,0,9,0,23,230,168,147,119,163,227,206,200,190,206,186,139,171,41,0,0,0,0,0,0,0,0,0,3,4,0,16,209,185,139,118,181,227,209,204,210,199,225,157,127,190,111,0,1,3,2,1,3,2,3,0,0,0,67,214,187,139,111,191,229,203,208,208,196,223,188,100,128,155,112,0,0,0,0,0,0,0,0,0,48,161,218,171,147,116,185,235,201,209,203,204,220,208,126,133,162,164,187,0,0,12,16,9,4,19,73,170,211,188,145,149,148,136,222,218,207,208,215,224,193,140,146,162,156,118,203,37,47,255,188,187,182,203,206,182,147,140,148,148,148,134,180,218,221,225,204,156,134,139,144,140,123,97,206,30,88,203,164,167,170,161,147,147,156,159,153,152,155,150,134,136,153,145,136,151,164,168,170,166,153,130,200,10,131,195,150,133,132,142,160,166,162,153,152,153,151,154,163,147,152,163,205,208,174,175,178,181,168,150,196,1,155,228,197,172,138,123,121,122,126,129,135,139,144,158,177,192,239,244,178,176,183,179,185,177,147,148,192,0,0,80,196,199,212,209,190,176,170,178,183,192,204,204,202,144,59,3,0,67,217,184,188,178,166,160,188,13,0,0,0,3,51,105,179,217,235,227,208,201,133,58,0,0,0,0,0,16,187,194,184,185,175,181,131,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
assert(str(r) == "<Response [200]>")
assert(int(r.text) == 9)
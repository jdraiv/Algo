def convert_html(s):
    dic = {'&': '&amp;', "<": 'lt;', '>': 'gt;', '"': '&quot;'}
    
    for l in s:
        if l in dic:
            s = s.replace(l, dic[l])
            
    print(s)
    
    
convert_html("Dolce & Gabbana")
convert_html("Hamburgers < Pizza < Tacos")
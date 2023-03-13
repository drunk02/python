import re

long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

# 定义正则表达式模式
name_pattern = r'^[A-Za-z\s]+\n'
lei_pattern = r'^\d+[A-Za-z\d]+\n'
sub_fund_pattern = r'^(\d+)\. (.+)\n((?:LU\d+\n)+)'

# 匹配字符串中的各个部分
name = ''.join(re.findall(name_pattern, long_text,re.MULTILINE)).strip('\n')
lei = ''.join(re.findall(lei_pattern, long_text,re.MULTILINE)).strip('\n')
sub_fund_matches = re.findall(sub_fund_pattern, long_text, re.MULTILINE)
# 构造结果字典
result = {
    'name': name,
    'lei': lei,
    'sub_fund': []
}
for match in sub_fund_matches:
    title = match[1]
    isin_list = re.findall(r'LU\d+', match[2])
    result['sub_fund'].append({
        'title': title,
        'isin': isin_list
    })

# 打印结果
print(result)

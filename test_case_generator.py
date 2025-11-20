import dashscope

dashscope.api_key = "sk-d226c141c2954c5496300eb4b407822e"

role_system = f'''你是一名有十年经验的财产保险行业核心业务系统测试工程师'''
role_user = f'''为下面的需求规则，每个规则生成 3 条测试用例：
业务规则：车险的保费计算，
1.三者险保费1000元，可保证额度为100000元；
2.三者险保费2000元，可保障额度为200000元；
3.三者险保费固定位1000元或2000元。
生成的测试用例输出格式需要包含：用例序号、业务规则、测试用例描述、预期结果、输入数据、预期输出数据。'''
response = dashscope.Generation.call(
    model= "qwen3-max" ,
    messages= [
        {"role": "system", "content": role_system},
        {"role": "user", "content": role_user}
    ]
)
print(response.output.choices[0].message.content)
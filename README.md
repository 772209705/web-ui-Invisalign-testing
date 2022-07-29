### 项目介绍
    web UI 自动化测试，基于Python3.8 、selenium 3.141.0 、 pytest 6.2.5 、 allure 2.8.18 

    web自动化测试 项目以PO分层设计思想，解决后期代码量大，便于修改维护。 可生成好看报告allure 

    设计多线程运行，每个用例独立思想

### 配置环境
    pip install -r requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple

### allure 用法
    1、启动项目并生成allure
    pytest --alluredir=reports/allure --clean-alluredir
    
    2、将allure生成 html格式查看
    allure generate reports/allure -o allure_html --clean






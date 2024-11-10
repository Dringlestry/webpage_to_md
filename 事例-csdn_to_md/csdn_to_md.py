
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import markdownify
import time

def csdn_to_md(url, file_name):
    # 设置Chrome浏览器驱动
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 无头模式，不显示浏览器界面
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # 打开网页
    driver.get(url)

    # 等待页面完全加载，调整时间根据页面加载情况
    time.sleep(5)  # 你可以增加时间，或者使用WebDriverWait来更精确地等待元素加载

    # 获取页面源代码
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 查找包含文章内容的div标签
    article = soup.find('div', id='content_views', class_='htmledit_views')

    if article:
        # 将HTML内容转换为Markdown
        md_content = markdownify.markdownify(str(article), heading_style="ATX")

        # 将Markdown内容保存到文件
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"文章已保存为 {file_name}")
    else:
        print("找不到文章内容，请检查标签或页面结构")

    # 关闭浏览器
    driver.quit()


# 示例用法
csdn_to_md('https://blog.csdn.net/leader_song/article/details/132094080', 'output.md')

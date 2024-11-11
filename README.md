# webpage_to_md
爬取网页内容以.md格式存到本地

**原理**：通常页面使用JavaScript动态加载内容，需要用Selenium来模拟浏览器加载完整的内容，再抓取内容
## 1、准备工作
 - 安装相关依赖库
```bash
pip install requests beautifulsoup4 markdownify 
```
 - 安装Selenium

```bash
pip install selenium
```

 - 安装 webdriver_manager
 

```bash
pip install webdriver-manager
```

 - 下载并安装对应版本的ChromeDriver

   参考 [chromedriver下载与安装方法，亲测可用](https://blog.csdn.net/zhoukeguai/article/details/113247342)
 
##  2、准备步骤说明
1.`requests` ：针对静态页面，往往都是动态的

2.`Selenium`：模拟打开浏览器并加载网页内容。time.sleep(5)可以确保页面完全加载后再抓取。

3.`BeautifulSoup`：解析网页源码，查找目标标签（请更根据实际情况决定，仅实例中：id="content_views" 和 class="htmledit_views"）。

4.`markdownify`：将抓取的HTML内容转换为Markdown格式。

5.`webdriver_manager`：自动下载并管理ChromeDriver

6.`ChromeDriver`：一个独立的服务器，它实现了 WebDriver 的协议，用于自动化 Chromium 浏览器。通常用于测试 Web 应用程序、网页抓取或自动化日常任务

## 3、使用事例代码
**注意事项**
 - 找到目标标签的特点，进而通过BeautifulSoup查找
 - 要将传入的url换为目标的网址

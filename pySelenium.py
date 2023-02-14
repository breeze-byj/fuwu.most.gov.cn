from selenium.webdriver.common.by import By


class PySelenium:
    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def locator(self, locator):
        return self.driver.find_element(*locator)

    # 关闭
    def quit_borwser(self):
        self.driver.quit()
        self.driver.close()

    def maxwin(self):
        self.driver.maximize_window()

    # 访问
    def visit_url(self, url):
        self.driver.get(url)

    def find(self, element):
        STYLE = "background: green; border: 2px solid red;"
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, STYLE)
        return element

    # 后退
    def back(self, breakCount):
        sum = 0
        while sum > breakCount:
            self.driver.back()
            sum += 1

    # 获取url路径
    def getUrl(self):
        return self.driver.current_url()

    # 关闭当前页签
    def close(self):
        return self.driver.close()

    # 切换到当前窗口
    '''
    -1 切换到新窗口
    -2 切换到倒数第二个打开的窗口
     0 切换到最开始打开的窗口
    '''

    def switch_to(self, index):
        hand = self.driver.window_handles
        self.driver.switch_to.window(hand[index])

    # 打开新标签
    def openlable(self, url):
        js = 'window.open("%s")' % url
        self.driver.excute_script(js)

    def back_(self):
        "浏览器后退"
        self.driver.back()

    def forward(self):
        "浏览器前进"
        self.driver.forward()

    def click_loc(self, locator):
        self.locator(locator).click()

    def assemble_title_data(self, clumcount, tit_list, data_list):
        all_data_list = []
        dataobj = {}
        i = 1
        for title_index in range(len(tit_list)):
            dataobj[tit_list[title_index]] = data_list[title_index]
            i = i + 1
            if i > clumcount:
                i = 1
                all_data_list.append(dataobj)
                dataobj = {}
        return all_data_list

    def get_locator(self, xpaths):
        global locator
        for i in range(10):
            try:
                locator = self.driver.find_element(By.XPATH, xpaths).text
                break
            except:
                pass
        return locator

    # 最大化浏览器
    def max_win(self):
        self.driver.maximize_window()

    # Csv [[],[]]
    def write_csv(self, file_path, data_list_name):
        with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in data_list_name:
                writer.writerow(row)

    # 多元素定位
    def locators(self, locator):
        return self.driver.find_elements(*locator)

    # 关闭
    def queit_borwser(self):
        self.driver.quit()

    # 访问
    def visit(self, url):
        self.driver.get(url)

    def click_elemet(self, locator):
        ele = self.locator(locator)
        ele.click()

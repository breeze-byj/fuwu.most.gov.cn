from selenium import webdriver
from selenium.webdriver.common.by import By
from pySelenium import PySelenium
from writer import json_dump


class Run(PySelenium):
    def getDate(self):
        test_list = []
        # 总页数23/每页12条数据/数据总数271
        # 总页数
        page_count = 23
        # 每页的数量
        page_number = 12
        # 遍历页数(1...*)
        # --------------------翻页-------------------------------------
        for index in range(1, page_count + 1):
            print(">" * 30 + f"正在打印第{index}页数据")
            # 对第一页作判断
            if index != 1:
                self.visit(url=url + str(f"index_{index}.html"))
            for i in range(1, page_number + 1):
                print(f"正在打印第{index}页第{i}条数据")
                # 点击的数据页
                this_data = (By.XPATH, f'.//div[@class="right"]/div[@class="right-min"]/ul/li[{i}]/a')
                # 数据详情名称
                this_data_name = (By.XPATH, f'.//div[@class="right"]/div[@class="right-min"]/ul/li[{i}]/a/span')
                this_data_name = self.locator(this_data_name).text
                # 点击数据详情
                self.locator(this_data).click()
                # 打开新窗口
                self.switch_to(-1)
                # --------------------开始爬取-------------------------------------
                data_all = {}
                all_list = {}
                # 标题/日期
                project_name = (By.XPATH, './/div[@id="xq"]/div[@id="xq_t"]')
                project_name = self.locator(project_name).text
                # url
                currentPageUrl = self.driver.current_url
                # 列表数量
                list_numbers = []
                list_all = (By.XPATH, './/div[@id="xp_zw"]/table/tbody')
                list_all = self.locators(list_all)
                for i in list_all:
                    list_numbers.append(i)
                # 返回列表数量1,2,3
                list_number = len(list_all)
                for j in range(1, list_number + 1):
                    # 表头
                    titl = []
                    # 数据
                    table_info = []
                    # 表格项目名称
                    items_name = (By.XPATH, f'.//div[@id="xp_zw"]/table[{j}]/preceding-sibling::*[1]')
                    items_name = self.locator(items_name).text
                    # 表格行
                    tr_count_list = (By.XPATH, f'.//div[@id="xp_zw"]/table[{j}]/tbody/tr')
                    tr_count = len(self.locators(tr_count_list))
                    # 表格列
                    td_count_list = (By.XPATH, f'.//div[@id="xp_zw"]/table[{j}]/tbody/tr[1]/td')
                    td_count = len(self.locators(td_count_list))
                    for tr in range(2, 1 + tr_count):
                        for td in range(1, td_count + 1):
                            title_info = (By.XPATH,
                                          f'.//div[@id="xp_zw"]/table[{j}]/tbody/tr[1]/td[{td}]')
                            title_info = self.locator(title_info).text
                            titl.append(title_info)
                            agency_info = (
                                By.XPATH,
                                f'.//div[@id="xp_zw"]/table[{j}]/tbody/tr[{tr}]/td[{td}]')
                            table_info.append(self.locator(agency_info).text)
                    # 调方法,取到table数据
                    list_data = self.assemble_title_data(td_count, titl, table_info)
                    all_list[f'{items_name}'] = list_data
                # --------------------保存-------------------------------------
                data_all['TabelContent'] = all_list
                data_all['Title'] = this_data_name
                data_all['URL'] = currentPageUrl
                data_all['TableTitle'] = project_name

                # 关闭新打开的窗口
                self.close()
                # 返回上一级
                self.switch_to(0)

                # --------------------写入-------------------------------------

                test_list.append(data_all)
                json_dump('./data/data.json', test_list)


if __name__ == '__main__':
    url = 'https://fuwu.most.gov.cn/html/tztg/xzxkzx/'
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    Run(browser).visit(url)
    Run(browser).getDate()

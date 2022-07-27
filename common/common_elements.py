from selenium.webdriver.common.by import By


'''
    元素定位有id，name优先使用id，name  无的话就优先使用css selector
'''
class nologin_elements():
    """
    未登录情况下浏览元素
    """
    # 关于我们
    about = (By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(1)')
    # 文档
    document = (By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(2)')
    # 登录
    login = (By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(3)')
    # 登录成功验证的文本元素位置
    login_txt = (By.CSS_SELECTOR,'div.page-section.center.third-login-wrapper > div > h2')
    # 注册按钮
    register_button = (By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(4)')
    # 产品与服务下拉窗
    product_service = (By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(1) > div:nth-child(2)')
    # 产品与服务-云游戏
    product_service_game = (By.CSS_SELECTOR,'div.next-overlay-inner > div > div > div:nth-child(1)')
    # 产品与服务-aksk
    product_service_aksk = (By.CSS_SELECTOR,'div.next-overlay-inner > div > div > div:nth-child(2)')


class login_elements():
    """
    登录步骤元素
    """

    name_input = (By.NAME,'domainAccount')

    password_input = (By.NAME,'password')

    login_button = (By.CLASS_NAME,'sso-btn-submit')

    # choose_team 的div:nth-child(1) 括号内的数字表示当前团队列表的索引
    choose_team = (By.CSS_SELECTOR,'div.page-tenantselect-section-publicAccount > div > div:nth-child(1)')
    # 选择团队之后提交选择按钮
    team_submit = (By.CSS_SELECTOR,'div.tenantselect-btns > button:nth-child(2)')
    # 选择团队之后返回上一步
    team_back = (By.CSS_SELECTOR,'div.tenantselect-btns > button:nth-child(1)')



class ConsolePage():
    """
    登陆之后控制台下拉窗
    """

    # 控制台下拉窗
    console_sele = (By.CSS_SELECTOR, 'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(3)')
    # 控制台下拉窗微端服务平台
    console_micro = (By.CSS_SELECTOR, 'div.next-overlay-inner > div > div:nth-child(1)')
    # 控制台下拉窗开发者控制台
    console_inner = (By.CSS_SELECTOR,'div.next-overlay-inner > div > div:nth-child(2)')

class ProjectManagement():

    # 当前列表内无项目的情况下，创建项目按钮
    no_project_new = (By.CSS_SELECTOR,'div.GameEmpty--tip--YelldI8 > button')

    project_make = (By.CSS_SELECTOR,'div.main-wrapper > div > div > div > div > div > div > button')
    # 新建项目名称输入框
    pm_input = (By.ID,'gameName')
    # 上传项目直接 send_keys(documents.address)
    pm_upload_pic = (By.CSS_SELECTOR,'div.next-dialog-body > form > div:nth-child(2)')
    pm_confirm = (By.CSS_SELECTOR,'div.next-dialog-body > form > div:nth-child(3) > button:nth-child(2)')
    pm_cancel = (By.CSS_SELECTOR,'div.next-dialog-body > form > div:nth-child(3) > button:nth-child(1)')

    # 不输入项目名称点击确定-toast提示元素属性
    no_name_ele = (By.CSS_SELECTOR,'body > div:nth-child(10) > div > div')
    # 断言 assert no_name_ele.txt == "请检查表单内容"

    # 控制台搜索
    console_search = (By.CSS_SELECTOR,'div.main-wrapper > div > div > div > div > div > div > span')
    # 项目编辑悬浮按钮
    project_suspension = (By.CSS_SELECTOR,'div.next-overlay-wrapper > div > div > div:nth-child(1) > div > div:nth-child(2) > div > div')
    # 项目编辑
    project_edit = (By.CSS_SELECTOR,'div.next-overlay-wrapper > ul > li:nth-child(1)')

    # 项目删除按钮
    project_delete = (By.CSS_SELECTOR,'div.next-overlay-wrapper > ul > li:nth-child(2)')
#





class PersonalCenter():
    """
    登录之后个人头像
    """
    personal_icon = (By.CSS_SELECTOR,'div.yuanjing-header3 > div > div:nth-child(2) > div:nth-child(4)')
    # 团队消息
    message = (By.CSS_SELECTOR,'div.next-overlay-inner > div:nth-child(2) > div:nth-child(1)')

    # 个人中心
    personal_center = (By.CSS_SELECTOR,'div.next-overlay-inner > div:nth-child(2) > div:nth-child(2)')
    pc_information = (By.CSS_SELECTOR,'ul.next-menu-content > li:nth-child(1)')
    pc_security = (By.CSS_SELECTOR,'ul.next-menu-content > li:nth-child(2)')
    pc_aksk = (By.CSS_SELECTOR,'ul.next-menu-content > li:nth-child(3)')

    # 团队管理
    team_management = (By.CSS_SELECTOR,'div.next-overlay-inner > div:nth-child(2) > div:nth-child(3)')
    team_number = (By.CSS_SELECTOR,'aside.next-aside-navigation > div > ul > ul > li:nth-child(1)')
    team_auth = (By.CSS_SELECTOR,'aside.next-aside-navigation > div > ul > ul > li:nth-child(2)')

    # 登出账号
    logout = (By.CSS_SELECTOR,'div.next-overlay-inner > div:nth-child(2) > div:nth-child(4)')

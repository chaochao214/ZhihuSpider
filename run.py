import zhihu.spider
from zhihu.conf import config

# ### 程序设置（务必设置存储路径） #### #

# 默认存储路径为用户文档，开发环境下可设置为用户桌面或其他路径，方便查看结果
config.warehouse(r'C:\Users\{}\Desktop'.format('??'))

config.setting('running/file_type', 0)
config.setting('running/cached', False)
config.setting('running/css_output', False)
config.setting('running/download_image', True)
config.setting('running/cover', False)

# ### 启动爬虫 #### #
zhihu.spider.start(r'https://www.zhihu.com/question/371430700')

import matplotlib.font_manager as fm

# 打印系统中所有可用的字体
for font in fm.fontManager.ttflist:
    print(font.name)

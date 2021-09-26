import os, sys, inspect
from utils.segWord import SegWord

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

if __name__ == '__main__':
    sg = SegWord(load_inner=False)
    common_test_str = 'Buffer overflow in the Windows Redirector function in Microsoft Windows XP allows local users to execute arbitrary code via a long parameter.'
    print(sg.tokenize(common_test_str))  # 普通分词方法
    print(sg.tokenize_no_space(common_test_str))  # 返回没有空格的分词结果
    # sg.add_word("昵称")    # 向分词库中添加词语
    print(sg.tokenize(common_test_str))
    sg.load_dict_file("segword_test_dict.txt")  # 加载自定义字典到分词库中
    print(sg.tokenize(common_test_str))

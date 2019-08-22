# -*- coding:utf-8 -*-

import os
from performance_autotest.customexception import CustomError


def get_all_script(script_path, file_extension):
    """
    获取当前文件夹下所有指定后缀文件
    :param script_path:    文件夹路径
    :param file_extension: 文件类型
    :return:返回脚本文件列表
    """
    script_files = []
    if not os.path.exists(script_path):
        raise CustomError("路径错误,文件夹不存在")

    files = os.listdir(script_path)
    for file in files:
        if not os.path.isfile(script_path + "\\" + file):
            continue
        if os.path.splitext(file)[1] == file_extension:
            script_files.append(os.path.splitext(file)[0])

    if not script_files.__len__():
        raise CustomError("路径下无后缀为%s的脚本文件" % file_extension)

    return script_files


def jmeter_cmd(script_file):
    """
    获取路径生成执行脚本命令
    """
    cmd_list = []
    # TODO cmd 参数化
    cmd = r"D:\JMeter\apache-jmeter-5.1.1\bin\jmeter -n -t "
    for file in script_file:
        command = cmd + jmeter_path + os.path.sep + file + ".jmx" + " -l " + jmeter_path + os.path.sep + file + ".jtl"
        print(command)
        cmd_list.append(command)

    return cmd_list


def lr_cmd(script_file):
    """
    获取路径生成执行脚本命令
    """
    cmd_list = []
    # TODO cmd 参数化
    cmd = r'C:\"Program Files (x86)"\HP\LoadRunner\bin\wlrun -TestPath  '
    for file in script_file:
        command = cmd + lr_path + os.path.sep + file + ".lrs" + " -Run -ResultName " + lr_path + os.path.sep + file
        print(command)
        cmd_list.append(command)

    return cmd_list


if __name__ == '__main__':
    lr_path = r"C:\Users\zengjn\Desktop\Get\scenario"
    jmeter_path = r'C:\Users\zengjn\Desktop\jemter'
    files_jmeter = get_all_script(jmeter_path, ".jmx")
    jmeter_command = jmeter_cmd(files_jmeter)
    print("lr=============================")
    lr_files = get_all_script(lr_path, ".lrs")
    lr_command = lr_cmd(lr_files)
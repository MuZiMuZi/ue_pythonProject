import argparse
import types


def run(input_locals) :
    u'''
    在ue里快速执行某一个模块里的某一个函数
    例如py console_function.py --my_fun1
    :param input_locals: 需要执行的函数
    :return:
    '''
    parser = argparse.ArgumentParser()
    funcs = []
    for name , var in input_locals.items() :
        if type(var) not in [type.Function , types.LambdaType] :
            continue
        parser.add_argument('--' + name)
        funcs.append(name)
    sys_args = parser.parse_args()
    for name in funcs :
        arg_value = getattr(sys_args , name)
        if not arg_value :
            continue
        # 使用正则表达式检查调用函数的时候是否有（），如果没有的话则报错不再运行后面的代码
        assert arg_value.startswith('(') and arg_value.endswith(')') , \
            'Insufficient function arguments found for function {}，Needs to match regular expression ^(.*)$'.format(
                name)

        # 判断是否需要给定函数参数，当函数参数为（）的时候直接调用
        if arg_value == '()' :
            input_locals[name]()
        # 判断是否需要给定函数参数，当函数参数有参数的时候需要传入参数
        else :
            # 如果给定多个参数的话则需要解包传入
            arguments = arg_value[1 :-1].split(',')
            input_locals[name](*arguments)

if __name__ == '__main__':
    run(input_locals)
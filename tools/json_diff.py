
from deepdiff import DeepDiff
import json
import datetime
today = datetime.date.today()




def diff_json():
    # 定义两个 JSON 数据
    old_json_str = '{"name": "Alice", "age": 20, "city": "Beijing", "test2":"delete value"}'
    new_json_str = '{"name": "Bob", "age": 25, "city": ["Shanghai", "Beijing"], "test":"add value"}'
    old_data = json.loads(old_json_str)
    new_data = json.loads(new_json_str)

    # 找到两个 JSON 数据的不同之处
    diff = DeepDiff(old_data, new_data, ignore_order=True)

    # 输出差异信息
    #  print("JSON 数据的不同之处：", diff)
    for i in diff.keys():
        if i == 'dictionary_item_added':
            # 提取新添加的键值对
            added_items = diff['dictionary_item_added']
            for item in added_items:
                # 获取新添加的key和value
                key = item.split("[")[1].split("]")[0].replace("'", '')
                print(key)
                value = new_data[key]
                # print(added_items, type(added_items))
                print(f"新添加内容: {key}: {value}")

        elif i =='dictionary_item_removed':
            # 提取移除的键值对
            removed_items = diff['dictionary_item_removed']
            for item in removed_items:
                # 获取新添加的key和value
                remove_key = item.split("[")[1].split("]")[0].replace("'",'')
                print(remove_key)
                value = old_data[remove_key]
                # print(added_items, type(added_items))
                print(f"删除内容: {remove_key}: {value}")

        elif i == 'type_changes':
            type_changes_item = diff['type_changes']
            for item in type_changes_item:
                print(type_changes_item, item)
                type_changes_key = item.split("[")[1].split("]")[0]
                print(f"{type_changes_key}发生类型变化：")
                print(f"原值：{type_changes_item[item]['old_value']}")
                print(f"新值：{type_changes_item[item]['new_value']}")
                print(f"原值类型：{type_changes_item[item]['old_type']}")
                print(f"新值类型：{type_changes_item[item]['new_type']}")

        elif i == 'values_changed':
            value_changes_item = diff['values_changed']
            for item in value_changes_item:
                # print(type_changes_item, item)
                value_changes_key = item.split("[")[1].split("]")[0]
                print(f"{value_changes_key}发生值变化：")
                print(f"原值：{value_changes_item[item]['old_value']}")
                print(f"新值：{value_changes_item[item]['new_value']}")


def diff_json_file():
    with open('./old.json', 'r') as old:
        old_data = old.read()
    old_obj = json.loads(old_data)

    with open('./new.json', 'r') as new:
        new_data = new.read()
    new_obj = json.loads(new_data)

    # 找到两个 JSON 数据的不同之处
    diff = DeepDiff(old_obj, new_obj, ignore_order=True)

    # 输出差异信息
    #  print("JSON 数据的不同之处：", diff)

    with open(f'./{today}.txt', 'a+') as f:
        for i in diff.keys():
            if i == 'dictionary_item_added':
                f.write(f'新加内容： \n')
                # 提取新添加的键值对
                added_items = diff['dictionary_item_added']
                for item in added_items:
                    # 获取新添加的key和value
                    key = item.split("[")[1].split("]")[0].replace("'", '')
                    value = new_obj[key]
                    print(f"New item added: {key}: {value}")
                    f.write(f'{key}:{value} \n')

            elif i == 'dictionary_item_removed':
                # 提取移除的键值对
                f.write(f'移除内容：\n')
                removed_items = diff['dictionary_item_removed']
                for item in removed_items:
                    # 获取新添加的key和value
                    remove_key = item.split("[")[1].split("]")[0].replace("'", '')
                    print(remove_key)
                    value = old_obj[remove_key]
                    # print(added_items, type(added_items))
                    print(f"remove item added: {remove_key}: {value}")
                    f.write(f'{remove_key}:{value} \n')
            elif i == 'type_changes':
                f.write(f'类型变更：\n')
                type_changes_item = diff['type_changes']
                for item in type_changes_item:
                    print(type_changes_item, item)
                    type_changes_key = item.split("[")[1].split("]")[0]
                    print(f"{type_changes_key}发生类型变化：")
                    print(f"原值：{type_changes_item[item]['old_value']}")
                    print(f"新值：{type_changes_item[item]['new_value']}")
                    print(f"原值类型：{type_changes_item[item]['old_type']}")
                    print(f"新值类型：{type_changes_item[item]['new_type']}")
                    f.write(
                        f"{type_changes_key}类型发生变化： \n"
                        f"原值类型：{type_changes_item[item]['old_type']}\n"
                        f"新值类型：{type_changes_item[item]['new_type']}\n"
                        f"原值：{type_changes_item[item]['old_value']}\n"
                        f"新值：{type_changes_item[item]['new_value']}\n"
                    )

            elif i == 'values_changed':
                f.write(f'值变更：\n')
                value_changes_item = diff['values_changed']
                for item in value_changes_item:
                    # print(type_changes_item, item)
                    value_changes_key = item.split("[")[1].split("]")[0]
                    print(f"{value_changes_key}发生值变化：\n")
                    print(f"原值：{value_changes_item[item]['old_value']}")
                    print(f"新值：{value_changes_item[item]['new_value']}")
                    f.write(
                        f"{value_changes_key}值发生变化"
                        f"原值：{value_changes_item[item]['old_value']}\n"
                        f"新值：{value_changes_item[item]['new_value']}\n"
                    )

            else:
                print('pass')





if __name__ == "__main__":
    diff_json_file()










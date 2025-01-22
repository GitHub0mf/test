def sort_output(arr):
    """
    # 对输入数组进行排序并输出
    """
    sorted_arr = sorted(arr)
    for num in sorted_arr:
        print(num)

# 测试数据
test_array = [5, 2, 8, 1, 9]
sort_output(test_array)

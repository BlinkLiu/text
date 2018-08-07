from math import log
import operator


def calc_entropy(data_set):
    num_enter = len(data_set)
    label_count = {}
    for featV in data_set:
        curr_label = featV[-1]
        if curr_label not in label_count.keys():
            label_count[curr_label] = 0
        label_count[curr_label] += 1
    entropy = 0
    for key in label_count:
        prob = float(label_count[key])/num_enter
        entropy -= prob*log(prob, 2)
    return entropy


def split_data(data_set, axis, value):
    ret_data = []
    for feat_v in data_set:
        if feat_v[axis] == value:
            reduced_feat = feat_v[:axis]
            reduced_feat.extend(feat_v[axis+1:])
            ret_data.append(reduced_feat)
    return ret_data


def choose_to_split(data_set):
    num_feat = len(data_set[0])-1
    base_entropy = calc_entropy(data_set)
    best_info_gain = 0
    best_choose = -1
    for i in range(num_feat):
        feat_list = [example[i] for example in data_set]
        unique_values = set(feat_list)
        new_entropy = 0
        for value in unique_values:
            sub_data_set = split_data(data_set, i, value)
            prob = len(sub_data_set)/float(len(data_set))
            new_entropy += prob*calc_entropy(sub_data_set)
        info_gain = base_entropy-new_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_choose = i
    return best_choose


def major_count(class_list):
    class_count = {}
    for vet in class_list:
        if vet not in class_count.keys():
            class_count[vet] = 0
        class_count[vet] += 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def create_tree(data_set, labels):
    class_list = [example[-1] for example in data_set]
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    if len(data_set[0]) == 1:
        return major_count(class_list)
    best_feat = choose_to_split(data_set)
    best_feat_labels = labels[best_feat]
    my_tree = {best_feat_labels: {}}
    del(labels[best_feat])
    feat_values = [example[best_feat] for example in data_set]
    unique_values = set(feat_values)
    for value in unique_values:
        sub_labels = labels[:]
        my_tree[best_feat_labels][value] = create_tree(split_data(data_set, best_feat, value), sub_labels)
    return my_tree


def initial_data():
    data_set1 = [['青绿', '蜷缩', '是'],
                 ['乌黑', '硬挺', '是'],
                 ['乌黑', '蜷缩', '是'],
                 ['青绿', '蜷缩', '是'],
                 ['浅白', '蜷缩', '是'],
                 ['浅白', '稍蜷', '否'],
                 ['乌黑', '稍蜷', '否'],
                 ['浅白', '硬挺', '否'],
                 ['浅白', '硬挺', '否']]
    labels1 = ['色泽', '根蒂']
    return data_set1, labels1


if __name__ == '__main__':
    data_set, labels = initial_data()
    print(create_tree(data_set, labels))

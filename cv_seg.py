from pandas import DataFrame
def find_segments(data):
    num_seg = 1
    seg_label = []
    seg_label.append(num_seg)
    for i, p in enumerate(data['Potential']):
        seg_label.append(num_seg)
        if i + 2 == len(data) - 1:
            break
        delta_1 = data['Potential'][i+1] - p
        delta_2 = data['Potential'][i+2] - data['Potential'][i+1]
        if delta_1 * delta_2 < 0:
            num_seg += 1
    seg_label.append(num_seg)
    # data_seg = DataFrame(data, index = [seg_label, list(range(len(data)))])
    return [num_seg, seg_label]
    
def seg_to_cyc(num_seg):
    if num_seg % 2:
        cycle = [[1]]
        for i in list(range(2, num_seg + 1, 2)):
            cycle.append([i, i + 1])
    else:
        cycle = []
        for i in list(range(1, num_seg + 1, 2)):
            cycle.append([i, i + 1])
    return cycle
    
def label_maker(text, num):
    label = []
    for i in range(1, num + 1):
        label.append(text+' '+str(i))
    return label
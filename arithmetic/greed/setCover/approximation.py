

# 假设你办了广播节目，要让全美50个州的听众都收听到。为此你需要决定在哪些广播台播出。
# 在每个广播台播出都需要支付费用，因此你力图在尽可能少的广播台播出。

# 参与覆盖的州
states_needed=set(["mt","wa","or","id","nv","ut","ca","az"])

# 广播台与其所对应的州，不同广播台的覆盖区域可能重叠。
stations={}
stations["kone"]=set(["id","nv","ut"])
stations["ktwo"]=set(["wa","id","mt"])
stations["kthree"]=set(["or","nv","ca"])
stations["kfour"]=set(["nv","ut"])
stations["kfive"]=set(["ca","az"])


# 如何找出覆盖全州最少广播台集合？


#  本例采用近似算法，可得到非常接近的解。
#      a,选出覆盖最多的未被覆盖的广播台，即便这个广播台覆盖了一些已被覆盖的州也没关系
#      b,重复第一步直到覆盖了所有的州

# 优劣标准：
#     a,运行速度快
#     b,得到的近似解接近最优解
#     c,运行时间为O(n^2),n为广播台数量

final_stations=set()
while states_needed:
    best_station=None
    states_covered=set()

    for station,states_for_station in stations.items():
        covered=states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered=covered
        states_needed-=states_covered
        if best_station:
            final_stations.add(best_station)

print(final_stations) #{'kthree', 'kfive', 'kone', 'ktwo'}
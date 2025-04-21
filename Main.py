def print_array(list):
  for item in list:
    print(f'{item}\n')

def fame_cost(initial_level, end_level):
  return total_fame[end_level-2] - total_fame[initial_level-2] 

def best_option(w1_ini_lvl, w2_ini_lvl, w1_end_lvl, w2_end_lvl, w1_ip, w2_ip):
  w1_cost = fame_cost(w1_ini_lvl, w1_end_lvl)
  w2_cost = fame_cost(w2_ini_lvl, w2_end_lvl)
  
  coef1 = ((w1_end_lvl-w1_ini_lvl)*w1_ip)/w1_cost
  coef2 = ((w2_end_lvl-w2_ini_lvl)*w2_ip)/w2_cost

  if coef1 > coef2 :
    print('A primeira arma é a melhor escolha')
  elif coef1==coef2:
    print('Ambas as escolhas são boas')
  else:
    print('A segunda arma é a melhor escolha')

# --------------

total_fame = [29782, 60444, 92009, 124504, 157958, 192398, 227853, 264354, 301932,
        340617, 380442, 421442, 463652, 507106, 551841, 597895, 645306, 694115, 744363,
        796094, 849349, 904174, 960616, 1018722, 1078542, 1140125, 1203525, 1268793, 1335985,
        1405159, 1476373, 1549685, 1625160, 1702860, 1782850, 1865199, 1949976, 2037253, 2127104,
        2219603, 2314830, 2412864, 2513789, 2617689, 2724653, 2834771, 2948136, 3064842, 3184991,
        3308681, 3436018, 3567110, 3702067, 3841003, 3984036, 4131286, 4282878, 4438939, 4599602,
        4765002, 4935278, 5110575, 5291040, 5476826, 5668091, 5864994, 6067703, 6276389, 6491228,
        6712400, 6940095, 7174503, 7415822, 7664257, 7920016, 8183316, 8454379, 8733435, 9020717,
        9316471, 9620945, 9934396, 10257088, 10589296, 10931298, 11283384, 11645852, 12019006, 12403163,
        12798645, 13205789, 13624936, 14056443, 14500672, 14957998, 15428809, 15913501, 16412483, 16926179]




w1_ini_lvl = 97
w1_end_lvl = 99
w2_ini_lvl = 97
w2_end_lvl = 99
w1_ip = 0.2
w2_ip = 0.1



""" initial_level = int(input("level you are: "))
end_level = int(input("level you want to go: ")) """

best_option(w1_ini_lvl, w2_ini_lvl, w1_end_lvl, w2_end_lvl, w1_ip, w2_ip)
const fame_value = [29782, 60444, 92009, 124504, 157958, 192398, 227853, 264354, 301932,
  340617, 380442, 421442, 463652, 507106, 551841, 597895, 645306, 694115, 744363,
  796094, 849349, 904174, 960616, 1018722, 1078542, 1140125, 1203525, 1268793, 1335985,
  1405159, 1476373, 1549685, 1625160, 1702860, 1782850, 1865199, 1949976, 2037253, 2127104,
  2219603, 2314830, 2412864, 2513789, 2617689, 2724653, 2834771, 2948136, 3064842, 3184991,
  3308681, 3436018, 3567110, 3702067, 3841003, 3984036, 4131286, 4282878, 4438939, 4599602,
  4765002, 4935278, 5110575, 5291040, 5476826, 5668091, 5864994, 6067703, 6276389, 6491228,
  6712400, 6940095, 7174503, 7415822, 7664257, 7920016, 8183316, 8454379, 8733435, 9020717,
  9316471, 9620945, 9934396, 10257088, 10589296, 10931298, 11283384, 11645852, 12019006, 12403163,
  12798645, 13205789, 13624936, 14056443, 14500672, 14957998, 15428809, 15913501, 16412483, 16926179,
];

class weapon {
  #name;
  #initial_level;
  #end_level;
  #ip_per_level;

  constructor(name, initial_level, end_level, ip_per_level) {
    this.#name = name;
    this.#initial_level = initial_level;
    this.#end_level = end_level;
    this.#ip_per_level = ip_per_level;
  }

  get name() {
    return this.#name;
  }

  get initial_level() {
    return this.#initial_level;
  }

  set initial_level(value) {
    this.#initial_level = value;
  }

  get end_level() {
    return this.#end_level;
  }

  set end_level(value) {
    this.#end_level = value;
  }

  get ip_per_level() {
    return this.#ip_per_level;
  }

  total_fame_cost() {
    return fame_value[this.#end_level - 2] - fame_value[this.#initial_level - 2];
  }

  ip_coeficient() {
    return ((this.#end_level - this.#initial_level) * this.ip_per_level) / this.total_fame_cost();
  }

}

let weapon1 = new weapon("Machado de Guerra", 95, 100, 0.2);
let weapon2 = new weapon("Patas de Urso", 10, 50, 0.1);

console.log(weapon1.ip_coeficient());
console.log(weapon2.ip_coeficient());

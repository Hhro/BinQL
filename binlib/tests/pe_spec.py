prolog_ops= ['lea', 'xor', 'sub', 'jmp', 'retn', 'mov', 'push', 'cmp']
funcs=\
{'sub_14001112c': (5368779052, 5368779057),\
 'sub_14001128f': (5368779407, 5368779412),\
 'sub_140011230': (5368779312, 5368779317),\
 'sub_140013450': (5368788048, 5368788186),\
 'sub_14001128a': (5368779402, 5368779407),\
 'sub_140011235': (5368779317, 5368779322),\
 'sub_140011325': (5368779557, 5368779562),\
 'sub_1400112da': (5368779482, 5368779487),\
 'sub_140014250': (5368791632, 5368791786),\
 'sub_140011320': (5368779552, 5368779557),\
 'sub_1400112df': (5368779487, 5368779492),\
 'sub_14001104b': (5368778827, 5368778832),\
 'sub_140014120': (5368791328, 5368791342),\
 'sub_140013500': (5368788224, 5368788234),\
 'sub_1400111ef': (5368779247, 5368779252),\
 'sub_1400155dc': (5368796636, 5368796642),\
 'sub_1400111ea': (5368779242, 5368779247),\
 'sub_1400111d1': (5368779217, 5368779222),\
 'sub_140015420': (5368796192, 5368796229),\
 'sub_140014490': (5368792208, 5368792533),\
 'sub_1400110b4': (5368778932, 5368778937),\
 'sub_140013050': (5368787024, 5368787294),\
 'sub_1400110f5': (5368778997, 5368779002),\
 'sub_1400110f0': (5368778992, 5368778997),\
 'sub_140014310': (5368791824, 5368791890),\
 'sub_14001132f': (5368779567, 5368779572),\
 'sub_1400112d0': (5368779472, 5368779477),\
 'sub_14001132a': (5368779562, 5368779567),\
 'sub_1400112d5': (5368779477, 5368779482),\
 'sub_140012380': (5368783744, 5368783798),\
 'sub_140011041': (5368778817, 5368778822),\
 'sub_140011046': (5368778822, 5368778827),\
 'sub_140011127': (5368779047, 5368779052),\
 'sub_140011122': (5368779042, 5368779047),\
 'sub_140011285': (5368779397, 5368779402),\
 'sub_1400123d0': (5368783824, 5368783892),\
 'sub_14001123f': (5368779327, 5368779332),\
 'sub_140011280': (5368779392, 5368779397),\
 'sub_1400110ff': (5368779007, 5368779012),\
 'sub_140015630': (5368796720, 5368796723),\
 'sub_1400110fa': (5368779002, 5368779007),\
 'sub_140015576': (5368796534, 5368796540),\
 'sub_1400111e5': (5368779237, 5368779242),\
 'sub_140011136': (5368779062, 5368779067),\
 'sub_1400111e0': (5368779232, 5368779237),\
 'sub_140011087': (5368778887, 5368778892),\
 'sub_140011c70': (5368781936, 5368781999),\
 'sub_140011212': (5368779282, 5368779287),\
 'sub_1400110a5': (5368778917, 5368778922),\
 'sub_140013b70': (5368789872, 5368790062),\
 'sub_14001126c': (5368779372, 5368779377),\
 'sub_140011217': (5368779287, 5368779292),\
 'sub_1400110b9': (5368778937, 5368778942),\
 'sub_140011343': (5368779587, 5368779592),\
 'sub_14001106e': (5368778862, 5368778867),\
 'sub_1400155fa': (5368796666, 5368796672),\
 'sub_140012430': (5368783920, 5368784261),\
 'sub_1400155f4': (5368796660, 5368796666),\
 'sub_140012310': (5368783632, 5368783661),\
 'sub_14001110e': (5368779022, 5368779027),\
 'sub_140011348': (5368779592, 5368779597),\
 'sub_1400154b0': (5368796336, 5368796342),\
 'sub_1400154b6': (5368796342, 5368796348),\
 'sub_140011109': (5368779017, 5368779022),\
 'sub_140015528': (5368796456, 5368796462),\
 'sub_140011190': (5368779152, 5368779157),\
 'sub_140015522': (5368796450, 5368796456),\
 'sub_140011195': (5368779157, 5368779162),\
 'sub_1400154bc': (5368796348, 5368796354),\
 'sub_14001100f': (5368778767, 5368778772),\
 'sub_140011375': (5368779637, 5368779642),\
 'sub_140013e90': (5368790672, 5368790687),\
 'sub_140011064': (5368778852, 5368778857),\
 'sub_1400111b3': (5368779187, 5368779192),\
 'sub_14001134d': (5368779597, 5368779602),\
 'sub_140011104': (5368779012, 5368779017),\
 'sub_140013640': (5368788544, 5368788565),\
 'sub_140013de0': (5368790496, 5368790565),\
 'sub_140011069': (5368778857, 5368778862),\
 'sub_1400155e2': (5368796642, 5368796648),\
 'sub_1400110af': (5368778927, 5368778932),\
 'sub_140011267': (5368779367, 5368779372),\
 'sub_14001121c': (5368779292, 5368779297),\
 'sub_1400111b8': (5368779192, 5368779197),\
 'sub_140013720': (5368788768, 5368788789),\
 'sub_1400110aa': (5368778922, 5368778927),\
 'sub_140013270': (5368787568, 5368787746),\
 'sub_140011910': (5368781072, 5368781261),\
 'sub_14001130c': (5368779532, 5368779537),\
 'sub_1400112c1': (5368779457, 5368779462),\
 'sub_140012360': (5368783712, 5368783726),\
 'sub_14001119a': (5368779162, 5368779167),\
 'sub_14001552e': (5368796462, 5368796468),\
 'sub_14001119f': (5368779167, 5368779172),\
 'sub_140013e70': (5368790640, 5368790648),\
 'sub_1400154c2': (5368796354, 5368796360),\
 'sub_14001124e': (5368779342, 5368779347),\
 'sub_140011c50': (5368781904, 5368781912),\
 'sub_1400155d0': (5368796624, 5368796630),\
 'sub_140011361': (5368779617, 5368779622),\
 'sub_140011262': (5368779362, 5368779367),\
 'sub_1400155ca': (5368796618, 5368796624),\
 'sub_140011366': (5368779622, 5368779627),\
 'sub_14001131b': (5368779547, 5368779552),\
 'sub_140015610': (5368796688, 5368796691),\
 'sub_1400137a0': (5368788896, 5368789156),\
 'sub_1400154d4': (5368796372, 5368796378),\
 'sub_140015468': (5368796264, 5368796270),\
 'sub_140011154': (5368779092, 5368779097),\
 'sub_140011ff0': (5368782832, 5368782848),\
 'sub_140015462': (5368796258, 5368796264),\
 'sub_14001116d': (5368779117, 5368779122),\
 'sub_140015504': (5368796420, 5368796426),\
 'sub_14001118b': (5368779147, 5368779152),\
 'sub_1400110cd': (5368778957, 5368778962),\
 'sub_1400154c8': (5368796360, 5368796366),\
 'sub_140015660': (5368796768, 5368796771),\
 'sub_1400155ac': (5368796588, 5368796594),\
 'sub_140011a50': (5368781392, 5368781521),\
 'sub_140011186': (5368779142, 5368779147),\
 'sub_1400112b2': (5368779442, 5368779447),\
 'sub_14001108c': (5368778892, 5368778897),\
 'sub_140012260': (5368783456, 5368783477),\
 'sub_140011168': (5368779112, 5368779117),\
 'sub_140013660': (5368788576, 5368788677),\
 'sub_140011163': (5368779107, 5368779112),\
 'sub_140013dc0': (5368790464, 5368790467),\
 'sub_140011d40': (5368782144, 5368782202),\
 'sub_140012d50': (5368786256, 5368786264),\
 'sub_140011244': (5368779332, 5368779337),\
 'sub_1400155c4': (5368796612, 5368796618),\
 'sub_140011249': (5368779337, 5368779342),\
 'sub_140011316': (5368779542, 5368779547),\
 'sub_140011311': (5368779537, 5368779542),\
 'sub_1400112bc': (5368779452, 5368779457),\
 'sub_140012340': (5368783680, 5368783701),\
 'sub_140011082': (5368778882, 5368778887),\
 'sub_140011850': (5368780880, 5368781023),\
 'sub_1400110c8': (5368778952, 5368778957),\
 'sub_14001550a': (5368796426, 5368796432),\
 'sub_140012860': (5368784992, 5368785600),\
 'sub_140011ee0': (5368782560, 5368782593),\
 'sub_140011760': (5368780640, 5368780699),\
 'sub_14001107d': (5368778877, 5368778882),\
 'sub_140011384': (5368779652, 5368779657),\
 'sub_1400125e0': (5368784352, 5368784430),\
 'sub_1400154f8': (5368796408, 5368796414),\
 'sub_140014ae0': (5368793824, 5368794789),\
 'sub_1400154f2': (5368796402, 5368796408),\
 'sub_14001133e': (5368779582, 5368779587),\
 'sub_140011389': (5368779657, 5368779662),\
 'sub_14001114a': (5368779082, 5368779087),\
 'sub_140011014': (5368778772, 5368778777),\
 'sub_140015486': (5368796294, 5368796300),\
 'sub_140015480': (5368796288, 5368796294),\
 'sub_14001114f': (5368779087, 5368779092),\
 'sub_140011307': (5368779527, 5368779532),\
 'sub_14001122b': (5368779307, 5368779312),\
 'sub_140011019': (5368778777, 5368778782),\
 'sub_140015564': (5368796516, 5368796522),\
 'sub_1400110eb': (5368778987, 5368778992),\
 'sub_1400155b2': (5368796594, 5368796600),\
 'sub_140015640': (5368796736, 5368796743),\
 'sub_140013d50': (5368790352, 5368790355),\
 'sub_140013da0': (5368790432, 5368790435),\
 'sub_14001101e': (5368778782, 5368778787),\
 'sub_140014140': (5368791360, 5368791363),\
 'sub_140011145': (5368779077, 5368779082),\
 'sub_14001548c': (5368796300, 5368796306),\
 'sub_140011221': (5368779297, 5368779302),\
 'sub_1400169f0': (5368801776, 5368801778),\
 'sub_140011226': (5368779302, 5368779307),\
 'sub_140011339': (5368779577, 5368779582),\
 'sub_14001138e': (5368779662, 5368779667),\
 'sub_140012d10': (5368786192, 5368786229),\
 'sub_1400154fe': (5368796414, 5368796420),\
 'sub_1400155a0': (5368796576, 5368796582),\
 'sub_140013510': (5368788240, 5368788338),\
 'sub_140011334': (5368779572, 5368779577),\
 'sub_140013a30': (5368789552, 5368789677),\
 'sub_140012280': (5368783488, 5368783502),\
 'sub_140012b90': (5368785808, 5368786005),\
 'sub_140012840': (5368784960, 5368784980),\
 'sub_1400155d6': (5368796630, 5368796636),\
 'sub_14001556a': (5368796522, 5368796528),\
 'sub_140013b30': (5368789808, 5368789859),\
 'sub_140011140': (5368779072, 5368779077),\
 'sub_1400110e1': (5368778977, 5368778982),\
 'sub_1400110e6': (5368778982, 5368778987),\
 'sub_14001135c': (5368779612, 5368779617),\
 'sub_1400122a0': (5368783520, 5368783582),\
 'sub_1400143e0': (5368792032, 5368792062),\
 'sub_140011037': (5368778807, 5368778812),\
 'sub_140011032': (5368778802, 5368778807),\
 'sub_140013d80': (5368790400, 5368790421),\
 'sub_1400138f0': (5368789232, 5368789371),\
 'sub_14001120d': (5368779277, 5368779282),\
 'sub_140011131': (5368779057, 5368779062),\
 'sub_140014410': (5368792080, 5368792104),\
 'sub_140015540': (5368796480, 5368796486),\
 'sub_140015588': (5368796552, 5368796558),\
 'sub_140015546': (5368796486, 5368796492),\
 'sub_140015620': (5368796704, 5368796707),\
 'sub_1400135d0': (5368788432, 5368788461),\
 'sub_14001123a': (5368779322, 5368779327),\
 'sub_140012d80': (5368786304, 5368786310),\
 'sub_140012030': (5368782896, 5368782915),\
 'sub_1400122f0': (5368783600, 5368783619),\
 'sub_1400140b0': (5368791216, 5368791297),\
 'sub_1400111f9': (5368779257, 5368779262),\
 'sub_14001547a': (5368796282, 5368796288),\
 'sub_140013d30': (5368790320, 5368790326),\
 'sub_14001553a': (5368796474, 5368796480),\
 'sub_1400111f4': (5368779252, 5368779257),\
 'sub_140013740': (5368788800, 5368788873),\
 'sub_140013e40': (5368790592, 5368790629),\
 'sub_140011203': (5368779267, 5368779272),\
 'sub_140011750': (5368780624, 5368780627),\
 'sub_14001113b': (5368779067, 5368779072),\
 'sub_140012f80': (5368786816, 5368786971),\
 'sub_14001554c': (5368796492, 5368796498),\
 'sub_140014240': (5368791616, 5368791619),\
 'sub_140011208': (5368779272, 5368779277),\
 'sub_140011352': (5368779602, 5368779607),\
 'sub_140015582': (5368796546, 5368796552),\
 'sub_140011357': (5368779607, 5368779612),\
 'sub_1400154a4': (5368796324, 5368796330),\
 'sub_140012650': (5368784464, 5368784671),\
 'sub_14001103c': (5368778812, 5368778817),\
 'sub_140015534': (5368796468, 5368796474),\
 'sub_140012760': (5368784736, 5368784914),\
 'sub_140014480': (5368792192, 5368792195),\
 'sub_1400111fe': (5368779262, 5368779267),\
 'sub_1400136e0': (5368788704, 5368788750),\
 'sub_140011a00': (5368781312, 5368781371),\
 'sub_1400154ce': (5368796366, 5368796372),\
 'sub_1400111c7': (5368779207, 5368779212),\
 'sub_140013d60': (5368790368, 5368790390),\
 'sub_1400111c2': (5368779202, 5368779207),\
 'sub_140011050': (5368778832, 5368778837),\
 'sub_140011055': (5368778837, 5368778842),\
 'sub_140011113': (5368779027, 5368779032),\
 'sub_140011299': (5368779417, 5368779422),\
 'sub_140014430': (5368792112, 5368792167),\
 'sub_1400110be': (5368778942, 5368778947),\
 'sub_140012e00': (5368786432, 5368786485),\
 'sub_1400155ee': (5368796654, 5368796660),\
 'sub_140011118': (5368779032, 5368779037),\
 'sub_140011294': (5368779412, 5368779417),\
 'sub_14001137a': (5368779642, 5368779647),\
 'sub_140013590': (5368788368, 5368788413),\
 'sub_140012d60': (5368786272, 5368786295),\
 'sub_1400112ee': (5368779502, 5368779507),\
 'sub_140012010': (5368782864, 5368782890),\
 'sub_140012dd0': (5368786384, 5368786416),\
 'sub_140014630': (5368792624, 5368793310),\
 'sub_140013d10': (5368790288, 5368790294),\
 'sub_14001545c': (5368796252, 5368796258),\
 'sub_140013eb0': (5368790704, 5368791105),\
 'sub_1400111d6': (5368779222, 5368779227),\
 'sub_140011c60': (5368781920, 5368781928),\
 'sub_14001111d': (5368779037, 5368779042),\
 'sub_140014220': (5368791584, 5368791606),\
 'sub_140013d00': (5368790272, 5368790280),\
 'sub_14001129e': (5368779422, 5368779427),\
 'sub_140013c60': (5368790112, 5368790228),\
 'sub_140011370': (5368779632, 5368779637),\
 'sub_140016a10': (5368801808, 5368801814),\
 'sub_1400111cc': (5368779212, 5368779217),\
 'sub_14001105a': (5368778842, 5368778847),\
 'sub_14001105f': (5368778847, 5368778852),\
 'sub_140011023': (5368778787, 5368778792),\
 'sub_1400111db': (5368779227, 5368779232),\
 'sub_140015456': (5368796246, 5368796252),\
 'sub_140011181': (5368779137, 5368779142),\
 'sub_140017a60': (5368805984, 5368806016),\
 'sub_140011d90': (5368782224, 5368782472),\
 'sub_140015510': (5368796432, 5368796438),\
 'sub_140015516': (5368796438, 5368796444),\
 'sub_140011cf0': (5368782064, 5368782124),\
 'sub_1400112e9': (5368779497, 5368779502),\
 'sub_1400112e4': (5368779492, 5368779497),\
 'sub_140017a20': (5368805920, 5368805968),\
 'sub_1400117b0': (5368780720, 5368780846),\
 'sub_1400154ec': (5368796396, 5368796402),\
 'sub_140011073': (5368778867, 5368778872),\
 'sub_14001100a': (5368778762, 5368778767),\
 'sub_140017a90': (5368806032, 5368806093),\
 'sub_1400111a4': (5368779172, 5368779177),\
 'sub_140011078': (5368778872, 5368778877),\
 'sub_140013db0': (5368790448, 5368790451),\
 'sub_1400111a9': (5368779177, 5368779182),\
 'sub_140011172': (5368779122, 5368779127),\
 'sub_14001559a': (5368796570, 5368796576),\
 'sub_140011177': (5368779127, 5368779132),\
 'sub_140011276': (5368779382, 5368779387),\
 'sub_14001139d': (5368779677, 5368779682),\
 'sub_140011271': (5368779377, 5368779382),\
 'sub_140014990': (5368793488, 5368793747),\
 'sub_140012d40': (5368786240, 5368786248),\
 'sub_140015650': (5368796752, 5368796759),\
 'sub_140015570': (5368796528, 5368796534),\
 'sub_140013350': (5368787792, 5368787990),\
 'sub_1400110a0': (5368778912, 5368778917),\
 'sub_140013ad0': (5368789712, 5368789787),\
 'sub_1400112cb': (5368779467, 5368779472),\
 'sub_140012db0': (5368786352, 5368786378),\
 'sub_14001551c': (5368796444, 5368796450),\
 'sub_1400155a6': (5368796582, 5368796588),\
 'sub_14001557c': (5368796540, 5368796546),\
 'sub_140015600': (5368796672, 5368796678),\
 'sub_14001127b': (5368779387, 5368779392),\
 'sub_140011393': (5368779667, 5368779672),\
 'sub_140011398': (5368779672, 5368779677),\
 'sub_140011005': (5368778757, 5368778762),\
 'sub_1400154e0': (5368796384, 5368796390),\
 'sub_1400154e6': (5368796390, 5368796396),\
 'sub_1400111ae': (5368779182, 5368779187),\
 'sub_14001558e': (5368796558, 5368796564),\
 'sub_14001117c': (5368779132, 5368779137),\
 'sub_140015474': (5368796276, 5368796282),\
 'sub_140015594': (5368796564, 5368796570),\
 'sub_140012b60': (5368785760, 5368785791),\
 'sub_1400139a0': (5368789408, 5368789455),\
 'sub_1400155e8': (5368796648, 5368796654),\
 'sub_1400111bd': (5368779197, 5368779202),\
 'sub_140013dd0': (5368790480, 5368790488),\
 'sub_1400112b7': (5368779447, 5368779452),\
 'sub_1400113a2': (5368779682, 5368779687),\
 'sub_1400112c6': (5368779462, 5368779467),\
 'sub_1400131b0': (5368787376, 5368787521),\
 'sub_1400154da': (5368796378, 5368796384),\
 'sub_14001549e': (5368796318, 5368796324),\
 'sub_140011258': (5368779352, 5368779357),\
 'sub_14001102d': (5368778797, 5368778802),\
 'sub_14001555e': (5368796510, 5368796516),\
 'sub_140014fa0': (5368795040, 5368795958),\
 'sub_140014370': (5368791920, 5368791986),\
 'sub_140011159': (5368779097, 5368779102),\
 'sub_140011253': (5368779347, 5368779352),\
 'sub_1400112fd': (5368779517, 5368779522),\
 'sub_1400155b8': (5368796600, 5368796606),\
 'sub_14001137f': (5368779647, 5368779652),\
 'sub_140013d40': (5368790336, 5368790339),\
 'sub_140015450': (5368796240, 5368796246),\
 'sub_140011302': (5368779522, 5368779527),\
 'sub_1400139e0': (5368789472, 5368789535),\
 'sub_140012050': (5368782928, 5368783342),\
 'sub_1400112ad': (5368779437, 5368779442),\
 'sub_140011096': (5368778902, 5368778907),\
 'sub_140011091': (5368778897, 5368778902),\
 'sub_140013e80': (5368790656, 5368790664),\
 'sub_1400110d2': (5368778962, 5368778967),\
 'sub_14001546e': (5368796270, 5368796276),\
 'sub_1400110d7': (5368778967, 5368778972),\
 'sub_1400143d0': (5368792016, 5368792022),\
 'sub_1400112f3': (5368779507, 5368779512),\
 'sub_140014150': (5368791376, 5368791542),\
 'sub_1400155be': (5368796606, 5368796612),\
 'sub_1400112f8': (5368779512, 5368779517),\
 'sub_140012c90': (5368786064, 5368786164),\
 'sub_14001115e': (5368779102, 5368779107),\
 'sub_1400110c3': (5368778947, 5368778952),\
 'sub_140015492': (5368796306, 5368796312),\
 'sub_140013600': (5368788480, 5368788528),\
 'sub_140015558': (5368796504, 5368796510),\
 'sub_14001125d': (5368779357, 5368779362),\
 'sub_140011028': (5368778792, 5368778797),\
 'sub_14001136b': (5368779627, 5368779632),\
 'sub_140015552': (5368796498, 5368796504),\
 'sub_140015498': (5368796312, 5368796318),\
 'sub_140012f60': (5368786784, 5368786803),\
 'sub_140012e50': (5368786512, 5368786721),\
 'sub_1400110dc': (5368778972, 5368778977),\
 'sub_140011f10': (5368782608, 5368782786),\
 'sub_140012d90': (5368786320, 5368786346),\
 'sub_1400112a3': (5368779427, 5368779432),\
 'sub_140011b00': (5368781568, 5368781827),\
 'sub_1400112a8': (5368779432, 5368779437),\
 'sub_140013d20': (5368790304, 5368790307),\
 'sub_1400154aa': (5368796330, 5368796336),\
 'sub_140011cc0': (5368782016, 5368782051),\
 'sub_14001109b': (5368778907, 5368778912)}
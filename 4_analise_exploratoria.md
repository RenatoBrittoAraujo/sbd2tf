# Análise exploratória

Aqui notamos a topologia dos dados.

No fim desse arquivo se encontra o log que é output do programa. Todas as observações feitas aqui estão presentes no log. 

## Observações exploratórias 

- A média dos eventos ocorre em **2016**
- Lojas vendem **208 produtos por dia por loja**
- Existem **8 tipos de loja**
- Empresa presente em **21 países**, nos Estados Unidos, Japão, Brasil e Europa
- Vendendo um total de **144 produtos**
- Produtos organizados em **21 categorias**
- Produtos de **26 marcas**
- Produtos disponíveis em **23 cores**
- Preço médio dos produtos é **$ 127,00**
- Preço médio de compra dos produtos é **$ 70,00** 
- Margem de lucro simples é **$ 57** por produto

## Log gerado

Este log é denso em informações, o programa retorna esse arquivo

```
====================
DailySales: 8756
--------------
retailer_code: INTEGER
Sample: [1209, 1209, 1283]
Average: 1259.6070123343993
--------------
order_method_code: INTEGER
Sample: [1, 1, 1]
Average: 4.333942439470078
--------------
product_number: INTEGER
Sample: [76110, 87110, 124190]
Average: 99370.25239835541
--------------
quantity: INTEGER
Sample: [477, 267, 217]
Average: 208.21984924623115
--------------
date: DATETIME
Sample: [datetime.datetime(2018, 1, 16, 0, 0), datetime.datetime(2018, 5, 17, 0, 0), datetime.datetime(2016, 1, 20, 0, 0)]
Mean: 2016-07-07 03:58:47.638190848
--------------
unit_price: FLOAT
Sample: [40.52, 6.01, 43.85]
Average: 151.47626998629613
--------------
unit_sale_price: FLOAT
Sample: [39.71, 6.01, 43.85]
Average: 145.3455801735972
====================
OneK: 891
--------------
retailer_code: INTEGER
Sample: [1115, 1115, 1115]
Average: 1261.314253647587
--------------
product_number: INTEGER
Sample: [125110, 144180, 149140]
Average: 112941.71717171717
--------------
date: DATETIME
Sample: [datetime.datetime(2016, 2, 9, 0, 0), datetime.datetime(2016, 4, 21, 0, 0), datetime.datetime(2017, 2, 14, 0, 0)]
Mean: 2017-01-22 01:53:07.878788096
--------------
quantity: INTEGER
Sample: [46, 19, 11]
Average: 135.0909090909091
====================
Retailers: 562
--------------
retailer_code: INTEGER
Sample: [1101, 1115, 1123]
Average: 1478.459074733096
--------------
retailer_name: VARCHAR(100)
Sample: ['ActiForme', 'SportsClub', 'Anapurna']
There are 562 strings
There are 562 unique strings
Histogram: 0
ActiForme                1
La Slitta                1
Crèmes solaires          1
Contacts maisons         1
Construction Montagne    1
                        ..
Sports d'Hiver           1
Ski d'été                1
La poudreuse             1
Au vieux montagnard      1
Sportuniversum           1
Name: count, Length: 562, dtype: int64
row named Retailers.retailer_name Ignored, unknown type
--------------
type: VARCHAR(100)
Sample: ['Equipment Rental Store', 'Golf Shop', 'Direct Marketing']
There are 562 strings
There are 8 unique strings
Histogram: 0
Outdoors Shop             164
Sports Store              124
Golf Shop                  72
Department Store           50
Warehouse Store            46
Direct Marketing           45
Eyewear Store              31
Equipment Rental Store     30
Name: count, dtype: int64
row named Retailers.type Ignored, unknown type
--------------
country: VARCHAR(100)
Sample: ['France', 'France', 'France']
There are 562 strings
There are 21 unique strings
Histogram: 0
United States     104
Japan              49
France             43
Germany            38
United Kingdom     38
Canada             34
China              28
Switzerland        26
Italy              22
Singapore          20
Netherlands        19
Austria            18
Sweden             17
Brazil             16
Finland            15
Spain              14
Korea              13
Belgium            13
Australia          13
Denmark            12
Mexico             10
Name: count, dtype: int64
row named Retailers.country Ignored, unknown type
====================
Products: 274
--------------
product_number: INTEGER
Sample: [1110, 2110, 3110]
Average: 99041.16788321167
--------------
product: VARCHAR(100)
Sample: ['TrailChef Water Bag', 'TrailChef Canteen', 'TrailChef Kitchen Kit']
There are 274 strings
There are 144 unique strings
Histogram: 0
Inferno              11
TX                   10
Cat Eye               9
Zone                  9
Polar Sun             8
                     ..
Flicker Lantern       1
EverGlow Lamp         1
EverGlow Butane       1
EverGlow Kerosene     1
Single Edge           1
Name: count, Length: 144, dtype: int64
row named Products.product Ignored, unknown type
--------------
product_line: VARCHAR(100)
Sample: ['Camping Equipment', 'Camping Equipment', 'Camping Equipment']
There are 274 strings
There are 5 unique strings
Histogram: 0
Personal Accessories        182
Camping Equipment            41
Mountaineering Equipment     21
Outdoor Protection           15
Golf Equipment               15
Name: count, dtype: int64
row named Products.product_line Ignored, unknown type
--------------
product_type: VARCHAR(100)
Sample: ['Cooking Gear', 'Cooking Gear', 'Cooking Gear']
There are 274 strings
There are 21 unique strings
Histogram: 0
Eyewear                 90
Watches                 60
Navigation              12
Knives                  12
Lanterns                12
Cooking Gear            10
Binoculars               8
Climbing Accessories     7
Sleeping Bags            7
Tools                    6
Tents                    6
Packs                    6
Insect Repellents        5
Sunscreen                5
First Aid                5
Safety                   4
Rope                     4
Irons                    4
Woods                    4
Golf Accessories         4
Putters                  3
Name: count, dtype: int64
row named Products.product_type Ignored, unknown type
--------------
product_brand: VARCHAR(100)
Sample: ['TrailChef', 'TrailChef', 'TrailChef']
There are 274 strings
There are 26 unique strings
Histogram: 0
Trakker         36
Epoch           33
Relax           26
Polar           18
Antoni          17
Xray            15
Alpha           15
Extreme         11
Granite         11
TrailChef       10
Firefly          9
Hailstorm        8
Mountain Man     7
Star             6
Hibernator       6
Sun              5
Relief           5
Course Pro       5
Husky            5
EverGlow         5
Canyon Mule      5
Edge             4
BugShield        4
Seeker           3
Glacier          3
Blue Steel       2
Name: count, dtype: int64
row named Products.product_brand Ignored, unknown type
--------------
product_color: VARCHAR(100)
Sample: ['Clear', 'Brown', 'Unspecified']
There are 274 strings
There are 23 unique strings
Histogram: 0
Black           46
Silver          40
Red             30
Blue            28
Yellow          21
Brown           16
White           15
Orange          15
Camouflage      13
Green           13
Clear            9
Pink             8
Grey             4
Light Blue       3
Bronze           3
Multicolored     2
Mahogany         2
Dark Blue        1
Purple           1
Beige            1
Ash              1
Unspecified      1
Brass            1
Name: count, dtype: int64
row named Products.product_color Ignored, unknown type
--------------
unit_cost: FLOAT
Sample: [2.77, 6.92, 15.78]
Average: 70.20251824817518
--------------
unit_price: FLOAT
Sample: [6.59, 12.92, 23.8]
Average: 127.95051094890512
====================
Methods: 12
--------------
order_method_code: INTEGER
Sample: [1, 2, 3]
Average: 6.5
--------------
order_method_type: VARCHAR(100)
Sample: ['Fax', 'Telephone', 'Mail']
There are 12 strings
There are 8 unique strings
Histogram: 0
Other          5
Fax            1
Telephone      1
Mail           1
E-mail         1
Web            1
Sales visit    1
Special        1
Name: count, dtype: int64
row named Methods.order_method_type Ignored, unknown type



======== Finding correlations....
-------------
Correlations for DailySales
Columns: retailer_code and order_method_code have a correlation of 0.13812620854136395
Columns: order_method_code and date have a correlation of 0.42184425016107596
Columns: product_number and quantity have a correlation of -0.32307832349395194
Columns: product_number and date have a correlation of 0.2066195112509234
Columns: quantity and date have a correlation of -0.10465618003218864
Columns: quantity and unit_price have a correlation of -0.1902140606142792
Columns: quantity and unit_sale_price have a correlation of -0.1971950276822028
Columns: unit_price and unit_sale_price have a correlation of 0.9990749380635912
Found 8 correlations
-------------
Correlations for OneK
Columns: product_number and quantity have a correlation of -0.4008852730083267
Found 1 correlations
-------------
Correlations for Retailers
Columns: retailer_code and country have a correlation of -0.22414359108597992
Found 1 correlations
-------------
Correlations for Products
Columns: product_number and product have a correlation of 0.1041368523744069
Columns: product_number and product_line have a correlation of 0.7190994899365872
Columns: product and product_type have a correlation of 0.2632633989741638
Columns: product and unit_cost have a correlation of -0.11392758703354618
Columns: product and unit_price have a correlation of -0.11096359870467758
Columns: product_line and product_type have a correlation of -0.22210328597331316
Columns: product_line and product_brand have a correlation of 0.28828210529263404
Columns: product_line and product_color have a correlation of -0.1022442423209993
Columns: product_line and unit_cost have a correlation of -0.14035148602625983
Columns: product_line and unit_price have a correlation of -0.13443003314126017
Columns: product_type and unit_cost have a correlation of 0.25125534185353227
Columns: product_type and unit_price have a correlation of 0.25319657439492294
Columns: product_brand and product_color have a correlation of -0.12460378923986071
Columns: product_brand and unit_cost have a correlation of -0.19551742145696138
Columns: product_brand and unit_price have a correlation of -0.2224859661733094
Columns: unit_cost and unit_price have a correlation of 0.9893015228052024
Found 16 correlations
-------------
Correlations for Methods
Columns: order_method_code and order_method_type have a correlation of 0.2277013119590402
Found 1 correlations
```

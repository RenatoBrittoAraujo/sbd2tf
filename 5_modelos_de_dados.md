# Modelagem

As **perguntas** vieram de um processo iterativo de observar os dados e calcular respostas para as perguntas, todas elas estão implementadas no código e se fazem presentes nos logs.

As **conclusões** são derivadas a partir das respostas que a gente encontrou aqui.

Uma **rede neural** foi criada pra tentar prever as vendas por dia, é bastante pesada de treinar.

De preferência, os códigos que rodam sistemas pesados podem ser executados em **ambiente em cloud**. 

## Perguntas

Todas as perguntas foram **respondidas em código** no arquivo `5_modelo_de_dados.py`. 

#### quantas vendas são feitas? 
numero de vendas é 8756 do dia 2015-01-12 até 2018-07-20

#### quantos produtos foram vendidos?
numero de produtos vendidos é 1823173

#### qual é o gasto total da empresa?
custos é $ 489236.88

#### qual o lucro total da empresa com produtos?
lucros brutos é $ 918002.44

#### qual é o lucro líquido da empresa com produtos?
lucro líquido é $ 428765.6

#### qual é a margem de lucro média por venda?
média de margens de lucro é $ 69.89
média de margens de lucro percentual é 100.12757

#### qual é o produto mais lucrativo?
produto que gerou mais lucro é: Lady Hailstorm Titanium Woods Set gerando $ 40426.96

#### qual é o produto menos lucrativo?
produto que gerou menos lucro é: Retro gerando $ 0.0

(nunca foi vendido)

# Logs

```
numero de vendas é 8756 do dia 2015-01-12 até 2018-07-20
numero de produtos vendidos é 1823173
produto que gerou mais lucro é: Lady Hailstorm Titanium Woods Set gerando $ 40426.96
produto que gerou menos lucro é: Retro gerando $ 0.0
média de margens de lucro percentual é 100.12757
média de margens de lucro é 69.89
lucros brutos é $ 918002.44
custos é $ 489236.88
lucro líquido é $ 428765.6

--------
produto TrailChef Water Bag vendido 14 vezes lucrando 6.59 e custando 2.77 sendo o lucro liquido de 3.82 por unidade, totalizando 92.26 com custo de 38.78 que é um lucro liquido de 53.48 e margem percentual de 1.38
--------
produto TrailChef Canteen vendido 8 vezes lucrando 12.92 e custando 6.92 sendo o lucro liquido de 6.0 por unidade, totalizando 103.36 com custo de 55.36 que é um lucro liquido de 48.0 e margem percentual de 0.87
--------
produto TrailChef Kitchen Kit vendido 44 vezes lucrando 23.8 e custando 15.78 sendo o lucro liquido de 8.02 por unidade, totalizando 1047.2 com custo de 694.32 que é um lucro liquido de 352.88 e margem percentual de 0.51
--------
produto TrailChef Cup vendido 22 vezes lucrando 3.66 e custando 0.85 sendo o lucro liquido de 2.81 por unidade, totalizando 80.52 com custo de 18.7 que é um lucro liquido de 61.82 e margem percentual de 3.31
--------
produto TrailChef Cook Set vendido 27 vezes lucrando 54.93 e custando 34.41 sendo o lucro liquido de 20.52 por unidade, totalizando 1483.11 com custo de 929.07 que é um lucro liquido de 554.04 e margem percentual de 0.6
--------
produto TrailChef Deluxe Cook Set vendido 15 vezes lucrando 129.72 e custando 78.72 sendo o lucro liquido de 51.0 por unidade, totalizando 1945.8 com custo de 1180.8 que é um lucro liquido de 765.0 e margem percentual de 0.65
--------
produto TrailChef Single Flame vendido 14 vezes lucrando 66.77 e custando 46.38 sendo o lucro liquido de 20.39 por unidade, totalizando 934.78 com custo de 649.32 que é um lucro liquido de 285.46 e margem percentual de 0.44
--------
produto TrailChef Double Flame vendido 27 vezes lucrando 151.77 e custando 75.0 sendo o lucro liquido de 76.77 por unidade, totalizando 4097.79 com custo de 2025.0 que é um lucro liquido de 2072.79 e margem percentual de 1.02
--------
produto TrailChef Kettle vendido 31 vezes lucrando 13.22 e custando 5.07 sendo o lucro liquido de 8.15 por unidade, totalizando 409.82 com custo de 157.17 que é um lucro liquido de 252.65 e margem percentual de 1.61
--------
produto TrailChef Utensils vendido 18 vezes lucrando 19.29 e custando 9.68 sendo o lucro liquido de 9.61 por unidade, totalizando 347.22 com custo de 174.24 que é um lucro liquido de 172.98 e margem percentual de 0.99
--------
produto Star Lite vendido 35 vezes lucrando 370.13 e custando 250.0 sendo o lucro liquido de 120.13 por unidade, totalizando 12954.55 com custo de 8750.0 que é um lucro liquido de 4204.55 e margem percentual de 0.48
--------
produto Star Dome vendido 20 vezes lucrando 650.89 e custando 396.0 sendo o lucro liquido de 254.89 por unidade, totalizando 13017.8 com custo de 7920.0 que é um lucro liquido de 5097.8 e margem percentual de 0.64
--------
produto Star Gazer 2 vendido 22 vezes lucrando 582.42 e custando 392.57 sendo o lucro liquido de 189.85 por unidade, totalizando 12813.24 com custo de 8636.54 que é um lucro liquido de 4176.7 e margem percentual de 0.48
--------
produto Star Gazer 3 vendido 14 vezes lucrando 707.29 e custando 438.62 sendo o lucro liquido de 268.67 por unidade, totalizando 9902.06 com custo de 6140.68 que é um lucro liquido de 3761.38 e margem percentual de 0.61
--------
produto Star Gazer 6 vendido 59 vezes lucrando 831.88 e custando 490.0 sendo o lucro liquido de 341.88 por unidade, totalizando 49080.92 com custo de 28910.0 que é um lucro liquido de 20170.92 e margem percentual de 0.7
--------
produto Star Peg vendido 18 vezes lucrando 2.06 e custando 1.0 sendo o lucro liquido de 1.06 por unidade, totalizando 37.08 com custo de 18.0 que é um lucro liquido de 19.08 e margem percentual de 1.06
--------
produto Hibernator Lite vendido 20 vezes lucrando 90.09 e custando 60.0 sendo o lucro liquido de 30.09 por unidade, totalizando 1801.8 com custo de 1200.0 que é um lucro liquido de 601.8 e margem percentual de 0.5
--------
produto Hibernator vendido 28 vezes lucrando 146.83 e custando 86.0 sendo o lucro liquido de 60.83 por unidade, totalizando 4111.24 com custo de 2408.0 que é um lucro liquido de 1703.24 e margem percentual de 0.71
--------
produto Hibernator Extreme vendido 44 vezes lucrando 265.14 e custando 150.0 sendo o lucro liquido de 115.14 por unidade, totalizando 11666.16 com custo de 6600.0 que é um lucro liquido de 5066.16 e margem percentual de 0.77
--------
produto Hibernator Self - Inflating Mat vendido 28 vezes lucrando 127.27 e custando 56.72 sendo o lucro liquido de 70.55 por unidade, totalizando 3563.56 com custo de 1588.16 que é um lucro liquido de 1975.4 e margem percentual de 1.24
--------
produto Hibernator Pad vendido 49 vezes lucrando 41.31 e custando 18.83 sendo o lucro liquido de 22.48 por unidade, totalizando 2024.19 com custo de 922.67 que é um lucro liquido de 1101.52 e margem percentual de 1.19
--------
produto Hibernator Pillow vendido 51 vezes lucrando 17.65 e custando 8.37 sendo o lucro liquido de 9.28 por unidade, totalizando 900.15 com custo de 426.87 que é um lucro liquido de 473.28 e margem percentual de 1.11
--------
produto Hibernator Camp Cot vendido 30 vezes lucrando 104.48 e custando 65.41 sendo o lucro liquido de 39.07 por unidade, totalizando 3134.4 com custo de 1962.3 que é um lucro liquido de 1172.1 e margem percentual de 0.6
--------
produto Canyon Mule Climber Backpack vendido 29 vezes lucrando 76.86 e custando 52.5 sendo o lucro liquido de 24.36 por unidade, totalizando 2228.94 com custo de 1522.5 que é um lucro liquido de 706.44 e margem percentual de 0.46
--------
produto Canyon Mule Weekender Backpack vendido 52 vezes lucrando 285.89 e custando 165.91 sendo o lucro liquido de 119.98 por unidade, totalizando 14866.28 com custo de 8627.32 que é um lucro liquido de 6238.96 e margem percentual de 0.72
--------
produto Canyon Mule Journey Backpack vendido 47 vezes lucrando 370.86 e custando 213.33 sendo o lucro liquido de 157.53 por unidade, totalizando 17430.42 com custo de 10026.51 que é um lucro liquido de 7403.91 e margem percentual de 0.74
--------
produto Canyon Mule Extreme Backpack vendido 35 vezes lucrando 460.52 e custando 238.88 sendo o lucro liquido de 221.64 por unidade, totalizando 16118.2 com custo de 8360.8 que é um lucro liquido de 7757.4 e margem percentual de 0.93
--------
produto Canyon Mule Cooler vendido 31 vezes lucrando 32.69 e custando 15.27 sendo o lucro liquido de 17.42 por unidade, totalizando 1013.39 com custo de 473.37 que é um lucro liquido de 540.02 e margem percentual de 1.14
--------
produto Canyon Mule Carryall vendido 51 vezes lucrando 73.5 e custando 41.18 sendo o lucro liquido de 32.32 por unidade, totalizando 3748.5 com custo de 2100.18 que é um lucro liquido de 1648.32 e margem percentual de 0.78
--------
produto Firefly Lite vendido 16 vezes lucrando 14.77 e custando 6.75 sendo o lucro liquido de 8.02 por unidade, totalizando 236.32 com custo de 108.0 que é um lucro liquido de 128.32 e margem percentual de 1.19
--------
produto Firefly Mapreader vendido 44 vezes lucrando 16.29 e custando 7.5 sendo o lucro liquido de 8.79 por unidade, totalizando 716.76 com custo de 330.0 que é um lucro liquido de 386.76 e margem percentual de 1.17
--------
produto Firefly 2 vendido 48 vezes lucrando 27.37 e custando 16.38 sendo o lucro liquido de 10.99 por unidade, totalizando 1313.76 com custo de 786.24 que é um lucro liquido de 527.52 e margem percentual de 0.67
--------
produto Firefly 4 vendido 21 vezes lucrando 29.44 e custando 17.84 sendo o lucro liquido de 11.6 por unidade, totalizando 618.24 com custo de 374.64 que é um lucro liquido de 243.6 e margem percentual de 0.65
--------
produto Firefly Extreme vendido 27 vezes lucrando 53.04 e custando 29.1 sendo o lucro liquido de 23.94 por unidade, totalizando 1432.08 com custo de 785.7 que é um lucro liquido de 646.38 e margem percentual de 0.82
--------
produto Firefly Multi-light vendido 25 vezes lucrando 26.54 e custando 17.78 sendo o lucro liquido de 8.76 por unidade, totalizando 663.5 com custo de 444.5 que é um lucro liquido de 219.0 e margem percentual de 0.49
--------
produto EverGlow Single vendido 18 vezes lucrando 35.1 e custando 17.95 sendo o lucro liquido de 17.15 por unidade, totalizando 631.8 com custo de 323.1 que é um lucro liquido de 308.7 e margem percentual de 0.96
--------
produto EverGlow Double vendido 55 vezes lucrando 52.15 e custando 28.75 sendo o lucro liquido de 23.4 por unidade, totalizando 2868.25 com custo de 1581.25 que é um lucro liquido de 1287.0 e margem percentual de 0.81
--------
produto EverGlow Kerosene vendido 23 vezes lucrando 31.55 e custando 20.0 sendo o lucro liquido de 11.55 por unidade, totalizando 725.65 com custo de 460.0 que é um lucro liquido de 265.65 e margem percentual de 0.58
--------
produto EverGlow Butane vendido 43 vezes lucrando 67.73 e custando 40.63 sendo o lucro liquido de 27.1 por unidade, totalizando 2912.39 com custo de 1747.09 que é um lucro liquido de 1165.3 e margem percentual de 0.67
--------
produto EverGlow Lamp vendido 48 vezes lucrando 27.81 e custando 14.76 sendo o lucro liquido de 13.05 por unidade, totalizando 1334.88 com custo de 708.48 que é um lucro liquido de 626.4 e margem percentual de 0.88
--------
produto Flicker Lantern vendido 23 vezes lucrando 35.09 e custando 15.62 sendo o lucro liquido de 19.47 por unidade, totalizando 807.07 com custo de 359.26 que é um lucro liquido de 447.81 e margem percentual de 1.25
--------
produto Husky Rope 50 vendido 43 vezes lucrando 160.0 e custando 100.91 sendo o lucro liquido de 59.09 por unidade, totalizando 6880.0 com custo de 4339.13 que é um lucro liquido de 2540.87 e margem percentual de 0.59
--------
produto Husky Rope 60 vendido 46 vezes lucrando 190.0 e custando 126.51 sendo o lucro liquido de 63.49 por unidade, totalizando 8740.0 com custo de 5819.46 que é um lucro liquido de 2920.54 e margem percentual de 0.5
--------
produto Husky Rope 100 vendido 46 vezes lucrando 346.66 e custando 227.69 sendo o lucro liquido de 118.97 por unidade, totalizando 15946.36 com custo de 10473.74 que é um lucro liquido de 5472.62 e margem percentual de 0.52
--------
produto Husky Rope 200 vendido 45 vezes lucrando 574.98 e custando 370.35 sendo o lucro liquido de 204.63 por unidade, totalizando 25874.1 com custo de 16665.75 que é um lucro liquido de 9208.35 e margem percentual de 0.55
--------
produto Granite Climbing Helmet vendido 41 vezes lucrando 74.0 e custando 52.54 sendo o lucro liquido de 21.46 por unidade, totalizando 3034.0 com custo de 2154.14 que é um lucro liquido de 879.86 e margem percentual de 0.41
--------
produto Husky Harness vendido 37 vezes lucrando 65.0 e custando 43.77 sendo o lucro liquido de 21.23 por unidade, totalizando 2405.0 com custo de 1619.49 que é um lucro liquido de 785.51 e margem percentual de 0.49
--------
produto Husky Harness Extreme vendido 43 vezes lucrando 110.0 e custando 53.93 sendo o lucro liquido de 56.07 por unidade, totalizando 4730.0 com custo de 2318.99 que é um lucro liquido de 2411.01 e margem percentual de 1.04
--------
produto Granite Signal Mirror vendido 39 vezes lucrando 33.0 e custando 15.47 sendo o lucro liquido de 17.53 por unidade, totalizando 1287.0 com custo de 603.33 que é um lucro liquido de 683.67 e margem percentual de 1.13
--------
produto Granite Carabiner vendido 38 vezes lucrando 4.0 e custando 1.96 sendo o lucro liquido de 2.04 por unidade, totalizando 152.0 com custo de 74.48 que é um lucro liquido de 77.52 e margem percentual de 1.04
--------
produto Granite Belay vendido 39 vezes lucrando 70.0 e custando 34.47 sendo o lucro liquido de 35.53 por unidade, totalizando 2730.0 com custo de 1344.33 que é um lucro liquido de 1385.67 e margem percentual de 1.03
--------
produto Granite Pulley vendido 41 vezes lucrando 38.0 e custando 18.35 sendo o lucro liquido de 19.65 por unidade, totalizando 1558.0 com custo de 752.35 que é um lucro liquido de 805.65 e margem percentual de 1.07
--------
produto Firefly Climbing Lamp vendido 45 vezes lucrando 39.99 e custando 21.57 sendo o lucro liquido de 18.42 por unidade, totalizando 1799.55 com custo de 970.65 que é um lucro liquido de 828.9 e margem percentual de 0.85
--------
produto Firefly Charger vendido 46 vezes lucrando 52.99 e custando 22.36 sendo o lucro liquido de 30.63 por unidade, totalizando 2437.54 com custo de 1028.56 que é um lucro liquido de 1408.98 e margem percentual de 1.37
--------
produto Firefly Rechargeable Battery vendido 46 vezes lucrando 8.0 e custando 3.15 sendo o lucro liquido de 4.85 por unidade, totalizando 368.0 com custo de 144.9 que é um lucro liquido de 223.1 e margem percentual de 1.54
--------
produto Granite Chalk Bag vendido 44 vezes lucrando 18.0 e custando 8.53 sendo o lucro liquido de 9.47 por unidade, totalizando 792.0 com custo de 375.32 que é um lucro liquido de 416.68 e margem percentual de 1.11
--------
produto Granite Ice vendido 43 vezes lucrando 80.0 e custando 38.97 sendo o lucro liquido de 41.03 por unidade, totalizando 3440.0 com custo de 1675.71 que é um lucro liquido de 1764.29 e margem percentual de 1.05
--------
produto Granite Hammer vendido 40 vezes lucrando 79.98 e custando 56.88 sendo o lucro liquido de 23.1 por unidade, totalizando 3199.2 com custo de 2275.2 que é um lucro liquido de 924.0 e margem percentual de 0.41
--------
produto Granite Shovel vendido 39 vezes lucrando 59.99 e custando 37.07 sendo o lucro liquido de 22.92 por unidade, totalizando 2339.61 com custo de 1445.73 que é um lucro liquido de 893.88 e margem percentual de 0.62
--------
produto Granite Grip vendido 40 vezes lucrando 20.0 e custando 9.89 sendo o lucro liquido de 10.11 por unidade, totalizando 800.0 com custo de 395.6 que é um lucro liquido de 404.4 e margem percentual de 1.02
--------
produto Granite Axe vendido 39 vezes lucrando 40.0 e custando 19.52 sendo o lucro liquido de 20.48 por unidade, totalizando 1560.0 com custo de 761.28 que é um lucro liquido de 798.72 e margem percentual de 1.05
--------
produto Granite Extreme vendido 39 vezes lucrando 80.0 e custando 46.52 sendo o lucro liquido de 33.48 por unidade, totalizando 3120.0 com custo de 1814.28 que é um lucro liquido de 1305.72 e margem percentual de 0.72
--------
produto Mountain Man Analog vendido 34 vezes lucrando 48.88 e custando 30.0 sendo o lucro liquido de 18.88 por unidade, totalizando 1661.92 com custo de 1020.0 que é um lucro liquido de 641.92 e margem percentual de 0.63
--------
produto Mountain Man Digital vendido 39 vezes lucrando 41.61 e custando 20.0 sendo o lucro liquido de 21.61 por unidade, totalizando 1622.79 com custo de 780.0 que é um lucro liquido de 842.79 e margem percentual de 1.08
--------
produto Mountain Man Deluxe vendido 25 vezes lucrando 81.55 e custando 39.0 sendo o lucro liquido de 42.55 por unidade, totalizando 2038.75 com custo de 975.0 que é um lucro liquido de 1063.75 e margem percentual de 1.09
--------
produto Mountain Man Combination vendido 16 vezes lucrando 98.01 e custando 45.0 sendo o lucro liquido de 53.01 por unidade, totalizando 1568.16 com custo de 720.0 que é um lucro liquido de 848.16 e margem percentual de 1.18
--------
produto Mountain Man Extreme vendido 34 vezes lucrando 294.38 e custando 116.19 sendo o lucro liquido de 178.19 por unidade, totalizando 10008.92 com custo de 3950.46 que é um lucro liquido de 6058.46 e margem percentual de 1.53
--------
produto Polar Sun vendido 48 vezes lucrando 61.84 e custando 26.08 sendo o lucro liquido de 35.76 por unidade, totalizando 2968.32 com custo de 1251.84 que é um lucro liquido de 1716.48 e margem percentual de 1.37
--------
produto Polar Ice vendido 61 vezes lucrando 109.25 e custando 49.69 sendo o lucro liquido de 59.56 por unidade, totalizando 6664.25 com custo de 3031.09 que é um lucro liquido de 3633.16 e margem percentual de 1.2
--------
produto Polar Sports vendido 12 vezes lucrando 122.7 e custando 58.88 sendo o lucro liquido de 63.82 por unidade, totalizando 1472.4 com custo de 706.56 que é um lucro liquido de 765.84 e margem percentual de 1.08
--------
produto Polar Wave vendido 36 vezes lucrando 95.62 e custando 40.95 sendo o lucro liquido de 54.67 por unidade, totalizando 3442.32 com custo de 1474.2 que é um lucro liquido de 1968.12 e margem percentual de 1.34
--------
produto Polar Extreme vendido 36 vezes lucrando 148.3 e custando 72.5 sendo o lucro liquido de 75.8 por unidade, totalizando 5338.8 com custo de 2610.0 que é um lucro liquido de 2728.8 e margem percentual de 1.05
--------
produto Single Edge vendido 6 vezes lucrando 12.78 e custando 8.56 sendo o lucro liquido de 4.22 por unidade, totalizando 76.68 com custo de 51.36 que é um lucro liquido de 25.32 e margem percentual de 0.49
--------
produto Double Edge vendido 6 vezes lucrando 16.64 e custando 11.43 sendo o lucro liquido de 5.21 por unidade, totalizando 99.84 com custo de 68.58 que é um lucro liquido de 31.26 e margem percentual de 0.46
--------
produto Edge Extreme vendido 33 vezes lucrando 119.69 e custando 80.0 sendo o lucro liquido de 39.69 por unidade, totalizando 3949.77 com custo de 2640.0 que é um lucro liquido de 1309.77 e margem percentual de 0.5
--------
produto Bear Edge vendido 17 vezes lucrando 40.52 e custando 23.53 sendo o lucro liquido de 16.99 por unidade, totalizando 688.84 com custo de 400.01 que é um lucro liquido de 288.83 e margem percentual de 0.72
--------
produto Bear Survival Edge vendido 4 vezes lucrando 92.29 e custando 45.7 sendo o lucro liquido de 46.59 por unidade, totalizando 369.16 com custo de 182.8 que é um lucro liquido de 186.36 e margem percentual de 1.02
--------
produto Seeker 35 vendido 9 vezes lucrando 105.29 e custando 71.19 sendo o lucro liquido de 34.1 por unidade, totalizando 947.61 com custo de 640.71 que é um lucro liquido de 306.9 e margem percentual de 0.48
--------
produto Seeker 50 vendido 21 vezes lucrando 134.11 e custando 92.58 sendo o lucro liquido de 41.53 por unidade, totalizando 2816.31 com custo de 1944.18 que é um lucro liquido de 872.13 e margem percentual de 0.45
--------
produto Seeker Extreme vendido 14 vezes lucrando 182.67 e custando 94.12 sendo o lucro liquido de 88.55 por unidade, totalizando 2557.38 com custo de 1317.68 que é um lucro liquido de 1239.7 e margem percentual de 0.94
--------
produto Seeker Mini vendido 22 vezes lucrando 85.56 e custando 40.0 sendo o lucro liquido de 45.56 por unidade, totalizando 1882.32 com custo de 880.0 que é um lucro liquido de 1002.32 e margem percentual de 1.14
--------
produto Glacier Basic vendido 17 vezes lucrando 32.72 e custando 19.93 sendo o lucro liquido de 12.79 por unidade, totalizando 556.24 com custo de 338.81 que é um lucro liquido de 217.43 e margem percentual de 0.64
--------
produto Glacier Deluxe vendido 8 vezes lucrando 96.44 e custando 54.44 sendo o lucro liquido de 42.0 por unidade, totalizando 771.52 com custo de 435.52 que é um lucro liquido de 336.0 e margem percentual de 0.77
--------
produto Glacier GPS vendido 12 vezes lucrando 113.97 e custando 74.06 sendo o lucro liquido de 39.91 por unidade, totalizando 1367.64 com custo de 888.72 que é um lucro liquido de 478.92 e margem percentual de 0.54
--------
produto Glacier GPS Extreme vendido 18 vezes lucrando 359.6 e custando 176.47 sendo o lucro liquido de 183.13 por unidade, totalizando 6472.8 com custo de 3176.46 que é um lucro liquido de 3296.34 e margem percentual de 1.04
--------
produto BugShield Natural vendido 25 vezes lucrando 6.0 e custando 1.86 sendo o lucro liquido de 4.14 por unidade, totalizando 150.0 com custo de 46.5 que é um lucro liquido de 103.5 e margem percentual de 2.23
--------
produto BugShield Spray vendido 30 vezes lucrando 6.01 e custando 1.83 sendo o lucro liquido de 4.18 por unidade, totalizando 180.3 com custo de 54.9 que é um lucro liquido de 125.4 e margem percentual de 2.28
--------
produto BugShield Lotion Lite vendido 61 vezes lucrando 7.0 e custando 1.88 sendo o lucro liquido de 5.12 por unidade, totalizando 427.0 com custo de 114.68 que é um lucro liquido de 312.32 e margem percentual de 2.72
--------
produto BugShield Lotion vendido 48 vezes lucrando 7.0 e custando 2.33 sendo o lucro liquido de 4.67 por unidade, totalizando 336.0 com custo de 111.84 que é um lucro liquido de 224.16 e margem percentual de 2.0
--------
produto BugShield Extreme vendido 32 vezes lucrando 7.0 e custando 2.42 sendo o lucro liquido de 4.58 por unidade, totalizando 224.0 com custo de 77.44 que é um lucro liquido de 146.56 e margem percentual de 1.89
--------
produto Sun Blocker vendido 14 vezes lucrando 5.0 e custando 1.95 sendo o lucro liquido de 3.05 por unidade, totalizando 70.0 com custo de 27.3 que é um lucro liquido de 42.7 e margem percentual de 1.56
--------
produto Sun Shelter Stick vendido 26 vezes lucrando 5.0 e custando 1.96 sendo o lucro liquido de 3.04 por unidade, totalizando 130.0 com custo de 50.96 que é um lucro liquido de 79.04 e margem percentual de 1.55
--------
produto Sun Shelter 15 vendido 27 vezes lucrando 4.99 e custando 1.79 sendo o lucro liquido de 3.2 por unidade, totalizando 134.73 com custo de 48.33 que é um lucro liquido de 86.4 e margem percentual de 1.79
--------
produto Sun Shelter 30 vendido 20 vezes lucrando 5.0 e custando 1.85 sendo o lucro liquido de 3.15 por unidade, totalizando 100.0 com custo de 37.0 que é um lucro liquido de 63.0 e margem percentual de 1.7
--------
produto Sun Shield vendido 26 vezes lucrando 6.0 e custando 2.76 sendo o lucro liquido de 3.24 por unidade, totalizando 156.0 com custo de 71.76 que é um lucro liquido de 84.24 e margem percentual de 1.17
--------
produto Compact Relief Kit vendido 31 vezes lucrando 23.0 e custando 9.03 sendo o lucro liquido de 13.97 por unidade, totalizando 713.0 com custo de 279.93 que é um lucro liquido de 433.07 e margem percentual de 1.55
--------
produto Deluxe Family Relief Kit vendido 51 vezes lucrando 35.0 e custando 16.68 sendo o lucro liquido de 18.32 por unidade, totalizando 1785.0 com custo de 850.68 que é um lucro liquido de 934.32 e margem percentual de 1.1
--------
produto Calamine Relief vendido 12 vezes lucrando 6.0 e custando 2.83 sendo o lucro liquido de 3.17 por unidade, totalizando 72.0 com custo de 33.96 que é um lucro liquido de 38.04 e margem percentual de 1.12
--------
produto Aloe Relief vendido 28 vezes lucrando 5.23 e custando 1.92 sendo o lucro liquido de 3.31 por unidade, totalizando 146.44 com custo de 53.76 que é um lucro liquido de 92.68 e margem percentual de 1.72
--------
produto Insect Bite Relief vendido 11 vezes lucrando 6.0 e custando 2.76 sendo o lucro liquido de 3.24 por unidade, totalizando 66.0 com custo de 30.36 que é um lucro liquido de 35.64 e margem percentual de 1.17
--------
produto Hailstorm Steel Irons vendido 60 vezes lucrando 498.45 e custando 239.71 sendo o lucro liquido de 258.74 por unidade, totalizando 29907.0 com custo de 14382.6 que é um lucro liquido de 15524.4 e margem percentual de 1.08
--------
produto Hailstorm Titanium Irons vendido 62 vezes lucrando 928.53 e custando 466.57 sendo o lucro liquido de 461.96 por unidade, totalizando 57568.86 com custo de 28927.34 que é um lucro liquido de 28641.52 e margem percentual de 0.99
--------
produto Lady Hailstorm Steel Irons vendido 53 vezes lucrando 532.75 e custando 277.76 sendo o lucro liquido de 254.99 por unidade, totalizando 28235.75 com custo de 14721.28 que é um lucro liquido de 13514.47 e margem percentual de 0.92
--------
produto Lady Hailstorm Titanium Irons vendido 50 vezes lucrando 889.02 e custando 441.97 sendo o lucro liquido de 447.05 por unidade, totalizando 44451.0 com custo de 22098.5 que é um lucro liquido de 22352.5 e margem percentual de 1.01
--------
produto Hailstorm Titanium Woods Set vendido 61 vezes lucrando 1271.08 e custando 648.72 sendo o lucro liquido de 622.36 por unidade, totalizando 77535.88 com custo de 39571.92 que é um lucro liquido de 37963.96 e margem percentual de 0.96
--------
produto Hailstorm Steel Woods Set vendido 66 vezes lucrando 798.56 e custando 384.45 sendo o lucro liquido de 414.11 por unidade, totalizando 52704.96 com custo de 25373.7 que é um lucro liquido de 27331.26 e margem percentual de 1.08
--------
produto Lady Hailstorm Titanium Woods Set vendido 56 vezes lucrando 1359.72 e custando 637.81 sendo o lucro liquido de 721.91 por unidade, totalizando 76144.32 com custo de 35717.36 que é um lucro liquido de 40426.96 e margem percentual de 1.13
--------
produto Lady Hailstorm Steel Woods Set vendido 54 vezes lucrando 910.82 e custando 449.13 sendo o lucro liquido de 461.69 por unidade, totalizando 49184.28 com custo de 24253.02 que é um lucro liquido de 24931.26 e margem percentual de 1.03
--------
produto Course Pro Putter vendido 54 vezes lucrando 74.96 e custando 31.12 sendo o lucro liquido de 43.84 por unidade, totalizando 4047.84 com custo de 1680.48 que é um lucro liquido de 2367.36 e margem percentual de 1.41
--------
produto Blue Steel Putter vendido 70 vezes lucrando 90.95 e custando 41.2 sendo o lucro liquido de 49.75 por unidade, totalizando 6366.5 com custo de 2884.0 que é um lucro liquido de 3482.5 e margem percentual de 1.21
--------
produto Blue Steel Max Putter vendido 56 vezes lucrando 180.63 e custando 89.41 sendo o lucro liquido de 91.22 por unidade, totalizando 10115.28 com custo de 5006.96 que é um lucro liquido de 5108.32 e margem percentual de 1.02
--------
produto Course Pro Golf and Tee Set vendido 60 vezes lucrando 10.64 e custando 2.88 sendo o lucro liquido de 7.76 por unidade, totalizando 638.4 com custo de 172.8 que é um lucro liquido de 465.6 e margem percentual de 2.69
--------
produto Course Pro Umbrella vendido 66 vezes lucrando 12.81 e custando 6.08 sendo o lucro liquido de 6.73 por unidade, totalizando 845.46 com custo de 401.28 que é um lucro liquido de 444.18 e margem percentual de 1.11
--------
produto Course Pro Golf Bag vendido 61 vezes lucrando 219.3 e custando 79.7 sendo o lucro liquido de 139.6 por unidade, totalizando 13377.3 com custo de 4861.7 que é um lucro liquido de 8515.6 e margem percentual de 1.75
--------
produto Course Pro Gloves vendido 44 vezes lucrando 10.71 e custando 2.54 sendo o lucro liquido de 8.17 por unidade, totalizando 471.24 com custo de 111.76 que é um lucro liquido de 359.48 e margem percentual de 3.22
--------
produto Bella vendido 0 vezes lucrando 67.5 e custando 36.43 sendo o lucro liquido de 31.07 por unidade, totalizando 0.0 com custo de 0.0 que é um lucro liquido de 0.0 e margem percentual de 0.85
--------
produto Capri vendido 7 vezes lucrando 38.3 e custando 25.17 sendo o lucro liquido de 13.13 por unidade, totalizando 268.1 com custo de 176.19 que é um lucro liquido de 91.91 e margem percentual de 0.52
--------
produto Cat Eye vendido 32 vezes lucrando 26.69 e custando 18.05 sendo o lucro liquido de 8.64 por unidade, totalizando 854.08 com custo de 577.6 que é um lucro liquido de 276.48 e margem percentual de 0.48
--------
produto Venue vendido 120 vezes lucrando 71.93 e custando 41.5 sendo o lucro liquido de 30.43 por unidade, totalizando 8631.6 com custo de 4980.0 que é um lucro liquido de 3651.6 e margem percentual de 0.73
--------
produto Dante vendido 87 vezes lucrando 43.2 e custando 26.04 sendo o lucro liquido de 17.16 por unidade, totalizando 3758.4 com custo de 2265.48 que é um lucro liquido de 1492.92 e margem percentual de 0.66
--------
produto Fairway vendido 61 vezes lucrando 20.37 e custando 12.1 sendo o lucro liquido de 8.27 por unidade, totalizando 1242.57 com custo de 738.1 que é um lucro liquido de 504.47 e margem percentual de 0.68
--------
produto Inferno vendido 0 vezes lucrando 67.5 e custando 36.15 sendo o lucro liquido de 31.35 por unidade, totalizando 0.0 com custo de 0.0 que é um lucro liquido de 0.0 e margem percentual de 0.87
--------
produto Infinity vendido 49 vezes lucrando 225.46 e custando 118.57 sendo o lucro liquido de 106.89 por unidade, totalizando 11047.54 com custo de 5809.93 que é um lucro liquido de 5237.61 e margem percentual de 0.9
--------
produto Lux vendido 61 vezes lucrando 165.85 e custando 85.92 sendo o lucro liquido de 79.93 por unidade, totalizando 10116.85 com custo de 5241.12 que é um lucro liquido de 4875.73 e margem percentual de 0.93
--------
produto Max Gizmo vendido 23 vezes lucrando 39.31 e custando 18.15 sendo o lucro liquido de 21.16 por unidade, totalizando 904.13 com custo de 417.45 que é um lucro liquido de 486.68 e margem percentual de 1.17
--------
produto Maximus vendido 82 vezes lucrando 81.22 e custando 40.65 sendo o lucro liquido de 40.57 por unidade, totalizando 6660.04 com custo de 3333.3 que é um lucro liquido de 3326.74 e margem percentual de 1.0
--------
produto Opera Vision vendido 22 vezes lucrando 110.0 e custando 50.4 sendo o lucro liquido de 59.6 por unidade, totalizando 2420.0 com custo de 1108.8 que é um lucro liquido de 1311.2 e margem percentual de 1.18
--------
produto Pocket Gizmo vendido 0 vezes lucrando 12.2 e custando 4.87 sendo o lucro liquido de 7.33 por unidade, totalizando 0.0 com custo de 0.0 que é um lucro liquido de 0.0 e margem percentual de 1.51
--------
produto Ranger Vision vendido 35 vezes lucrando 163.48 e custando 76.28 sendo o lucro liquido de 87.2 por unidade, totalizando 5721.8 com custo de 2669.8 que é um lucro liquido de 3052.0 e margem percentual de 1.14
--------
produto Sam vendido 1 vezes lucrando 47.3 e custando 28.36 sendo o lucro liquido de 18.94 por unidade, totalizando 47.3 com custo de 28.36 que é um lucro liquido de 18.94 e margem percentual de 0.67
--------
produto Trail Master vendido 14 vezes lucrando 365.0 e custando 234.9 sendo o lucro liquido de 130.1 por unidade, totalizando 5110.0 com custo de 3288.6 que é um lucro liquido de 1821.4 e margem percentual de 0.55
--------
produto Trail Scout vendido 30 vezes lucrando 238.0 e custando 152.9 sendo o lucro liquido de 85.1 por unidade, totalizando 7140.0 com custo de 4587.0 que é um lucro liquido de 2553.0 e margem percentual de 0.56
--------
produto Trail Star vendido 18 vezes lucrando 154.0 e custando 88.57 sendo o lucro liquido de 65.43 por unidade, totalizando 2772.0 com custo de 1594.26 que é um lucro liquido de 1177.74 e margem percentual de 0.74
--------
produto Trendi vendido 68 vezes lucrando 50.0 e custando 30.02 sendo o lucro liquido de 19.98 por unidade, totalizando 3400.0 com custo de 2041.36 que é um lucro liquido de 1358.64 e margem percentual de 0.67
--------
produto TX vendido 18 vezes lucrando 188.0 e custando 103.68 sendo o lucro liquido de 84.32 por unidade, totalizando 3384.0 com custo de 1866.24 que é um lucro liquido de 1517.76 e margem percentual de 0.81
--------
produto Legend vendido 1 vezes lucrando 220.0 e custando 115.72 sendo o lucro liquido de 104.28 por unidade, totalizando 220.0 com custo de 115.72 que é um lucro liquido de 104.28 e margem percentual de 0.9
--------
produto Zodiak vendido 3 vezes lucrando 107.98 e custando 62.04 sendo o lucro liquido de 45.94 por unidade, totalizando 323.94 com custo de 186.12 que é um lucro liquido de 137.82 e margem percentual de 0.74
--------
produto Zone vendido 118 vezes lucrando 31.42 e custando 20.96 sendo o lucro liquido de 10.46 por unidade, totalizando 3707.56 com custo de 2473.28 que é um lucro liquido de 1234.28 e margem percentual de 0.5
--------
produto Hawk Eye vendido 55 vezes lucrando 41.41 e custando 24.66 sendo o lucro liquido de 16.75 por unidade, totalizando 2277.55 com custo de 1356.3 que é um lucro liquido de 921.25 e margem percentual de 0.68
--------
produto Retro vendido 0 vezes lucrando 62.65 e custando 33.56 sendo o lucro liquido de 29.09 por unidade, totalizando 0.0 com custo de 0.0 que é um lucro liquido de 0.0 e margem percentual de 0.87
--------
produto Astro Pilot vendido 55 vezes lucrando 145.0 e custando 90.34 sendo o lucro liquido de 54.66 por unidade, totalizando 7975.0 com custo de 4968.7 que é um lucro liquido de 3006.3 e margem percentual de 0.61
--------
produto Sky Pilot vendido 37 vezes lucrando 358.0 e custando 234.22 sendo o lucro liquido de 123.78 por unidade, totalizando 13246.0 com custo de 8666.14 que é um lucro liquido de 4579.86 e margem percentual de 0.53
--------
produto Auto Pilot vendido 5 vezes lucrando 235.0 e custando 152.98 sendo o lucro liquido de 82.02 por unidade, totalizando 1175.0 com custo de 764.9 que é um lucro liquido de 410.1 e margem percentual de 0.54
--------
produto Kodiak vendido 13 vezes lucrando 120.3 e custando 66.67 sendo o lucro liquido de 53.63 por unidade, totalizando 1563.9 com custo de 866.71 que é um lucro liquido de 697.19 e margem percentual de 0.8
```

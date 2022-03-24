""" Match schedule imported from TBA before competition. Use scraping program found at
    https://github.com/core2062/TBAScraper to quickly get this data that is
    formatted correctly,
    Format: blue team1, blue team3, blue team3, red team1, red team2, red team3 """

SCHEDULE = [
(1739, 706, 8531, 930, 1732,537), (1714,2194,2077,5148,4787,1091), (5096,6574,6643,7417,3596,3418),(93,2574,1259,6381,7237,1306),(8802,6421,3197,2506,8701,2202),(6823,7915,7900,6223,2830,2062),(8803,1792,1675,8847,8700,4786),(706,3418,1714,2194,8531,7417),(2077,93,5148,2574,6643,930),(4787,537,8802,6421,1259,6574),(1306,2506,1732,2830,5096,6823),(1091,8803,7237,7900,2202,1792),(1675,8847,6223,3596,3197,1739),(8701,4786,6381,7915,2062,8700),(8531,930,93,6574,8802,2194),(6643,1714,6421,1259,6823,706),(1792,7417,2574,537,7900,2506),(2202,6223,4787,3418,1306,8847),(8700,1091,3596,4786,1739,2830),(1732,6381,7915,3197,2077,8803),(2062,5148,8701,7237,1675,5096)
# (5350,5133,3734,63,1675,8160),(3110,8014,4645,7411,7608,1756),(111,3410,2136,101,1739,8029),(2338,5822,3197,2039,7560,4292),(6381,6237,8096,4702,1781,5934),(1625,2451,5148,8184,2151,5125),(4096,1732,2358,5847,2022,3352),(8122,6906,7237,3488,2725,3061),(930,4296,4241,3067,4787,4191),(63,111,8096,6237,2338,1756),(1781,5350,5148,3110,1739,7608),(7560,2022,2151,3734,5934,8029),(4096,1625,2136,6381,5133,5822),(2725,4191,8014,5847,2039,2451),(8160,3061,4645,101,4296,3488),(8184,1675,3197,7237,4787,5125),(3410,930,3352,4702,8122,4292),(3067,4241,2358,6906,7411,1732),(2022,8029,6237,7608,5148,5822),(7560,3734,2136,4096,111,2725),(3110,7237,4296,5125,2338,5133),(3352,1625,8184,1675,4645,8096),(2039,3488,3067,1739,3410,4241),(4292,1756,6906,1781,8160,2451),(3061,3197,4191,7411,2358,4702),(930,5847,101,6381,2151,5350),(4787,63,5934,8014,8122,1732),(6237,2136,3110,4296,3734,3067),(7237,5133,2725,1739,4645,2022),(4191,4096,1675,1781,3061,111),(2151,5847,4702,6906,4241,5822),(8122,7608,5934,2039,1625,1756),(3410,8014,2338,5350,8184,8160),(5148,101,1732,7411,930,7560),(8029,3488,6381,3352,2451,3197),(63,5125,2358,8096,4292,4787),(1756,4241,4702,4296,1675,2022),(2725,5934,3067,5133,8184,1781),(8014,7560,101,1625,4191,7237),(3197,3410,3734,7608,3352,3061),(8029,5125,6906,4645,5350,63),(1732,6237,5847,2136,4292,3488),(6381,1739,7411,8122,2338,4787),(2451,5822,4096,8096,8160,930),(111,2358,2039,5148,2151,3110),(6906,2022,3410,1675,7560,1625),(4191,6237,5133,8184,1756,8029),(3067,7608,63,5847,6381,7237),(4645,1781,2338,2136,3197,930),(8160,5125,1739,3061,1732,2151),(4241,5350,2039,101,8096,2358),(4292,7411,4296,5934,4096,3488),(4787,8014,5148,4702,3734,2725),(3352,5822,8122,111,3110,2451),(930,6381,8184,5125,1756,2022),(1781,8029,1675,2358,2338,5847),(5350,7237,4096,2151,2039,6237),(4292,3734,7608,4191,4296,1739),(63,2136,5133,4241,5148,3352),(1732,3110,8096,3410,2725,8122),(5822,5934,101,3197,8014,6906),(8160,7411,3488,1625,4702,111),(7560,3067,3061,4787,2451,4645),(2022,1781,930,2039,63,4296),(3110,8029,8122,4241,4096,8184),(8096,3352,8014,3197,6237,1739),(3488,1732,1675,5148,4191,6381),(3061,5847,5350,5934,111,7560),(8160,7608,1625,4787,2358,2725),(3734,101,1756,5822,3067,5125),(2151,4292,3410,5133,4645,7411),(2451,6906,4702,2338,2136,7237),(5847,5148,4296,3197,8096,8122),(1675,1739,3061,6237,930,1625),(2725,3110,8160,2022,63,6381),(4645,111,5125,5934,4241,8014),(1756,3488,7560,2358,2136,5350),(5822,4787,2151,4191,3410,1781),(7237,4702,3067,8029,4096,4292),(6906,8184,2039,3352,7411,3734),(2451,1732,2338,5133,101,7608),(5125,8122,4241,7560,8160,6237),(2136,8096,2151,8014,3061,2022),(4296,6381,111,2358,7237,3410),(4292,4645,5847,3734,2039,3110),(5934,3352,4191,2338,3067,5148),(1739,4702,4096,8184,101,63),(7608,930,4787,3488,6906,5133),(2451,2725,7411,5350,1675,5822),(1756,3197,1781,1732,8029,1625)
]

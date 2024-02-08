import pandas as pd

## transform the metadata file from txt file to df

### stations_id
stations_id_string = """
00003
00044
00052
00071
00073
00078
00091
00096
00102
00106
00125
00131
00142
00150
00151
00154
00161
00164
00167
00175
00181
00183
00191
00198
00217
00222
00232
00257
00259
00268
00282
00284
00294
00298
00303
00314
00320
00326
00330
00342
00348
00350
00361
00368
00377
00379
00390
00399
00400
00403
00410
00420
00424
00427
00430
00433
00445
00450
00460
00474
00535
00553
00554
00555
00591
00596
00598
00599
00603
00617
00656
00662
00685
00691
00701
00704
00722
00755
00757
00760
00766
00769
00817
00840
00850
00853
00856
00860
00863
00867
00876
00879
00880
00891
00896
00917
00919
00920
00953
00954
00963
00979
00982
00983
00991
00998
01001
01048
01050
01051
01052
01072
01076
01078
01103
01107
01130
01161
01197
01200
01207
01214
01219
01221
01224
01228
01239
01246
01255
01262
01266
01270
01279
01281
01297
01300
01303
01327
01332
01339
01341
01346
01357
01358
01411
01420
01421
01424
01425
01426
01443
01451
01468
01473
01490
01503
01504
01515
01526
01544
01550
01572
01580
01583
01584
01587
01590
01602
01605
01612
01639
01645
01666
01684
01691
01694
01721
01735
01736
01757
01758
01759
01766
01792
01803
01832
01833
01834
01863
01869
01886
01892
01902
01957
01960
01964
01975
01981
02014
02023
02039
02044
02074
02080
02081
02088
02110
02115
02158
02166
02167
02171
02174
02201
02211
02244
02252
02261
02290
02303
02306
02315
02319
02323
02338
02362
02374
02385
02410
02423
02429
02437
02444
02456
02477
02480
02483
02485
02486
02488
02494
02497
02503
02521
02522
02532
02542
02559
02564
02565
02575
02578
02597
02600
02601
02618
02627
02629
02638
02641
02656
02667
02680
02691
02693
02700
02704
02708
02712
02738
02750
02761
02773
02794
02796
02812
02814
02829
02856
02878
02886
02905
02907
02920
02925
02928
02932
02947
02951
02953
02961
02968
02985
03015
03023
03028
03031
03032
03034
03042
03044
03083
03085
03086
03093
03098
03126
03137
03139
03145
03147
03155
03158
03164
03166
03167
03170
03181
03196
03204
03226
03231
03234
03244
03245
03246
03254
03257
03268
03271
03274
03278
03284
03287
03289
03307
03319
03321
03340
03348
03362
03366
03376
03379
03382
03385
03390
03402
03404
03426
03442
03478
03484
03485
03490
03509
03513
03527
03540
03545
03552
03571
03575
03577
03591
03603
03605
03612
03621
03623
03631
03639
03659
03660
03667
03668
03671
03679
03702
03730
03734
03739
03761
03791
03811
03815
03821
03836
03857
03875
03879
03897
03904
03925
03927
03939
03946
03975
03987
04018
04024
04032
04036
04039
04063
04094
04104
04127
04154
04160
04169
04174
04175
04177
04189
04261
04271
04275
04280
04287
04294
04300
04301
04323
04336
04339
04347
04349
04350
04354
04371
04373
04377
04393
04411
04445
04464
04466
04477
04480
04485
04501
04508
04517
04548
04559
04560
04584
04592
04605
04625
04629
04642
04651
04665
04692
04702
04703
04704
04706
04709
04719
04745
04748
04752
04763
04813
04841
04857
04878
04887
04896
04911
04926
04927
04928
04931
04933
04978
04997
05009
05014
05017
05029
05046
05049
05064
05068
05097
05099
05100
05109
05111
05133
05142
05146
05149
05155
05158
05229
05275
05277
05279
05280
05282
05300
05335
05347
05349
05371
05397
05404
05419
05424
05426
05431
05433
05440
05467
05480
05490
05516
05538
05541
05546
05562
05629
05640
05643
05663
05664
05665
05676
05688
05692
05705
05715
05717
05719
05731
05732
05745
05750
05779
05792
05797
05800
05802
05822
05825
05832
05839
05856
05871
05906
05930
05941
06093
06105
06109
06129
06157
06158
06159
06163
06170
06182
06184
06186
06192
06197
06199
06217
06242
06243
06244
06245
06246
06247
06254
06255
06256
06258
06259
06260
06262
06263
06264
06265
06266
06272
06273
06275
06305
06310
06312
06314
06336
06337
06344
06346
06347
07075
07099
07105
07106
07135
07187
07244
07298
07319
07321
07329
07330
07331
07341
07343
07350
07351
07364
07367
07368
07369
07370
07373
07374
07389
07393
07394
07395
07396
07403
07410
07412
07419
07420
07424
07427
07428
07431
07432
13667
13670
13674
13675
13696
13700
13710
13711
13713
13776
13777
13904
13965
14003
15000
15207
15444
15555
15813
19171
19172
19207

"""
stations_id_list = stations_id_string.split("\n")
#### drop empty strings
stations_id_list = list(filter(None, stations_id_list))

### stationshoehe
stationshoehe_string = """202
 44
 46
759
374
 64
300
 50
  0
500
742
296
511
215
382
516
 75
 54
 11
413
 30
 42
217
164
670
393
462
240
275
622
240
282
110
  3
 55
234
350
120
455
103
127
540
550
 69
210
304
610
 36
 60
 51
 33
 61
 36
 46
 36
 48
 85
120
362
599
417
 25
 23
110
 45
 15
 62
 62
147
 47
607
 81
585
  4
  7
 11
135
340
445
 83
477
 68
293
895
 45
416
551
 80
585
344
314
 68
 69
  5
170
162
169
108
481
  0
 38
314
420
419
359
696
 97
228
112
119
 80
107
692
 37
592
346
 18
384
463
  3
558
431
  5
  0
201
  0
540
104
226
446
 18
316
268
284
156
351
150
147
471
 76
  0
486
655
213
747
100
125
121
103
 65
237
  2
797
414
394
  6
172
519
242
 47
719
 80
111
823
673
536
 37
177
 35
311
203
340
 12
239
167
 59
506
628
 26
  2
  2
 12
 48
 27
 35
436
307
913
258
 56
444
 72
413
 93
102
328
 11
  4
 55
501
203
404
518
110
561
522
 57
  4
350
344
302
272
236
  1
295
008
271
565
977
 10
  8
 80
685
110
 39
328
  3
376
364
712
 20
 21
155
  7
728
108
839
489
271
516
 31
505
487
374
112
231
716
705
 28
 17
432
 14
282
193
822
732
128
 46
974
 90
 96
 91
289
378
380
416
 76
742
428
776
310
520
415
 40
 41
156
687
617
 91
117
539
550
  7
365
356
138
131
286
 20
854
  0
 43
321
 98
 22
157
 92
 25
496
230
 22
 57
 15
 15
 16
387
 79
195
509
 30
390
413
 12
187
639
547
  9
360
 81
429
107
450
158
614
630
181
 19
278
900
314
415
354
240
453
356
984
239
 76
265
241
243
406
 63
515
521
515
529
755
 62
127
149
 81
380
486
111
 78
845
500
195
236
 38
452
163
 64
350
459
451
 25
435
110
 12
 26
627
485
369
314
280
518
515
806
232
596
276
 11
150
 95
244
314
886
549
409
  2
152
332
630
385
387
522
 81
550
 40
142
204
 11
 41
441
365
347
345
478
131
 40
283
116
534
442
  5
 32
386
415
360
589
102
461
319
193
293
251
339
457
135
 29
518
  5
155
609
501
 43
993
230
296
938
649
635
608
398
265
444
356
277
 59
 37
 21
189
431
229
645
581
508
358
445
169
 75
185
626
265
318
 -0
  2
504
734
 40
351
224
286
314
371
401
395
196
 33
  7
633
387
501
846
 37
 80
 10
132
261
 68
560
295
  1
 50
318
567
159
719
105
349
176
 33
246
380
352
236
 73
920
440
477
264
328
553
 24
380
439
832
 85
233
  3
551
263
187
571
105
 10
 68
118
296
677
 82
881
 88
268
 49
134
235
395
  9
 51
264
877
956
349
615
615
 42
 40
 50
 -0
476
497
 98
  1
686
 62
 15
 52
291
  4
454
  8
 27
 39
404
  6
268
115
258
 17
190
 64
 96
145
180
368
307
 19
351
201
461
524
385
412
445
457
 36
112
284
 36
327
193
  1
362
306
288
 59
168
531
305
429
187
719
105
565
194
 62
  4
435
160
465
159
467
119
689
585
115
 74
144
312
475
499
  3
 46
 83
116
622
351
740
672
350
340
389
246
457
 17
397
604
 71
274
 24
237
 75
 60
203
490
289
386
 85
109
  3
619
728
231
317
593
815
 40
 13
 48
 16"""
stationshoehe_list = stationshoehe_string.split("\n")

### geoBreite
geobreite_string = """50.7827
52.9336
53.6623
48.2156
48.6183
52.4853
50.7446
52.9437
53.8633
51.7976
47.8342
51.0881
48.4060
49.7273
49.4691
48.0197
50.4237
53.0316
53.8409
49.2964
52.8761
54.6791
49.9694
51.3744
47.8774
50.5908
48.4253
48.7270
47.8064
48.5293
49.8743
49.8800
52.3199
54.3405
52.0613
51.1604
49.9666
51.7204
49.5617
52.3170
50.4135
51.6715
47.6344
52.8152
49.1070
50.9075
50.9837
52.5198
52.6310
52.4537
52.4040
52.5447
52.5000
52.3807
52.5644
52.4676
51.8218
49.9186
49.2641
48.1252
50.0372
51.8380
51.8293
51.5026
53.3911
54.0027
50.7285
50.7055
50.7293
51.8730
51.7234
52.2915
49.9017
53.0451
53.5332
53.4451
51.7986
49.5182
47.9625
53.3629
50.1745
52.2817
51.0306
50.4313
52.5959
50.7913
47.8843
52.2731
51.7904
50.3066
51.3040
51.7667
51.7759
53.8713
51.0778
49.8809
49.8697
49.8564
49.7619
54.1796
52.5881
50.7364
48.5701
48.5562
50.9116
48.7968
51.6451
51.1278
51.0221
51.0249
52.2174
49.4719
48.0135
51.2960
48.1003
49.8520
54.6282
48.8777
48.9895
54.0691
50.2705
48.2012
53.3449
53.3707
48.1378
54.1651
47.8516
51.8418
49.1661
48.3477
54.2992
50.9829
49.6497
49.5653
51.2041
51.2540
51.4041
50.7119
48.4832
52.9157
54.6000
47.8748
49.9807
50.4283
50.5309
50.0259
50.1474
50.1269
50.1214
52.3397
48.0232
53.8277
48.4538
49.1869
47.6454
53.0643
51.1190
48.2000
50.5668
52.5129
47.4830
50.9593
49.9859
50.7719
47.9242
48.9481
51.4942
48.4330
52.3875
50.8812
50.6017
50.9656
54.8273
51.1621
51.5002
53.6058
49.6640
48.7894
53.5731
54.0967
54.1000
54.2437
52.1344
52.7553
54.0714
49.1129
49.0851
50.8519
50.2667
53.3154
48.4878
51.9298
49.1273
51.5138
51.4831
49.9445
53.6332
53.4776
52.4644
48.7918
51.9002
51.6520
48.3752
49.4206
49.3981
48.6849
51.0411
54.1750
48.8042
51.0167
49.7672
50.8520
51.6255
54.5750
50.7370
47.7327
50.8992
50.3123
47.8009
54.3162
54.3194
51.7657
47.8823
51.8529
52.3333
50.5651
54.4752
49.6927
48.7111
47.6894
53.9897
54.4570
50.9251
53.5322
47.5938
50.0643
51.1803
48.9170
49.4262
48.7701
51.7329
50.5014
50.6266
48.6765
49.0382
51.2963
47.8652
47.7233
54.3776
54.3378
49.1804
53.9995
50.2240
49.7363
50.2218
50.8458
51.5554
51.7612
48.1054
51.5185
50.3519
50.8645
50.2840
48.6707
50.1855
48.8302
51.7511
47.6652
47.6952
47.6448
50.2524
48.2510
49.4283
52.9362
53.9156
48.3647
48.5122
48.0772
51.9173
51.3909
48.2175
48.1849
54.7903
48.7654
51.3932
51.3151
51.4347
51.1333
53.1007
47.8597
54.4996
50.9894
50.9383
52.2085
52.5181
51.7854
51.6336
55.0110
50.4505
50.5617
52.7198
51.9267
53.8773
53.8025
52.9724
51.2452
52.1029
49.9656
48.2166
54.1800
48.7548
50.1015
52.5468
50.8492
50.6511
50.6621
54.4937
49.4875
53.3222
50.7335
51.7259
50.5611
51.1294
47.9821
47.9833
50.3667
52.7155
49.4797
48.1694
48.8548
49.5070
48.5377
49.6692
49.7177
50.7281
47.4779
49.7644
51.1313
50.4383
51.7209
48.9721
48.2790
52.5176
48.1632
48.1441
48.1660
48.1369
48.3851
51.9494
51.5660
50.3574
53.5468
48.7085
48.3115
50.5346
53.1020
50.5003
50.8923
50.8446
49.3440
52.9037
49.8174
49.3570
53.3585
50.6743
49.3895
48.5334
52.6711
48.8253
50.8294
53.7123
53.7647
50.3391
50.3602
49.4258
49.5030
48.6321
47.6187
47.8780
47.3984
49.1280
49.4521
49.2070
53.1763
51.2960
52.2553
51.0872
50.4538
47.6362
49.1510
48.5779
54.0893
49.5354
48.9329
47.9345
49.1912
50.4818
49.4777
52.3812
48.1877
54.3643
51.7953
51.3895
53.7331
52.4461
47.8062
49.0425
50.9906
51.1800
48.7425
48.6703
52.2887
47.5590
48.9726
48.1479
47.8753
54.1803
53.1289
49.2162
49.3849
48.4704
48.1815
49.8502
49.6468
49.2128
49.2231
51.5909
48.9569
47.5619
48.7832
52.1042
52.8568
50.3518
54.3279
49.9195
51.7658
50.5679
54.5275
47.8208
50.3447
50.7250
50.6545
50.2968
48.7859
50.1847
49.1644
50.4925
48.3667
49.3278
50.6441
53.6424
54.5166
52.8911
51.9040
49.5281
50.8534
48.1000
48.0719
47.5776
48.2718
49.9996
49.2447
52.9604
51.3691
50.3746
51.0607
50.0806
53.6946
53.5534
51.6646
48.6656
54.6654
48.8275
48.7896
48.7693
48.8281
48.6883
48.7091
50.6390
50.9771
53.7610
53.2758
50.4002
49.4737
49.8576
47.8991
51.2897
51.5833
54.0654
49.7326
49.7479
53.5998
48.0311
51.3344
53.7445
52.9414
49.5679
48.3837
52.1601
48.0453
49.2445
50.8119
51.6194
53.9224
51.1197
50.2596
50.8963
51.5039
53.5196
50.4973
49.6662
48.4024
50.9751
51.0177
49.3758
53.0333
49.5534
49.0115
47.7035
51.5763
51.8454
54.5283
47.8827
50.1321
52.1206
48.6516
51.8891
53.5503
53.1864
53.4618
48.2953
47.8180
52.3962
47.7004
49.6051
49.7704
52.4626
51.2256
51.2051
47.6783
54.6928
52.9664
51.0314
50.7313
47.4210
50.6879
49.0280
49.0007
52.8630
52.6198
53.1007
53.3881
48.5451
49.9463
49.5063
54.6410
47.6754
53.2139
54.3194
53.3837
51.0594
53.6411
49.2249
52.9542
54.1654
52.0192
48.7757
53.5333
50.1989
49.8083
51.8664
54.2484
49.2406
50.4088
49.2506
49.3650
49.0423
47.6213
47.6078
53.5408
49.4667
47.9100
47.6845
49.0210
49.3328
48.7695
47.7738
51.4140
52.3613
52.0304
50.8426
52.5075
48.6705
51.2061
54.1049
49.5314
51.0507
50.0132
51.7663
50.3940
48.2070
50.0579
48.7020
52.0111
47.8350
52.0714
47.9655
49.7636
53.1424
54.5268
48.7374
51.1507
50.5467
51.4633
48.6099
50.0900
50.6200
49.1088
53.3176
51.6818
51.9643
51.0007
49.1623
49.3910
53.5984
52.0813
52.7461
51.4492
50.0315
48.6595
50.5084
47.7955
50.7513
50.0083
50.6610
51.1044
47.7724
54.0188
50.4167
48.0130
52.6423
48.0006
51.5088
49.2943
52.0818
51.5966
51.3329
48.5734
50.6820
51.0899
52.1789
52.2467
55.0000
48.2639
47.8619
50.7983
51.2835
48.4418
47.8761
52.5126
54.0039
54.0246
53.8178"""
geobreite_list = geobreite_string.split("\n")

### geoLaenge
geolaenge_string = """ 6.0941
 8.2370
10.1990
 8.9784
13.0620
 7.9125
 9.3450
12.8518
 8.1275
10.4429
10.8667
12.9326
11.3117
 8.1164
11.8546
12.2925
 7.4202
13.9908
13.6854
10.5751
11.5042
13.4344
 9.9114
11.2920
11.3643
12.7139
10.9417
 8.2457
 7.6387
 8.2727
10.9206
10.8800
 9.4300
12.7108
13.4997
14.5042
11.5198
 8.0577
 8.9673
 8.1694
 7.5886
10.7268
13.0109
 9.9248
 7.9967
11.2665
 8.3683
13.4057
13.5021
13.3017
13.7309
13.5598
13.4667
13.5306
13.3088
13.4020
11.7110
 7.0664
 6.6868
 9.7639
 7.3079
 6.6107
 6.5365
 7.2289
10.6878
11.1908
 7.0839
 7.1467
 7.2040
 6.8863
10.6021
10.4464
 9.4281
 8.7981
 8.5761
 9.1390
10.6183
 9.3213
 7.9983
 9.9435
 7.0595
 9.0890
 8.8146
12.6114
10.0296
12.8720
12.5404
10.0163
10.3470
10.9679
13.0096
14.2833
14.3168
 8.7060
10.8619
 8.6779
 8.6796
 8.5929
 7.0542
 7.4587
 8.3424
 8.2672
10.4985
10.5599
13.7087
 8.4921
13.5747
13.7543
13.8470
13.7750
12.1641
 8.1929
 8.5343
 6.7686
11.9872
10.4991
 9.3649
11.2349
10.1312
 9.0105
12.2742
 8.1088
 7.1909
 7.2236
 7.8351
 6.3460
 8.7673
 8.0607
 8.8483
11.8134
 9.3162
10.9608
11.0075
10.9729
10.0138
 8.1565
 6.9677
 6.7905
12.7241
10.1885
11.1500
 8.0038
11.8376
12.9536
10.0479
 8.5213
 8.6746
 8.6694
 8.6604
14.5080
 7.8343
 9.2493
 8.4090
11.3080
 9.4795
 7.9020
 9.2799
11.2667
 9.6532
11.3942
11.0621
 6.0392
 7.9548
13.7732
 8.6474
11.4289
 6.2463
 7.9930
12.1602
12.1289
 8.6439
 9.0500
 9.5058
14.9506
 9.9507
12.1034
11.2239
13.6290
10.6797
13.4056
13.4500
13.9102
 7.6969
 7.4815
12.3238
13.1338
13.2801
10.4665
 9.1854
13.9339
10.2608
 8.3005
10.7448
11.9499
11.9671
 6.3821
 9.9881
 9.8957
 9.6779
10.7062
10.5699
11.1366
 8.9800
 8.6676
 8.7251
10.1420
 6.1042
 7.8920
 8.4430
14.7500
 7.3356
 9.7377
10.3695
13.1044
 7.6525
 8.1627
14.7456
11.8760
11.0108
 9.5385
10.6732
13.1666
11.6961
 9.4953
 7.5500
 7.4843
 9.0564
 7.3263
11.5363
10.0416
 9.5697
 9.5203
11.5830
 7.8806
 7.9597
 8.9930
 8.4891
 9.6871
 7.7557
10.7876
 6.2688
 6.5264
10.1455
11.2961
 8.3641
 9.4424
10.6007
10.3348
10.1424
10.0929
 9.9800
11.4341
10.0792
10.1781
 8.4469
10.4803
13.8845
 6.0954
 8.7548
12.9065
 7.5906
 7.1575
10.4456
11.2173
 8.4698
11.4872
12.0094
11.0805
 9.1307
11.7438
11.3209
10.4163
11.9016
12.4093
12.2790
 7.8280
 9.7644
10.9144
13.0878
11.8786
 9.9097
10.8507
 8.9514
12.5121
10.3123
12.4462
12.2396
 8.0348
11.4864
 8.2308
10.2737
 6.9777
14.2094
14.1180
 7.3081
 8.8388
 8.3945
 8.4125
11.6350
 8.2386
 7.7472
13.8797
10.6915
10.6989
11.1374
 7.6425
11.5827
 8.2139
11.2965
10.5528
12.2118
 6.8009
14.5453
 8.7745
13.1469
 7.9603
11.2411
10.6277
11.9321
10.8815
11.5109
10.3771
13.4328
10.1384
10.2333
 7.3167
 7.3176
 9.7832
 8.9433
12.9189
 6.5215
 9.2734
 9.0085
 9.0997
11.7838
11.2653
 9.2530
 6.3608
 7.8061
 9.8351
 8.8735
12.5024
14.1232
11.5429
11.6000
11.5011
11.7094
 9.4837
 7.5906
14.7008
 8.7506
13.1914
11.2147
10.3773
 7.0853
13.0421
11.1345
 9.4050
 7.3720
 7.2297
12.8071
11.8638
 8.1405
13.0502
 6.4240
 9.9666
10.2427
 9.2229
10.5067
 6.6601
 7.1519
 8.6584
 6.9501
 6.8697
11.2539
11.0549
 9.3261
12.1665
 7.8288
10.2759
 9.3525
12.4365
 9.5176
 8.1824
13.0928
 8.0534
11.9293
10.2211
10.3892
11.6896
13.4694
10.8773
 6.3789
 8.6973
 9.2869
 7.5879
12.1300
11.5357
13.0622
11.2206
13.4771
11.1320
11.5412
 9.8776
 8.5906
 9.6206
12.1019
 7.6958
 7.2505
 8.9240
 7.9939
 7.3866
 7.7721
 8.3301
 9.4596
12.1280
12.0808
 9.3398
11.1035
10.1732
 8.9687
 8.6356
 7.8710
 7.8837
 7.1077
 7.0168
10.5691
 9.0711
 7.9399
13.3146
 8.7521
11.1319
10.0034
 8.6031
 8.9672
10.6533
11.8041
 9.5487
 8.1860
 9.5533
10.4539
10.7696
 6.4194
 8.6451
12.0791
12.6175
 9.1226
11.8000
12.0871
11.1936
11.3871
 9.1420
11.7297
10.1885
 7.0417
 7.9966
 9.2500
 9.1943
 9.7404
13.0273
 7.5981
 8.8787
 9.7930
10.8800
11.1828
 9.9266
11.0467
 8.8735
 9.6097
10.8811
 9.8648
 9.8050
12.5597
 9.2167
 9.1814
 9.2000
 9.2235
 9.2147
10.0228
12.3419
12.5574
 8.9857
11.3888
 7.0385
12.3542
 8.1460
 6.4437
13.0000
12.7655
 6.6131
 6.6583
13.3039
12.5396
 8.9132
14.0698
10.5289
10.1969
 9.9524
11.1759
 8.4608
 8.5374
 9.1280
 9.5749
10.2267
13.6744
 8.3607
10.5483
 9.1118
12.6654
 9.9427
12.1844
11.6946
11.3076
11.3544
 8.1212
11.8000
 6.8120
10.9308
12.0119
 7.8879
10.7686
11.0606
11.1576
 8.3169
12.4586
 8.6801
12.6446
 7.6672
12.4949
13.6099
 8.2391
 9.7970
10.6892
 8.1057
 8.3659
 9.9576
 9.4245
 7.1052
 7.2000
 8.3801
 8.5271
13.3268
12.1495
13.7516
10.9848
12.4329
13.2385
13.2137
 8.6989
12.7867
11.0455
 7.2287
13.3532
 7.2645
 8.5584
10.0238
12.4698
10.4704
 9.8051
14.3728
14.4266
 8.0809
10.6085
 7.3197
10.3519
14.7254
12.1743
 8.1667
 7.8651
 7.8458
 9.2710
13.0419
 6.9351
 7.4890
 8.4422
 9.0804
 9.1733
 8.2167
 8.1813
 9.9528
 6.3968
 7.5838
 9.4409
 9.6033
 9.7040
 9.8737
 8.8219
 8.6500
12.3867
10.9626
10.2518
11.8551
 9.4627
10.4978
13.8239
10.6418
13.3003
 9.6540
 7.5194
 8.1423
11.2035
10.2972
11.8493
10.3966
12.6548
 8.4565
 9.6804
 9.4063
13.0319
 9.0425
10.7393
11.3321
12.2863
 7.9780
10.2674
 8.7862
13.4817
12.8231
13.4175
12.3053
 9.8072
10.3621
10.3661
12.6838
 6.7024
 6.9409
13.8427
14.2533
11.9745
12.5388
 9.2246
10.0325
 9.0224
 9.4238
12.0756
11.7112
12.9073
 9.9255
10.8156
11.5524
10.6628
 7.8450
 6.7018
 8.9053
 9.4077
 7.4048
 7.3412
12.2576
11.5150
 7.6289
 9.9524
10.9592
 6.3333
 8.8134
10.6144
 6.0244
 9.3590
 9.9216
10.5849
 7.4131
 9.8555
 9.3880
12.0645"""
geolaenge_list = geolaenge_string.split("\n")

### stationsname
stationsname_string = """Aachen                              
Großenkneten                        
Ahrensburg-Wulfsdorf                
Albstadt-Badkap                     
Aldersbach-Kramersepp               
Alfhausen                           
Alsfeld-Eifa                        
Neuruppin-Alt Ruppin                
Leuchtturm Alte Weser               
Altenau                             
Altenstadt                          
Geringswalde-Altgeringswalde        
Altomünster-Maisbrunn               
Alzey                               
Amberg-Unterammersricht             
Amerang-Pfaffing                    
Andernach                           
Angermünde                          
Anklam                              
Ansbach                             
Arendsee                            
Arkona                              
Arnstein-Müdesheim                  
Artern                              
Attenkam                            
Aue                                 
Augsburg                            
Baden-Baden-Geroldsau               
Müllheim                            
Baiersbronn-Obertal                 
Bamberg                             
Bamberg (Sternwarte)                
Barsinghausen-Hohenbostel           
Barth                               
Baruth                              
Kubschütz, Kr. Bautzen              
Heinersreuth-Vollhof                
Beckum-Unterberg                    
Oberzent-Beerfelden                 
Belm                                
Bendorf                             
Benneckenstein                      
Berchtesgaden (KKst)                
Bergen                              
Bergzabern, Bad                     
Berka, Bad (Flugplatz)              
Berleburg, Bad-Stünzel              
Berlin-Alexanderplatz               
Berlin-Buch                         
Berlin-Dahlem (FU)                  
Berlin-Kaniswall                    
Berlin-Marzahn                      
Berlin-Ostkreuz                     
Berlin Brandenburg                  
Berlin-Tegel                        
Berlin-Tempelhof                    
Bernburg/Saale (Nord)               
Bernkastel-Kues                     
Berus                               
Warthausen-Birkenhard               
Blankenrath                         
Bocholt (Marienschule)              
Bocholt-Liedern (Wasserwerk)        
Bochum                              
Boizenburg                          
Boltenhagen                         
Bonn                                
Bonn-Friesdorf                      
Königswinter-Heiderhof              
Borken in Westfalen                 
Braunlage                           
Braunschweig                        
Breitsol                            
Bremen                              
Bremerhaven                         
Bremervörde                         
Brocken                             
Buchen, Kr. Neckar-Odenwald         
Buchenbach                          
Rosengarten-Klecken                 
Büchel-Alflen                       
Bückeburg                           
Burgwald-Bottendorf                 
Carlsfeld                           
Celle                               
Chemnitz                            
Chieming                            
Algermissen-Groß Lobke              
Clausthal-Zellerfeld                
Lautertal-Oberlauter                
Collmberg                           
Cottbus (Flugplatz)                 
Cottbus                             
Cuxhaven                            
Dachwig                             
Darmstadt                           
Darmstadt-Botanischer Garten        
Darmstadt (US-Air-Base)             
Deuselbach                          
UFS Deutsche Bucht                  
Diepholz                            
Dillenburg                          
Dillingen/Donau                     
Dillingen/Donau-Fristingen          
Dippoldiswalde-Reinberg             
Dobel                               
Doberlug-Kirchhain                  
Dresden-Klotzsche                   
Dresden-Hosterwitz                  
Dresden-Strehlen                    
Möckern-Drewitz                     
Dürkheim, Bad                       
Dürrheim, Bad                       
Düsseldorf                          
Ebersberg-Halbing                   
Ebrach                              
Eggebek                             
Eichstätt-Landershofen              
Ellwangen-Rindelbach                
Elpersbüttel                        
Elster, Bad-Sohl                    
Elzach-Fisnacht                     
Emden-Nesserland                    
Emden-Wolthusen                     
Emmendingen-Mundingen               
UFS TW Ems                          
Engen/Hegau                         
Ennigerloh-Ostenfelde               
Eppingen-Elsenz                     
München-Flughafen                   
Erfde                               
Erfurt-Weimar                       
Möhrendorf-Kleinseebach             
Erlangen-Frauenaurach               
Eschwege                            
Eslohe                              
Essen-Bredeney                      
Weilerswist-Lommersum               
Falkenberg,Kr.Rottal-Inn            
Faßberg                             
Fehmarnbelt                         
Feldberg/Schwarzwald                
Fichtelberg/Oberfranken-Hüttstadl   
Fichtelberg                         
Birx/Rhön                           
Frankfurt/Main                      
Frankfurt/Main (Stadt)              
Frankfurt/Main-Westend              
Frankfurt/Main (Feldbergstr.)       
Frankfurt/Oder                      
Freiburg                            
Freiburg/Elbe                       
Freudenstadt                        
Freystadt-Michelbach                
Friedrichshafen                     
Friesoythe-Altenoythe               
Fritzlar/Eder                       
Fürstenfeldbruck                    
Fulda-Horas                         
Gardelegen                          
Garmisch-Partenkirchen              
Geilenkirchen-Neutevern             
Geisenheim                          
Geisingberg                         
Geisingen                           
Gelbelsee                           
Geldern-Walbeck                     
Ohlsbach                            
Genthin                             
Gera-Leumnitz                       
Gießen/Wettenberg                   
Gilserberg-Moischeid                
Glücksburg-Meierwik                 
Görlitz                             
Göttingen                           
Goldberg                            
Gräfenberg-Kasberg                  
Grainet-Rehberg                     
Grambek                             
Greifswald                          
Greifswald-Wieck                    
Greifswalder Oie                    
Münster/Osnabrück                   
Groß Berßen                         
Groß Lüsewitz                       
Großer Arber                        
Grosser Falkenstein                 
Grosser Inselsberg                  
Gründau-Breitenborn                 
Grünow                              
Günzburg                            
Gütersloh (Flugplatz)               
Gunzenhausen/Altmühlsee             
Halle-Kröllwitz                     
Halle (Stadt)                       
Olsdorf                             
Hamburg-Fuhlsbüttel                 
Hamburg-Neuwiedenthal               
Hannover                            
Harburg                             
Harzburg, Bad                       
Harzgerode                          
Hechingen                           
Heidelberg                          
Königstuhl                          
Heidenheim/Brenz                    
Heinsberg-Schleiden                 
Helgoland                           
Herrenalb, Bad                      
Herrnhut                            
Niederwörresbach                    
Hersfeld, Bad                       
Herzberg                            
Hiddensee-Vitte                     
Hilgenroth                          
Höchenschwand                       
Bertsdorf-Hörnitz                   
Hof                                 
Hohenpeißenberg                     
Hohn                                
Hohwacht                            
Holzdorf-Bernsdorf                  
Holzkirchen                         
Bevern, Kr. Holzminden              
Hopsten (Flugplatz)                 
Hümmerich                           
Husum                               
Idar-Oberstein                      
Ingolstadt-Manching                 
Isny                                
Itzehoe                             
Schleswig-Jagel                     
Jena (Sternwarte)                   
Jever                               
Jungholz (Kühmoos)                  
Kahl/Main                           
Kahler Asten                        
Kaisersbach-Cronhütte               
Kaiserslautern                      
Kaisheim-Neuhof                     
Kalkar                              
Kall-Sistig                         
Kaltennordheim                      
Karlshuld                           
Karlsruhe                           
Kassel                              
Kaufbeuren                          
Kempten                             
Kiel-Holtenau                       
Kiel-Kronshagen                     
Kirchberg/Jagst-Herboldshausen      
Kirchdorf/Poel                      
Kissingen, Bad                      
Kitzingen                           
Kleiner Feldberg/Taunus             
Kleiner Inselsberg                  
Schipkau-Klettwitz                  
Kleve                               
Klippeneck                          
Klitzschen bei Torgau               
Koblenz                             
Köln/Bonn                           
Königshofen, Bad                    
Königsmoos-Untermaxfeld             
Königstein/Taunus                   
Kösching                            
Köthen (Anhalt)                     
Kohlgrub, Bad (Rosshof)             
Konstanz                            
Kreuth                              
Kronach                             
Krumbach-Edenhausen                 
Kümmersbruck                        
Kyritz                              
Laage-Kronskamp                     
Lahr                                
Merklingen                          
Landsberg (Flugplatz)               
Langenlipsdorf                      
Lauchstädt, Bad                     
Laupheim                            
Lechfeld                            
Leck                                
Leiblfing                           
Leinefelde                          
Leipzig-Holzhausen                  
Leipzig/Halle                       
Lennestadt-Theten                   
Lenzen/Elbe                         
Lenzkirch-Ruhbühl                   
Leuchtturm Kiel                     
Köln-Stammheim                      
Lichtenhain-Mittelndorf             
Lindenberg                          
Lingen                              
Lippspringe, Bad                    
Lippstadt-Bökenförde                
List auf Sylt                       
Lobenstein, Bad                     
Löhnberg-Obershausen                
Löningen                            
Lübben-Blumenfelde                  
Lübeck                              
Lübeck-Blankensee                   
Lüchow                              
Lüdenscheid                         
Magdeburg                           
Mainz-Lerchenberg (ZDF)             
Maisach-Gernlinden                  
Malente, Bad-Gremsmühlen            
Mallersdorf-Pfaffenberg-Oberlindhart
Manderscheid-Sonnenhof              
Manschnow                           
Cölbe, Kr. Marburg-Biedenkopf       
Marienberg                          
Marienberg, Bad                     
Marienleuchte                       
Markt Erlbach-Hagenhofen            
Marnitz                             
Martinroda                          
Aschersleben-Mehringen              
Meiningen                           
Klipphausen-Garsebach               
Memmingen                           
Memmingen (Flugplatz)               
Mendig                              
Meppen                              
Mergentheim, Bad                    
Meßstetten-Appental                 
Metten                              
Mettlach-Orscholz (Kurort)          
Metzingen                           
Michelstadt                         
Michelstadt-Vielbrunn               
Schmieritz-Weltwitz                 
Mittenwald-Buckelwiesen             
Röllbach                            
Mönchengladbach-Hilderath           
Montabaur                           
Moringen-Lutterbeck                 
Mühlacker                           
Mühldorf                            
Müncheberg                          
München-Stadt                       
München-Bogenhausen                 
München-Nymphenburg                 
München-Riem                        
Münsingen-Apfelstetten              
Münster                             
Muskau, Bad                         
Nauheim, Bad                        
Neubrandenburg                      
Neuburg an der Donau                
Neuburg/Kammel-Langenhaslach        
Neuenahr, Bad-Ahrweiler             
Stechlin-Menz                       
Neuhaus am Rennweg                  
Neukirchen-Hauptschwenda            
Neunkirchen-Seelscheid-Krawinkel    
Neunkirchen-Wellesweiler            
Neuruppin                           
Neustadt am Kulm-Filchendorf        
Neustadt/Weinstraße                 
Neustrelitz                         
Nideggen-Schmidt                    
Niederstetten                       
Niederstotzingen                    
Nienburg                            
Reimlingen                          
Nörvenich-Niederbolheim             
Norderney                           
Nordholz-Wanhöden                   
Nürburg                             
Nürburg-Barweiler                   
Nürnberg-Netzstall                  
Nürnberg                            
Nürtingen                           
Kiefersfelden-Gach                  
Münstertal-Obermünstertal           
Oberstdorf                          
Obersulm-Willsbach                  
Oberviechtach                       
Öhringen                            
Oldenburg                           
Oschatz                             
Osnabrück                           
Osterfeld                           
Ostheim v.d. Rhön                   
Oy-Mittelberg-Petersthal            
Parsberg/Oberpfalz-Eglwang          
Passau-Oberhaus                     
Pelzerhaken                         
Perl-Nennig                         
Pforzheim-Ispringen                 
Pfullendorf                         
Pirmasens                           
Plauen                              
Pommelsbrunn-Mittelburg             
Potsdam                             
Puch                                
Putbus                              
Quedlinburg                         
Querfurt-Mühle Lodersleben          
Quickborn                           
Rahden-Kleinendorf                  
Weingarten, Kr. Ravensburg          
Regensburg                          
Reichshof-Eckenhagen                
Remscheid-Lennep                    
Renningen-Ihinger Hof               
Rheinau-Memprechtshofen             
Rheine-Bentlage                     
Rheinfelden                         
Rheinstetten                        
Altheim, Kreis Biberach             
Rosenheim                           
Rostock-Warnemünde                  
Rotenburg (Wümme)                   
Roth                                
Rothenburg ob der Tauber            
Rottenburg-Kiebingen                
Rottweil                            
Kreuznach, Bad                      
Ruppertsecken                       
Saarbrücken-Ensheim                 
Saarbrücken-Sankt Johann            
Sachsa, Bad                         
Sachsenheim                         
Säckingen, Bad (Bergseestr.)        
Saldenburg-Entschenreuth            
Salzuflen, Bad                      
Salzwedel                           
Sandberg                            
Sankt Peter-Ording                  
Schaafheim-Schlierbach              
Wernigerode-Schierke                
Schleiz                             
Schleswig                           
Schluchsee                          
Schlüchtern-Herolz                  
Schmalkalden, Kurort                
Schmücke                            
Schneifelforsthaus                  
Schömberg, Kr. Calw                 
Schönwald/Ofr.-Brunn                
Schorndorf-Knöbling                 
Schotten                            
Schwaigermoos                       
Schwandorf                          
Schwarzburg                         
Schwerin                            
Schwesing                           
Seehausen                           
Seesen                              
Selbach (Tholey)                    
Siegen (Kläranlage)                 
Sigmaringen (Flugplatz)             
Sigmaringen-Laiz                    
Sigmarszell-Zeisertsweiler          
Simbach/Inn                         
Simmern-Wahlbach                    
Sinsheim                            
Soltau                              
Sondershausen                       
Sonneberg-Neufang                   
Sontra                              
Staffelstein, Bad-Stublang          
Steinau, Kr. Cuxhaven               
Mittelnkirchen-Hohenfelde           
Oberharz am Brocken-Stiege          
Stötten                             
Wagersrott                          
Straubing                           
Stuttgart (Neckartal)               
Stuttgart-Stadt                     
Stuttgart (Schnarrenberg)           
Stuttgart-Echterdingen              
Stuttgart-Hohenheim                 
Tann/Rhön                           
Starkenberg-Tegkwitz                
Teterow                             
Worpswede-Hüttenbusch               
Teuschnitz                          
Tholey                              
Tirschenreuth-Lodermühl             
Titisee-Neustadt-Titisee            
Tönisvorst                          
Torgau                              
Tribsees                            
Trier-Zewen                         
Trier-Petrisberg                    
Trollenhagen                        
Trostberg                           
Twistetal-Mühlhausen                
Ueckermünde                         
Uelzen                              
Gollhofen                           
Ulm                                 
Ummendorf                           
Villingen-Schwenningen              
Waghäusel-Kirrlach                  
Wahlen                              
Wesertal-Lippoldsberg               
Wittenborn                          
Wahnsdorf bei Dresden               
Waldems-Reinborn                    
Waltershausen                       
Warburg                             
Waren (Müritz)                      
Wasserkuppe                         
Weiden                              
Weihenstephan-Dürnast               
Weimar                              
Weimar-Schöndorf                    
Weinbiet                            
Weisen bei Wittenberge              
Weiskirchen/Saar                    
Weißenburg-Emetzheim                
Wendelstein                         
Werl                                
Wernigerode                         
Fehmarn                             
Wielenbach (Demollstr.)             
Wiesbaden-Auringen                  
Wiesenburg                          
Neubulach-Oberhaugstett             
Wittenberg                          
Wittmundhafen                       
Wittstock-Rote Mühle                
Woldegk                             
Wolfach                             
Wolfegg                             
Wolfsburg (Südwest)                 
Dachsberg-Wolpadingen               
Worms                               
Würzburg                            
Wunstorf                            
Wuppertal-Buchenhofen               
Remscheid                           
Wutöschingen-Ofteringen             
Wrixum/Föhr                         
Zehdenick                           
Zeitz                               
Zinnwald-Georgenfeld                
Zugspitze                           
Lichtentanne                        
Zwiesel                             
Zwieselberg                         
Bassum                              
Berge                               
Dannenberg                          
Emden                               
Fürstenzell                         
Hahn                                
Mannheim                            
Schönhagen (Ostseebad)              
Reit im Winkl                       
Wendisch Evern                      
Ostenfeld (Rendsburg)               
Grambow-Schwennenz                  
Sohland/Spree                       
Wangerland-Hooksiel                 
Weidenbach-Weiherschneidbach        
Dörpen                              
Dörnick                             
Coschen                             
Mallersdorf-Pfaffenberg             
Wilhelmshaven (Flugplatz)           
Nastätten                           
Münster am Stein, Bad               
Lügde-Paenbruch                     
Steinhagen-Negast                   
Saarbrücken-Burbach                 
Mülheim-Kärlich                     
Philippsburg KKW                    
Obrigheim                           
Neckarwestheim KKW                  
Waldshut KKW                        
Dogern (Leibstadt)                  
Hamburg-Lotsenhöft                  
Perl/Saar                           
Bremgarten (Fessenheim)             
Friedrichshafen-Unterraderach       
Großerlach-Mannenweiler             
Ingelfingen-Stachenhausen           
Schwäbisch Gmünd-Weiler             
Singen                              
Brilon-Thülen                       
Wusterwitz                          
Huy-Pabstorf                        
Salzungen, Bad-Gräfen-Nitzendorf    
Demker                              
Notzingen                           
Mühlhausen/Thüringen-Görmar         
Karlshagen                          
Markt Erlbach-Mosbach               
Nossen                              
Lohr/Main-Halsbach                  
Lüdinghausen-Brochtrup              
Runkel-Ennerich                     
Maisach-Galgen                      
Schonungen-Mainberg                 
Elsendorf-Horneck                   
Liebenburg-Othfresen                
Siegsdorf-Höll                      
Bielefeld-Deppendorf                
Aulendorf-Haslach                   
Freudenberg/Main-Boxtal             
Neuglobsow (HM)                     
Hattstedt                           
Donauwörth-Osterweiler              
Olbersleben                         
Treuen                              
Arnsberg-Neheim                     
Hermaringen-Allewind                
Offenbach-Wetterpark                
Deutschneudorf-Brüderwiese          
Prackenbach-Neuhäusl                
Feldberg/Mecklenburg                
Jeßnitz                             
Alfeld                              
Eisenach                            
Feuchtwangen-Heilbronn              
Waldmünchen                         
Borkum-Flugplatz                    
Ahaus                               
Heckelberg                          
Hoyerswerda                         
Wunsiedel-Schönbrunn                
Gottfrieding                        
Hoherodskopf/Vogelsberg             
Leutkirch-Herlazhofen               
Neu-Ulrichstein                     
Neuhütten/Spessart                  
Langenwetzendorf-Göttendorf         
Naumburg/Saale-Kreipitzsch          
Piding                              
Padenstedt (Pony-Park)              
Veilsdorf                           
Oberhaching-Laufzorn                
Wittingen-Vorhop                    
Freiburg-Mitte                      
Duisburg-Baerl                      
Waibstadt                           
Hameln-Hastenbeck                   
Waltrop-Abdinghof                   
Gevelsberg-Oberbröking              
Landshut-Reithof                    
Krölpa-Rockendorf                   
Meinerzhagen-Redlendorf             
Hildesheim-Drispenstedt             
Helmstedt-Emmerstedt                
Nordseeboje 2                       
Balingen-Bronnhaupten               
Kaufbeuren (Flugplatz)              
Aachen-Orsbach                      
Schauenburg-Elgershausen            
Ulm-Mähringen                       
Kaufbeuren-Oberbeuren               
Lingen-Baccum                       
Hasenkrug-Hardebek                  
Wacken                              
Gülzow-Prüzen                       """
stationsname_list = stationsname_string.split("\n")

### bundesland
bundesland_string = """Nordrhein-Westfalen   
Niedersachsen         
Schleswig-Holstein    
Baden-Württemberg     
Bayern                
Niedersachsen         
Hessen                
Brandenburg           
Niedersachsen         
Niedersachsen         
Bayern                
Sachsen               
Bayern                
Rheinland-Pfalz       
Bayern                
Bayern                
Rheinland-Pfalz       
Brandenburg           
Mecklenburg-Vorpommern
Bayern                
Sachsen-Anhalt        
Mecklenburg-Vorpommern
Bayern                
Thüringen             
Bayern                
Sachsen               
Bayern                
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Bayern                
Bayern                
Niedersachsen         
Mecklenburg-Vorpommern
Brandenburg           
Sachsen               
Bayern                
Nordrhein-Westfalen   
Hessen                
Niedersachsen         
Rheinland-Pfalz       
Sachsen-Anhalt        
Bayern                
Niedersachsen         
Rheinland-Pfalz       
Thüringen             
Nordrhein-Westfalen   
Berlin                
Berlin                
Berlin                
Berlin                
Berlin                
Berlin                
Brandenburg           
Berlin                
Berlin                
Sachsen-Anhalt        
Rheinland-Pfalz       
Saarland              
Baden-Württemberg     
Rheinland-Pfalz       
Nordrhein-Westfalen   
Nordrhein-Westfalen   
Nordrhein-Westfalen   
Mecklenburg-Vorpommern
Mecklenburg-Vorpommern
Nordrhein-Westfalen   
Nordrhein-Westfalen   
Nordrhein-Westfalen   
Nordrhein-Westfalen   
Niedersachsen         
Niedersachsen         
Bayern                
Bremen                
Bremen                
Niedersachsen         
Sachsen-Anhalt        
Baden-Württemberg     
Baden-Württemberg     
Niedersachsen         
Rheinland-Pfalz       
Niedersachsen         
Hessen                
Sachsen               
Niedersachsen         
Sachsen               
Bayern                
Niedersachsen         
Niedersachsen         
Bayern                
Sachsen               
Brandenburg           
Brandenburg           
Niedersachsen         
Thüringen             
Hessen                
Hessen                
Hessen                
Rheinland-Pfalz       
Hamburg               
Niedersachsen         
Hessen                
Bayern                
Bayern                
Sachsen               
Baden-Württemberg     
Brandenburg           
Sachsen               
Sachsen               
Sachsen               
Sachsen-Anhalt        
Rheinland-Pfalz       
Baden-Württemberg     
Nordrhein-Westfalen   
Bayern                
Bayern                
Schleswig-Holstein    
Bayern                
Baden-Württemberg     
Schleswig-Holstein    
Sachsen               
Baden-Württemberg     
Niedersachsen         
Niedersachsen         
Baden-Württemberg     
Hamburg               
Baden-Württemberg     
Nordrhein-Westfalen   
Baden-Württemberg     
Bayern                
Schleswig-Holstein    
Thüringen             
Bayern                
Bayern                
Hessen                
Nordrhein-Westfalen   
Nordrhein-Westfalen   
Nordrhein-Westfalen   
Bayern                
Niedersachsen         
Schleswig-Holstein    
Baden-Württemberg     
Bayern                
Sachsen               
Thüringen             
Hessen                
Hessen                
Hessen                
Hessen                
Brandenburg           
Baden-Württemberg     
Niedersachsen         
Baden-Württemberg     
Bayern                
Baden-Württemberg     
Niedersachsen         
Hessen                
Bayern                
Hessen                
Sachsen-Anhalt        
Bayern                
Nordrhein-Westfalen   
Hessen                
Sachsen               
Baden-Württemberg     
Bayern                
Nordrhein-Westfalen   
Baden-Württemberg     
Sachsen-Anhalt        
Thüringen             
Hessen                
Hessen                
Schleswig-Holstein    
Sachsen               
Niedersachsen         
Mecklenburg-Vorpommern
Bayern                
Bayern                
Schleswig-Holstein    
Mecklenburg-Vorpommern
Mecklenburg-Vorpommern
Mecklenburg-Vorpommern
Nordrhein-Westfalen   
Niedersachsen         
Mecklenburg-Vorpommern
Bayern                
Bayern                
Thüringen             
Hessen                
Brandenburg           
Bayern                
Nordrhein-Westfalen   
Bayern                
Sachsen-Anhalt        
Sachsen-Anhalt        
Rheinland-Pfalz       
Hamburg               
Hamburg               
Niedersachsen         
Bayern                
Niedersachsen         
Sachsen-Anhalt        
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Nordrhein-Westfalen   
Schleswig-Holstein    
Baden-Württemberg     
Sachsen               
Rheinland-Pfalz       
Hessen                
Niedersachsen         
Mecklenburg-Vorpommern
Rheinland-Pfalz       
Baden-Württemberg     
Sachsen               
Bayern                
Bayern                
Schleswig-Holstein    
Schleswig-Holstein    
Brandenburg           
Bayern                
Niedersachsen         
Nordrhein-Westfalen   
Rheinland-Pfalz       
Schleswig-Holstein    
Rheinland-Pfalz       
Bayern                
Baden-Württemberg     
Schleswig-Holstein    
Schleswig-Holstein    
Thüringen             
Niedersachsen         
Baden-Württemberg     
Bayern                
Nordrhein-Westfalen   
Baden-Württemberg     
Rheinland-Pfalz       
Bayern                
Nordrhein-Westfalen   
Nordrhein-Westfalen   
Thüringen             
Bayern                
Baden-Württemberg     
Hessen                
Bayern                
Bayern                
Schleswig-Holstein    
Schleswig-Holstein    
Baden-Württemberg     
Mecklenburg-Vorpommern
Bayern                
Bayern                
Hessen                
Thüringen             
Brandenburg           
Nordrhein-Westfalen   
Baden-Württemberg     
Sachsen               
Rheinland-Pfalz       
Nordrhein-Westfalen   
Bayern                
Bayern                
Hessen                
Bayern                
Sachsen-Anhalt        
Bayern                
Baden-Württemberg     
Bayern                
Bayern                
Bayern                
Bayern                
Brandenburg           
Mecklenburg-Vorpommern
Baden-Württemberg     
Baden-Württemberg     
Bayern                
Brandenburg           
Sachsen-Anhalt        
Baden-Württemberg     
Bayern                
Schleswig-Holstein    
Bayern                
Thüringen             
Sachsen               
Sachsen               
Nordrhein-Westfalen   
Brandenburg           
Baden-Württemberg     
Schleswig-Holstein    
Nordrhein-Westfalen   
Sachsen               
Brandenburg           
Niedersachsen         
Nordrhein-Westfalen   
Nordrhein-Westfalen   
Schleswig-Holstein    
Thüringen             
Hessen                
Niedersachsen         
Brandenburg           
Schleswig-Holstein    
Schleswig-Holstein    
Niedersachsen         
Nordrhein-Westfalen   
Sachsen-Anhalt        
Rheinland-Pfalz       
Bayern                
Schleswig-Holstein    
Bayern                
Rheinland-Pfalz       
Brandenburg           
Hessen                
Sachsen               
Rheinland-Pfalz       
Schleswig-Holstein    
Bayern                
Mecklenburg-Vorpommern
Thüringen             
Sachsen-Anhalt        
Thüringen             
Sachsen               
Bayern                
Bayern                
Rheinland-Pfalz       
Niedersachsen         
Baden-Württemberg     
Baden-Württemberg     
Bayern                
Saarland              
Baden-Württemberg     
Hessen                
Hessen                
Thüringen             
Bayern                
Bayern                
Nordrhein-Westfalen   
Rheinland-Pfalz       
Niedersachsen         
Baden-Württemberg     
Bayern                
Brandenburg           
Bayern                
Bayern                
Bayern                
Bayern                
Baden-Württemberg     
Nordrhein-Westfalen   
Sachsen               
Hessen                
Mecklenburg-Vorpommern
Bayern                
Bayern                
Rheinland-Pfalz       
Brandenburg           
Thüringen             
Hessen                
Nordrhein-Westfalen   
Saarland              
Brandenburg           
Bayern                
Rheinland-Pfalz       
Mecklenburg-Vorpommern
Nordrhein-Westfalen   
Baden-Württemberg     
Baden-Württemberg     
Niedersachsen         
Bayern                
Nordrhein-Westfalen   
Niedersachsen         
Niedersachsen         
Rheinland-Pfalz       
Rheinland-Pfalz       
Bayern                
Bayern                
Baden-Württemberg     
Bayern                
Baden-Württemberg     
Bayern                
Baden-Württemberg     
Bayern                
Baden-Württemberg     
Niedersachsen         
Sachsen               
Niedersachsen         
Sachsen-Anhalt        
Bayern                
Bayern                
Bayern                
Bayern                
Schleswig-Holstein    
Saarland              
Baden-Württemberg     
Baden-Württemberg     
Rheinland-Pfalz       
Sachsen               
Bayern                
Brandenburg           
Bayern                
Mecklenburg-Vorpommern
Sachsen-Anhalt        
Sachsen-Anhalt        
Schleswig-Holstein    
Nordrhein-Westfalen   
Baden-Württemberg     
Bayern                
Nordrhein-Westfalen   
Nordrhein-Westfalen   
Baden-Württemberg     
Baden-Württemberg     
Nordrhein-Westfalen   
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Bayern                
Mecklenburg-Vorpommern
Niedersachsen         
Bayern                
Bayern                
Baden-Württemberg     
Baden-Württemberg     
Rheinland-Pfalz       
Rheinland-Pfalz       
Saarland              
Saarland              
Niedersachsen         
Baden-Württemberg     
Baden-Württemberg     
Bayern                
Nordrhein-Westfalen   
Sachsen-Anhalt        
Bayern                
Schleswig-Holstein    
Hessen                
Sachsen-Anhalt        
Thüringen             
Schleswig-Holstein    
Baden-Württemberg     
Hessen                
Thüringen             
Thüringen             
Rheinland-Pfalz       
Baden-Württemberg     
Bayern                
Bayern                
Hessen                
Bayern                
Bayern                
Thüringen             
Mecklenburg-Vorpommern
Schleswig-Holstein    
Sachsen-Anhalt        
Niedersachsen         
Saarland              
Nordrhein-Westfalen   
Baden-Württemberg     
Baden-Württemberg     
Bayern                
Bayern                
Rheinland-Pfalz       
Baden-Württemberg     
Niedersachsen         
Thüringen             
Thüringen             
Hessen                
Bayern                
Niedersachsen         
Niedersachsen         
Sachsen-Anhalt        
Baden-Württemberg     
Schleswig-Holstein    
Bayern                
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Hessen                
Thüringen             
Mecklenburg-Vorpommern
Niedersachsen         
Bayern                
Saarland              
Bayern                
Baden-Württemberg     
Nordrhein-Westfalen   
Sachsen               
Mecklenburg-Vorpommern
Rheinland-Pfalz       
Rheinland-Pfalz       
Mecklenburg-Vorpommern
Bayern                
Hessen                
Mecklenburg-Vorpommern
Niedersachsen         
Bayern                
Baden-Württemberg     
Sachsen-Anhalt        
Baden-Württemberg     
Baden-Württemberg     
Hessen                
Hessen                
Schleswig-Holstein    
Sachsen               
Hessen                
Thüringen             
Nordrhein-Westfalen   
Mecklenburg-Vorpommern
Hessen                
Bayern                
Bayern                
Thüringen             
Thüringen             
Rheinland-Pfalz       
Sachsen-Anhalt        
Saarland              
Bayern                
Bayern                
Nordrhein-Westfalen   
Sachsen-Anhalt        
Schleswig-Holstein    
Bayern                
Hessen                
Brandenburg           
Baden-Württemberg     
Sachsen-Anhalt        
Niedersachsen         
Brandenburg           
Mecklenburg-Vorpommern
Baden-Württemberg     
Baden-Württemberg     
Niedersachsen         
Baden-Württemberg     
Rheinland-Pfalz       
Bayern                
Niedersachsen         
Nordrhein-Westfalen   
Nordrhein-Westfalen   
Baden-Württemberg     
Schleswig-Holstein    
Brandenburg           
Sachsen-Anhalt        
Sachsen               
Bayern                
Sachsen               
Bayern                
Bayern                
Niedersachsen         
Brandenburg           
Niedersachsen         
Niedersachsen         
Bayern                
Rheinland-Pfalz       
Baden-Württemberg     
Schleswig-Holstein    
Bayern                
Niedersachsen         
Schleswig-Holstein    
Mecklenburg-Vorpommern
Sachsen               
Niedersachsen         
Bayern                
Niedersachsen         
Schleswig-Holstein    
Brandenburg           
Bayern                
Niedersachsen         
Rheinland-Pfalz       
Rheinland-Pfalz       
Nordrhein-Westfalen   
Mecklenburg-Vorpommern
Saarland              
Rheinland-Pfalz       
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Hamburg               
Saarland              
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Baden-Württemberg     
Nordrhein-Westfalen   
Brandenburg           
Sachsen-Anhalt        
Thüringen             
Sachsen-Anhalt        
Baden-Württemberg     
Thüringen             
Mecklenburg-Vorpommern
Bayern                
Sachsen               
Bayern                
Nordrhein-Westfalen   
Hessen                
Bayern                
Bayern                
Bayern                
Niedersachsen         
Bayern                
Nordrhein-Westfalen   
Baden-Württemberg     
Baden-Württemberg     
Brandenburg           
Schleswig-Holstein    
Bayern                
Thüringen             
Sachsen               
Nordrhein-Westfalen   
Baden-Württemberg     
Hessen                
Sachsen               
Bayern                
Mecklenburg-Vorpommern
Sachsen-Anhalt        
Niedersachsen         
Thüringen             
Bayern                
Bayern                
Niedersachsen         
Nordrhein-Westfalen   
Brandenburg           
Sachsen               
Bayern                
Bayern                
Hessen                
Baden-Württemberg     
Hessen                
Bayern                
Thüringen             
Sachsen-Anhalt        
Bayern                
Schleswig-Holstein    
Thüringen             
Bayern                
Niedersachsen         
Baden-Württemberg     
Nordrhein-Westfalen   
Baden-Württemberg     
Niedersachsen         
Nordrhein-Westfalen   
Nordrhein-Westfalen   
Bayern                
Thüringen             
Nordrhein-Westfalen   
Niedersachsen         
Niedersachsen         
Hamburg               
Baden-Württemberg     
Bayern                
Nordrhein-Westfalen   
Hessen                
Baden-Württemberg     
Bayern                
Niedersachsen         
Schleswig-Holstein    
Schleswig-Holstein    
Mecklenburg-Vorpommern"""
bundesland_list = bundesland_string.split("\n")

metadata_string_raw = """ 
Stations_id von_datum bis_datum Stationshoehe geoBreite geoLaenge Stationsname Bundesland
----------- --------- --------- ------------- --------- --------- ----------------------------------------- ----------
00003 19500401 20110331            202     50.7827    6.0941 Aachen                                                                           Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
00044 20070401 20240206             44     52.9336    8.2370 Großenkneten                                                                     Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00052 19760101 19880101             46     53.6623   10.1990 Ahrensburg-Wulfsdorf                                                             Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
00071 20091201 20191231            759     48.2156    8.9784 Albstadt-Badkap                                                                  Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
00073 20070401 20240206            374     48.6183   13.0620 Aldersbach-Kramersepp                                                            Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00078 20041101 20240206             64     52.4853    7.9125 Alfhausen                                                                        Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00091 20040901 20240206            300     50.7446    9.3450 Alsfeld-Eifa                                                                     Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00096 20190409 20240206             50     52.9437   12.8518 Neuruppin-Alt Ruppin                                                             Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
00102 20020101 20240206              0     53.8633    8.1275 Leuchtturm Alte Weser                                                            Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00106 19990101 20061201            500     51.7976   10.4429 Altenau                                                                          Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00125 19710104 20240206            742     47.8342   10.8667 Altenstadt                                                                       Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00131 20041101 20240206            296     51.0881   12.9326 Geringswalde-Altgeringswalde                                                     Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
00142 19820101 20240206            511     48.4060   11.3117 Altomünster-Maisbrunn                                                            Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00150 20050701 20240206            215     49.7273    8.1164 Alzey                                                                            Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
00151 20050301 20240206            382     49.4691   11.8546 Amberg-Unterammersricht                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00154 20050301 20240206            516     48.0197   12.2925 Amerang-Pfaffing                                                                 Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00161 20110901 20240206             75     50.4237    7.4202 Andernach                                                                        Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
00164 19560101 20240206             54     53.0316   13.9908 Angermünde                                                                       Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
00167 20040901 20240206             11     53.8409   13.6854 Anklam                                                                           Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00175 19550101 19751231            413     49.2964   10.5751 Ansbach                                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00181 19990928 20081103             30     52.8761   11.5042 Arendsee                                                                         Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
00183 19730101 20240206             42     54.6791   13.4344 Arkona                                                                           Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00191 20041104 20240206            217     49.9694    9.9114 Arnstein-Müdesheim                                                               Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00198 19610101 20240206            164     51.3744   11.2920 Artern                                                                           Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
00217 20050101 20240206            670     47.8774   11.3643 Attenkam                                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00222 19820101 20240206            393     50.5908   12.7139 Aue                                                                              Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
00232 19550101 20240206            462     48.4253   10.9417 Augsburg                                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00257 20021101 20240206            240     48.7270    8.2457 Baden-Baden-Geroldsau                                                            Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
00259 20040701 20240206            275     47.8064    7.6387 Müllheim                                                                         Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
00268 19960718 20081231            622     48.5293    8.2727 Baiersbronn-Obertal                                                              Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
00282 19610101 20240206            240     49.8743   10.9206 Bamberg                                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00284 19470101 19550101            282     49.8800   10.8800 Bamberg (Sternwarte)                                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00294 20040701 20240206            110     52.3199    9.4300 Barsinghausen-Hohenbostel                                                        Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00298 19810101 20240206              3     54.3405   12.7108 Barth                                                                            Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00303 19930819 20240206             55     52.0613   13.4997 Baruth                                                                           Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
00314 20040501 20240206            234     51.1604   14.5042 Kubschütz, Kr. Bautzen                                                           Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
00320 20060701 20240206            350     49.9666   11.5198 Heinersreuth-Vollhof                                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00326 20040701 20130708            120     51.7204    8.0577 Beckum-Unterberg                                                                 Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
00330 20040801 20240206            455     49.5617    8.9673 Oberzent-Beerfelden                                                              Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00342 20101201 20240206            103     52.3170    8.1694 Belm                                                                             Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00348 19891215 20110901            127     50.4135    7.5886 Bendorf                                                                          Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
00350 19990601 19991231            540     51.6715   10.7268 Benneckenstein                                                                   Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
00361 19480101 19760101            550     47.6344   13.0109 Berchtesgaden (KKst)                                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00368 20020101 20240206             69     52.8152    9.9248 Bergen                                                                           Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00377 20041001 20240206            210     49.1070    7.9967 Bergzabern, Bad                                                                  Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
00379 20170901 20240206            304     50.9075   11.2665 Berka, Bad (Flugplatz)                                                           Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
00390 20040701 20240206            610     50.9837    8.3683 Berleburg, Bad-Stünzel                                                           Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
00399 19691201 20110801             36     52.5198   13.4057 Berlin-Alexanderplatz                                                            Berlin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00400 19910101 20240206             60     52.6310   13.5021 Berlin-Buch                                                                      Berlin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00403 20020101 20240206             51     52.4537   13.3017 Berlin-Dahlem (FU)                                                               Berlin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00410 20040501 20200615             33     52.4040   13.7309 Berlin-Kaniswall                                                                 Berlin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00420 20070801 20230806             61     52.5447   13.5598 Berlin-Marzahn                                                                   Berlin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00424 19610101 19810101             36     52.5000   13.4667 Berlin-Ostkreuz                                                                  Berlin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00427 19730101 20240206             46     52.3807   13.5306 Berlin Brandenburg                                                               Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
00430 19860101 20210505             36     52.5644   13.3088 Berlin-Tegel                                                                     Berlin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00433 19510101 20240206             48     52.4676   13.4020 Berlin-Tempelhof                                                                 Berlin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00445 20050701 20240206             85     51.8218   11.7110 Bernburg/Saale (Nord)                                                            Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
00450 20051101 20121204            120     49.9186    7.0664 Bernkastel-Kues                                                                  Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
00460 19610101 20240206            362     49.2641    6.6868 Berus                                                                            Saarland                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
00474 19750601 19780601            599     48.1252    9.7639 Warthausen-Birkenhard                                                            Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
00535 20040601 20240206            417     50.0372    7.3079 Blankenrath                                                                      Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
00553 19510101 19740901             25     51.8380    6.6107 Bocholt (Marienschule)                                                           Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
00554 19740901 20060228             23     51.8293    6.5365 Bocholt-Liedern (Wasserwerk)                                                     Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
00555 20080101 20240206            110     51.5026    7.2289 Bochum                                                                           Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
00591 19730101 20240206             45     53.3911   10.6878 Boizenburg                                                                       Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00596 19730101 20240206             15     54.0027   11.1908 Boltenhagen                                                                      Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00598 19490101 19570101             62     50.7285    7.0839 Bonn                                                                             Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
00599 19840101 19971201             62     50.7055    7.1467 Bonn-Friesdorf                                                                   Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
00603 20010403 20240206            147     50.7293    7.2040 Königswinter-Heiderhof                                                           Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
00617 20040601 20240206             47     51.8730    6.8863 Borken in Westfalen                                                              Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
00656 19480101 20240206            607     51.7234   10.6021 Braunlage                                                                        Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00662 19510101 20240206             81     52.2915   10.4464 Braunschweig                                                                     Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00685 20020101 20061031            585     49.9017    9.4281 Breitsol                                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00691 19490101 20240206              4     53.0451    8.7981 Bremen                                                                           Bremen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00701 19490101 20240206              7     53.5332    8.5761 Bremerhaven                                                                      Bremen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00704 19910101 20240206             11     53.4451    9.1390 Bremervörde                                                                      Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00722 19510101 20240206           1135     51.7986   10.6183 Brocken                                                                          Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
00755 20040601 20240206            340     49.5182    9.3213 Buchen, Kr. Neckar-Odenwald                                                      Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
00757 20040601 20240206            445     47.9625    7.9983 Buchenbach                                                                       Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
00760 20171201 20240206             83     53.3629    9.9435 Rosengarten-Klecken                                                              Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00766 20020101 20240206            477     50.1745    7.0595 Büchel-Alflen                                                                    Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
00769 20020101 20240206             68     52.2817    9.0890 Bückeburg                                                                        Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00817 20050201 20240206            293     51.0306    8.8146 Burgwald-Bottendorf                                                              Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00840 19910101 20240206            895     50.4313   12.6114 Carlsfeld                                                                        Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
00850 20020101 20240206             45     52.5959   10.0296 Celle                                                                            Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00853 19510101 20240206            416     50.7913   12.8720 Chemnitz                                                                         Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
00856 19910101 20240206            551     47.8843   12.5404 Chieming                                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00860 20231001 20240206             80     52.2731   10.0163 Algermissen-Groß Lobke                                                           Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00863 20071001 20120403            585     51.7904   10.3470 Clausthal-Zellerfeld                                                             Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00867 19470101 20240206            344     50.3066   10.9679 Lautertal-Oberlauter                                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00876 19730101 19890101            314     51.3040   13.0096 Collmberg                                                                        Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
00879 20020101 20030611             68     51.7667   14.2833 Cottbus (Flugplatz)                                                              Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
00880 19560101 20240206             69     51.7759   14.3168 Cottbus                                                                          Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
00891 19510101 20240206              5     53.8713    8.7060 Cuxhaven                                                                         Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00896 20040801 20240206            170     51.0778   10.8619 Dachwig                                                                          Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
00917 20040901 20240206            162     49.8809    8.6779 Darmstadt                                                                        Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00919 19580101 19720101            169     49.8697    8.6796 Darmstadt-Botanischer Garten                                                     Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00920 19720101 19870929            108     49.8564    8.5929 Darmstadt (US-Air-Base)                                                          Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00953 19550101 20240206            481     49.7619    7.0542 Deuselbach                                                                       Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
00954 20000501 20221121              0     54.1796    7.4587 UFS Deutsche Bucht                                                               Hamburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
00963 19940103 20240206             38     52.5881    8.3424 Diepholz                                                                         Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
00979 20040901 20230313            314     50.7364    8.2672 Dillenburg                                                                       Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00982 19760101 19780601            420     48.5701   10.4985 Dillingen/Donau                                                                  Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00983 20061201 20240206            419     48.5562   10.5599 Dillingen/Donau-Fristingen                                                       Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
00991 20050201 20240206            359     50.9116   13.7087 Dippoldiswalde-Reinberg                                                          Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
00998 19961001 20090201            696     48.7968    8.4921 Dobel                                                                            Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
01001 19810101 20240206             97     51.6451   13.5747 Doberlug-Kirchhain                                                               Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
01048 19730101 20240206            228     51.1278   13.7543 Dresden-Klotzsche                                                                Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
01050 20060401 20240206            112     51.0221   13.8470 Dresden-Hosterwitz                                                               Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
01051 20070301 20230814            119     51.0249   13.7750 Dresden-Strehlen                                                                 Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
01052 20040701 20240206             80     52.2174   12.1641 Möckern-Drewitz                                                                  Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
01072 20040601 20240206            107     49.4719    8.1929 Dürkheim, Bad                                                                    Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
01076 19960514 20090101            692     48.0135    8.5343 Dürrheim, Bad                                                                    Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
01078 19760301 20240206             37     51.2960    6.7686 Düsseldorf                                                                       Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
01103 20061001 20240206            592     48.1003   11.9872 Ebersberg-Halbing                                                                Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01107 20041201 20240206            346     49.8520   10.4991 Ebrach                                                                           Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01130 20020101 20050422             18     54.6282    9.3649 Eggebek                                                                          Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
01161 20050201 20240206            384     48.8777   11.2349 Eichstätt-Landershofen                                                           Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01197 19480101 20240206            463     48.9895   10.1312 Ellwangen-Rindelbach                                                             Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
01200 20020101 20240206              3     54.0691    9.0105 Elpersbüttel                                                                     Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
01207 20060301 20240206            558     50.2705   12.2742 Elster, Bad-Sohl                                                                 Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
01214 20040801 20240206            431     48.2012    8.1088 Elzach-Fisnacht                                                                  Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
01219 19710101 19981102              5     53.3449    7.1909 Emden-Nesserland                                                                 Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
01221 19490101 19710101              0     53.3707    7.2236 Emden-Wolthusen                                                                  Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
01224 20021201 20240206            201     48.1378    7.8351 Emmendingen-Mundingen                                                            Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
01228 20020101 20240206              0     54.1651    6.3460 UFS TW Ems                                                                       Hamburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
01239 20040701 20080923            540     47.8516    8.7673 Engen/Hegau                                                                      Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
01246 20150801 20240206            104     51.8418    8.0607 Ennigerloh-Ostenfelde                                                            Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
01255 20021201 20240206            226     49.1661    8.8483 Eppingen-Elsenz                                                                  Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
01262 19920517 20240206            446     48.3477   11.8134 München-Flughafen                                                                Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01266 20040601 20240206             18     54.2992    9.3162 Erfde                                                                            Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
01270 19510101 20240206            316     50.9829   10.9608 Erfurt-Weimar                                                                    Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
01279 19861101 20240206            268     49.6497   11.0075 Möhrendorf-Kleinseebach                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01281 19941101 20010501            284     49.5653   10.9729 Erlangen-Frauenaurach                                                            Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01297 20041001 20240206            156     51.2041   10.0138 Eschwege                                                                         Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01300 20040601 20240206            351     51.2540    8.1565 Eslohe                                                                           Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
01303 19510101 20240206            150     51.4041    6.9677 Essen-Bredeney                                                                   Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
01327 20040801 20240206            147     50.7119    6.7905 Weilerswist-Lommersum                                                            Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
01332 20050301 20240206            471     48.4832   12.7241 Falkenberg,Kr.Rottal-Inn                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01339 20020101 20240206             76     52.9157   10.1885 Faßberg                                                                          Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
01341 20081201 20110929              0     54.6000   11.1500 Fehmarnbelt                                                                      Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
01346 19520101 20240206           1486     47.8748    8.0038 Feldberg/Schwarzwald                                                             Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
01357 20050301 20240206            655     49.9807   11.8376 Fichtelberg/Oberfranken-Hüttstadl                                                Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01358 19510101 20240206           1213     50.4283   12.9536 Fichtelberg                                                                      Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
01411 20070101 20240206            747     50.5309   10.0479 Birx/Rhön                                                                        Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
01420 19810101 20240206            100     50.0259    8.5213 Frankfurt/Main                                                                   Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01421 19620101 19840901            125     50.1474    8.6746 Frankfurt/Main (Stadt)                                                           Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01424 20080801 20240206            121     50.1269    8.6694 Frankfurt/Main-Westend                                                           Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01425 19480101 19620101            103     50.1214    8.6604 Frankfurt/Main (Feldbergstr.)                                                    Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01426 19610101 19850101             65     52.3397   14.5080 Frankfurt/Oder                                                                   Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
01443 19510101 20240206            237     48.0232    7.8343 Freiburg                                                                         Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
01451 20040601 20240206              2     53.8277    9.2493 Freiburg/Elbe                                                                    Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
01468 19510101 20240206            797     48.4538    8.4090 Freudenstadt                                                                     Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
01473 20060101 20190228            414     49.1869   11.3080 Freystadt-Michelbach                                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01490 19650101 19770801            394     47.6454    9.4795 Friedrichshafen                                                                  Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
01503 20121001 20240206              6     53.0643    7.9020 Friesoythe-Altenoythe                                                            Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
01504 20020101 20240206            172     51.1190    9.2799 Fritzlar/Eder                                                                    Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01515 20021104 20030814            519     48.2000   11.2667 Fürstenfeldbruck                                                                 Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01526 20041101 20240206            242     50.5668    9.6532 Fulda-Horas                                                                      Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01544 19510101 20240206             47     52.5129   11.3942 Gardelegen                                                                       Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
01550 19480101 20240206            719     47.4830   11.0621 Garmisch-Partenkirchen                                                           Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01572 20020101 20240206             80     50.9593    6.0392 Geilenkirchen-Neutevern                                                          Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
01580 19460101 20240206            111     49.9859    7.9548 Geisenheim                                                                       Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01583 19510101 19710101            823     50.7719   13.7732 Geisingberg                                                                      Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
01584 20090601 20240206            673     47.9242    8.6474 Geisingen                                                                        Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
01587 19910101 20240206            536     48.9481   11.4289 Gelbelsee                                                                        Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01590 20030701 20240206             37     51.4942    6.2463 Geldern-Walbeck                                                                  Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
01602 20040701 20240206            177     48.4330    7.9930 Ohlsbach                                                                         Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
01605 19820101 20240206             35     52.3875   12.1602 Genthin                                                                          Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
01612 19730101 20240206            311     50.8812   12.1289 Gera-Leumnitz                                                                    Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
01639 19500101 20240206            203     50.6017    8.6439 Gießen/Wettenberg                                                                Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01645 20040501 20240206            340     50.9656    9.0500 Gilserberg-Moischeid                                                             Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01666 20020101 20240206             12     54.8273    9.5058 Glücksburg-Meierwik                                                              Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
01684 19510101 20240206            239     51.1621   14.9506 Görlitz                                                                          Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
01691 19480101 20240206            167     51.5002    9.9507 Göttingen                                                                        Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
01694 19810101 20240206             59     53.6058   12.1034 Goldberg                                                                         Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01721 20061001 20240206            506     49.6640   11.2239 Gräfenberg-Kasberg                                                               Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01735 20050301 20240206            628     48.7894   13.6290 Grainet-Rehberg                                                                  Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01736 20020124 20240206             26     53.5731   10.6797 Grambek                                                                          Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
01757 19780101 20240206              2     54.0967   13.4056 Greifswald                                                                       Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01758 19510101 19780101              2     54.1000   13.4500 Greifswald-Wieck                                                                 Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01759 20001025 20240206             12     54.2437   13.9102 Greifswalder Oie                                                                 Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01766 19891001 20240206             48     52.1344    7.6969 Münster/Osnabrück                                                                Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
01792 20200814 20240206             27     52.7553    7.4815 Groß Berßen                                                                      Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
01803 19910101 20240206             35     54.0714   12.3238 Groß Lüsewitz                                                                    Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01832 19821101 20240206           1436     49.1129   13.1338 Großer Arber                                                                     Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01833 19480101 19821101           1307     49.0851   13.2801 Grosser Falkenstein                                                              Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01834 19510101 19780701            913     50.8519   10.4665 Grosser Inselsberg                                                               Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
01863 20071201 20240206            258     50.2667    9.1854 Gründau-Breitenborn                                                              Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01869 19810101 20240206             56     53.3154   13.9339 Grünow                                                                           Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
01886 20160901 20240206            444     48.4878   10.2608 Günzburg                                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01892 20020101 20131028             72     51.9298    8.3005 Gütersloh (Flugplatz)                                                            Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
01902 19841101 19871001            413     49.1273   10.7448 Gunzenhausen/Altmühlsee                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
01957 19530101 20150323             93     51.5138   11.9499 Halle-Kröllwitz                                                                  Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
01960 19600101 19710101            102     51.4831   11.9671 Halle (Stadt)                                                                    Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
01964 20050501 20240206            328     49.9445    6.3821 Olsdorf                                                                          Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
01975 19490101 20240206             11     53.6332    9.9881 Hamburg-Fuhlsbüttel                                                              Hamburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
01981 20050301 20240206              4     53.4776    9.8957 Hamburg-Neuwiedenthal                                                            Hamburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
02014 19490101 20240206             55     52.4644    9.6779 Hannover                                                                         Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
02023 20020101 20240206            501     48.7918   10.7062 Harburg                                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02039 20061101 20240206            203     51.9002   10.5699 Harzburg, Bad                                                                    Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
02044 19810101 20240206            404     51.6520   11.1366 Harzgerode                                                                       Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
02074 20040601 20240206            518     48.3752    8.9800 Hechingen                                                                        Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02080 20040701 20120912            110     49.4206    8.6676 Heidelberg                                                                       Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02081 19480101 19550101            561     49.3981    8.7251 Königstuhl                                                                       Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02088 20040601 20050512            522     48.6849   10.1420 Heidenheim/Brenz                                                                 Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02110 20030101 20240206             57     51.0411    6.1042 Heinsberg-Schleiden                                                              Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
02115 19520501 20240206              4     54.1750    7.8920 Helgoland                                                                        Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
02158 19961001 20090101            350     48.8042    8.4430 Herrenalb, Bad                                                                   Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02166 19820101 19910502            344     51.0167   14.7500 Herrnhut                                                                         Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
02167 20050301 20120402            302     49.7672    7.3356 Niederwörresbach                                                                 Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
02171 19510101 20240206            272     50.8520    9.7377 Hersfeld, Bad                                                                    Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02174 20101101 20240206            236     51.6255   10.3695 Herzberg                                                                         Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
02201 20050801 20240206              1     54.5750   13.1044 Hiddensee-Vitte                                                                  Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02211 20041001 20240206            295     50.7370    7.6525 Hilgenroth                                                                       Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
02244 19710101 20050901           1008     47.7327    8.1627 Höchenschwand                                                                    Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02252 20050701 20240206            271     50.8992   14.7456 Bertsdorf-Hörnitz                                                                Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
02261 19480101 20240206            565     50.3123   11.8760 Hof                                                                              Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02290 19470101 20240206            977     47.8009   11.0108 Hohenpeißenberg                                                                  Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02303 20020101 20240206             10     54.3162    9.5385 Hohn                                                                             Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
02306 20050801 20240206              8     54.3194   10.6732 Hohwacht                                                                         Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
02315 20021101 20240206             80     51.7657   13.1666 Holzdorf-Bernsdorf                                                               Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
02319 20050601 20240206            685     47.8823   11.6961 Holzkirchen                                                                      Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02323 20060701 20240206            110     51.8529    9.4953 Bevern, Kr. Holzminden                                                           Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
02338 20020101 20051223             39     52.3333    7.5500 Hopsten (Flugplatz)                                                              Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
02362 20040801 20240206            328     50.5651    7.4843 Hümmerich                                                                        Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
02374 19490101 19740701              3     54.4752    9.0564 Husum                                                                            Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
02385 20020101 20240206            376     49.6927    7.3263 Idar-Oberstein                                                                   Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
02410 19610102 20240206            364     48.7111   11.5363 Ingolstadt-Manching                                                              Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02423 20040301 20050702            712     47.6894   10.0416 Isny                                                                             Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02429 20020101 20240206             20     53.9897    9.5697 Itzehoe                                                                          Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
02437 20020101 20240206             21     54.4570    9.5203 Schleswig-Jagel                                                                  Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
02444 19910801 20240206            155     50.9251   11.5830 Jena (Sternwarte)                                                                Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
02456 20011017 20050826              7     53.5322    7.8806 Jever                                                                            Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
02477 19710101 19760101            728     47.5938    7.9597 Jungholz (Kühmoos)                                                               Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02480 20040901 20240206            108     50.0643    8.9930 Kahl/Main                                                                        Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02483 19510101 20240203            839     51.1803    8.4891 Kahler Asten                                                                     Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
02485 20110502 20240206            489     48.9170    9.6871 Kaisersbach-Cronhütte                                                            Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02486 20050301 20240206            271     49.4262    7.7557 Kaiserslautern                                                                   Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
02488 19820101 20021001            516     48.7701   10.7876 Kaisheim-Neuhof                                                                  Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02494 20020101 20131020             31     51.7329    6.2688 Kalkar                                                                           Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
02497 20040801 20240206            505     50.5014    6.5264 Kall-Sistig                                                                      Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
02503 19510101 20030505            487     50.6266   10.1455 Kaltennordheim                                                                   Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
02521 19820101 19940401            374     48.6765   11.2961 Karlshuld                                                                        Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02522 19480101 20081031            112     49.0382    8.3641 Karlsruhe                                                                        Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02532 19480101 20131031            231     51.2963    9.4424 Kassel                                                                           Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02542 19750601 20160402            716     47.8652   10.6007 Kaufbeuren                                                                       Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02559 19550101 20240206            705     47.7233   10.3348 Kempten                                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02564 20020101 20240206             28     54.3776   10.1424 Kiel-Holtenau                                                                    Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
02565 19490101 19881015             17     54.3378   10.0929 Kiel-Kronshagen                                                                  Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
02575 20070523 20240206            432     49.1804    9.9800 Kirchberg/Jagst-Herboldshausen                                                   Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02578 20040701 20240206             14     53.9995   11.4341 Kirchdorf/Poel                                                                   Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02597 19480101 20240206            282     50.2240   10.0792 Kissingen, Bad                                                                   Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02600 20050301 20240206            193     49.7363   10.1781 Kitzingen                                                                        Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02601 19480101 20240206            822     50.2218    8.4469 Kleiner Feldberg/Taunus                                                          Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02618 20041001 20240206            732     50.8458   10.4803 Kleiner Inselsberg                                                               Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
02627 20040701 20240206            128     51.5554   13.8845 Schipkau-Klettwitz                                                               Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
02629 20040701 20240206             46     51.7612    6.0954 Kleve                                                                            Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
02638 19650701 20240206            974     48.1054    8.7548 Klippeneck                                                                       Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02641 20040901 20240206             90     51.5185   12.9065 Klitzschen bei Torgau                                                            Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
02656 19550101 19900101             96     50.3519    7.5906 Koblenz                                                                          Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
02667 19600101 20240206             91     50.8645    7.1575 Köln/Bonn                                                                        Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
02680 20050601 20240206            289     50.2840   10.4456 Königshofen, Bad                                                                 Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02691 19940401 19941101            378     48.6707   11.2173 Königsmoos-Untermaxfeld                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02693 19510101 19660101            380     50.1855    8.4698 Königstein/Taunus                                                                Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02700 20041201 20240206            416     48.8302   11.4872 Kösching                                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02704 20040501 20240206             76     51.7511   12.0094 Köthen (Anhalt)                                                                  Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
02708 20060701 20240206            742     47.6652   11.0805 Kohlgrub, Bad (Rosshof)                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02712 19710101 20240206            428     47.6952    9.1307 Konstanz                                                                         Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02738 19980101 19980201            776     47.6448   11.7438 Kreuth                                                                           Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02750 20051101 20240206            310     50.2524   11.3209 Kronach                                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02761 19750601 19780601            520     48.2510   10.4163 Krumbach-Edenhausen                                                              Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02773 20020101 20240206            415     49.4283   11.9016 Kümmersbruck                                                                     Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02794 19890101 20240206             40     52.9362   12.4093 Kyritz                                                                           Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
02796 20020101 20240206             41     53.9156   12.2790 Laage-Kronskamp                                                                  Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02812 19950101 20240206            156     48.3647    7.8280 Lahr                                                                             Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02814 19750601 20240206            687     48.5122    9.7644 Merklingen                                                                       Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02829 19660101 20180710            617     48.0772   10.9144 Landsberg (Flugplatz)                                                            Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02856 20040701 20240206             91     51.9173   13.0878 Langenlipsdorf                                                                   Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
02878 20170801 20240206            117     51.3909   11.8786 Lauchstädt, Bad                                                                  Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
02886 20020101 20240206            539     48.2175    9.9097 Laupheim                                                                         Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02905 20020101 20240206            550     48.1849   10.8507 Lechfeld                                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02907 19910101 20240206              7     54.7903    8.9514 Leck                                                                             Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
02920 19820101 19841101            365     48.7654   12.5121 Leiblfing                                                                        Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
02925 19560101 20240206            356     51.3932   10.3123 Leinefelde                                                                       Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
02928 19510101 20240206            138     51.3151   12.4462 Leipzig-Holzhausen                                                               Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
02932 19720501 20240206            131     51.4347   12.2396 Leipzig/Halle                                                                    Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
02947 20061001 20240206            286     51.1333    8.0348 Lennestadt-Theten                                                                Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
02951 20040601 20240206             20     53.1007   11.4864 Lenzen/Elbe                                                                      Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
02953 20070401 20240206            854     47.8597    8.2308 Lenzkirch-Ruhbühl                                                                Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
02961 20020101 20240206              0     54.4996   10.2737 Leuchtturm Kiel                                                                  Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
02968 20081201 20240206             43     50.9894    6.9777 Köln-Stammheim                                                                   Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
02985 19910305 20240206            321     50.9383   14.2094 Lichtenhain-Mittelndorf                                                          Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
03015 19510101 20240206             98     52.2085   14.1180 Lindenberg                                                                       Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
03023 19510101 20161231             22     52.5181    7.3081 Lingen                                                                           Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
03028 19710401 20240206            157     51.7854    8.8388 Lippspringe, Bad                                                                 Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
03031 20040701 20240206             92     51.6336    8.3945 Lippstadt-Bökenförde                                                             Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
03032 19490101 20240206             25     55.0110    8.4125 List auf Sylt                                                                    Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
03034 20070101 20240206            496     50.4505   11.6350 Lobenstein, Bad                                                                  Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
03042 20080601 20240206            230     50.5617    8.2386 Löhnberg-Obershausen                                                             Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03044 20070701 20180601             22     52.7198    7.7472 Löningen                                                                         Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
03083 20050101 20240206             57     51.9267   13.8797 Lübben-Blumenfelde                                                               Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
03085 19510101 19850301             15     53.8773   10.6915 Lübeck                                                                           Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
03086 19850301 20240206             15     53.8025   10.6989 Lübeck-Blankensee                                                                Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
03093 19541201 20240206             16     52.9724   11.1374 Lüchow                                                                           Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
03098 19940101 20240206            387     51.2452    7.6425 Lüdenscheid                                                                      Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
03126 19550101 20240206             79     52.1029   11.5827 Magdeburg                                                                        Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
03137 20080501 20230801            195     49.9656    8.2139 Mainz-Lerchenberg (ZDF)                                                          Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
03139 19831101 20050101            509     48.2166   11.2965 Maisach-Gernlinden                                                               Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03145 19981201 20080901             30     54.1800   10.5528 Malente, Bad-Gremsmühlen                                                         Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
03147 19850101 20240206            390     48.7548   12.2118 Mallersdorf-Pfaffenberg-Oberlindhart                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03155 20040801 20240206            413     50.1015    6.8009 Manderscheid-Sonnenhof                                                           Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
03158 19890101 20240206             12     52.5468   14.5453 Manschnow                                                                        Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
03164 20060701 20240206            187     50.8492    8.7745 Cölbe, Kr. Marburg-Biedenkopf                                                    Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03166 19820101 20240206            639     50.6511   13.1469 Marienberg                                                                       Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
03167 19621201 20240206            547     50.6621    7.9603 Marienberg, Bad                                                                  Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
03170 20020101 20121221              9     54.4937   11.2411 Marienleuchte                                                                    Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
03181 20210801 20240206            360     49.4875   10.6277 Markt Erlbach-Hagenhofen                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03196 19810101 20240206             81     53.3222   11.9321 Marnitz                                                                          Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03204 20080701 20240206            429     50.7335   10.8815 Martinroda                                                                       Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
03226 20060801 20240206            107     51.7259   11.5109 Aschersleben-Mehringen                                                           Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
03231 19790101 20240206            450     50.5611   10.3771 Meiningen                                                                        Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
03234 20050201 20240206            158     51.1294   13.4328 Klipphausen-Garsebach                                                            Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
03244 19750601 20240206            614     47.9821   10.1384 Memmingen                                                                        Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03245 20020102 20021120            630     47.9833   10.2333 Memmingen (Flugplatz)                                                            Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03246 20020101 20070613            181     50.3667    7.3167 Mendig                                                                           Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
03254 20020102 20240206             19     52.7155    7.3176 Meppen                                                                           Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
03257 20040601 20221001            278     49.4797    9.7832 Mergentheim, Bad                                                                 Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
03268 20021101 20240206            900     48.1694    8.9433 Meßstetten-Appental                                                              Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
03271 20041101 20240206            314     48.8548   12.9189 Metten                                                                           Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03274 19921001 19941001            415     49.5070    6.5215 Mettlach-Orscholz (Kurort)                                                       Saarland                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
03278 20090401 20240206            354     48.5377    9.2734 Metzingen                                                                        Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
03284 20050501 20240206            240     49.6692    9.0085 Michelstadt                                                                      Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03287 19871001 20240206            453     49.7177    9.0997 Michelstadt-Vielbrunn                                                            Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03289 20041101 20240206            356     50.7281   11.7838 Schmieritz-Weltwitz                                                              Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
03307 20080401 20230102            984     47.4779   11.2653 Mittenwald-Buckelwiesen                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03319 20060901 20240206            239     49.7644    9.2530 Röllbach                                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03321 20230501 20240206             76     51.1313    6.3608 Mönchengladbach-Hilderath                                                        Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
03340 20050501 20220329            265     50.4383    7.8061 Montabaur                                                                        Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
03348 20040601 20240206            241     51.7209    9.8351 Moringen-Lutterbeck                                                              Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
03362 20020101 20240206            243     48.9721    8.8735 Mühlacker                                                                        Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
03366 19550101 20240206            406     48.2790   12.5024 Mühldorf                                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03376 19910101 20240206             63     52.5176   14.1232 Müncheberg                                                                       Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
03379 19970701 20240206            515     48.1632   11.5429 München-Stadt                                                                    Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03382 19480101 19540101            521     48.1441   11.6000 München-Bogenhausen                                                              Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03385 19820101 19990331            515     48.1660   11.5011 München-Nymphenburg                                                              Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03390 19490101 19920517            529     48.1369   11.7094 München-Riem                                                                     Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03402 20021101 20240206            755     48.3851    9.4837 Münsingen-Apfelstetten                                                           Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
03404 19480101 19891001             62     51.9494    7.5906 Münster                                                                          Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
03426 20040601 20240206            127     51.5660   14.7008 Muskau, Bad                                                                      Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
03442 20041001 20240206            149     50.3574    8.7506 Nauheim, Bad                                                                     Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03478 19760701 20050818             81     53.5468   13.1914 Neubrandenburg                                                                   Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03484 20020101 20240206            380     48.7085   11.2147 Neuburg an der Donau                                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03485 20050501 20240206            486     48.3115   10.3773 Neuburg/Kammel-Langenhaslach                                                     Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03490 20040901 20240206            111     50.5346    7.0853 Neuenahr, Bad-Ahrweiler                                                          Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
03509 20041001 20240206             78     53.1020   13.0421 Stechlin-Menz                                                                    Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
03513 19890501 20240206            845     50.5003   11.1345 Neuhaus am Rennweg                                                               Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
03527 20040501 20240206            500     50.8923    9.4050 Neukirchen-Hauptschwenda                                                         Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03540 20041101 20240206            195     50.8446    7.3720 Neunkirchen-Seelscheid-Krawinkel                                                 Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
03545 20050301 20240206            236     49.3440    7.2297 Neunkirchen-Wellesweiler                                                         Saarland                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
03552 19730101 20190408             38     52.9037   12.8071 Neuruppin                                                                        Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
03571 20080301 20240206            452     49.8174   11.8638 Neustadt am Kulm-Filchendorf                                                     Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03575 19540101 19830101            163     49.3570    8.1405 Neustadt/Weinstraße                                                              Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
03577 19510101 19760701             64     53.3585   13.0502 Neustrelitz                                                                      Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03591 20040601 20240206            350     50.6743    6.4240 Nideggen-Schmidt                                                                 Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
03603 20020101 20240206            459     49.3895    9.9666 Niederstetten                                                                    Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
03605 19750601 19780601            451     48.5334   10.2427 Niederstotzingen                                                                 Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
03612 20070401 20240206             25     52.6711    9.2229 Nienburg                                                                         Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
03621 20060101 20240206            435     48.8253   10.5067 Reimlingen                                                                       Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03623 20020101 20240206            110     50.8294    6.6601 Nörvenich-Niederbolheim                                                          Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
03631 19490101 20240206             12     53.7123    7.1519 Norderney                                                                        Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
03639 20020101 20240206             26     53.7647    8.6584 Nordholz-Wanhöden                                                                Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
03659 19510101 19950327            627     50.3391    6.9501 Nürburg                                                                          Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
03660 19950302 20240206            485     50.3602    6.8697 Nürburg-Barweiler                                                                Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
03667 20050301 20240206            369     49.4258   11.2539 Nürnberg-Netzstall                                                               Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03668 19510101 20240206            314     49.5030   11.0549 Nürnberg                                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03671 19790101 19810401            280     48.6321    9.3261 Nürtingen                                                                        Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
03679 20061101 20240206            518     47.6187   12.1665 Kiefersfelden-Gach                                                               Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03702 20030101 20061231            515     47.8780    7.8288 Münstertal-Obermünstertal                                                        Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
03730 19480101 20240206            806     47.3984   10.2759 Oberstdorf                                                                       Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03734 20040701 20240206            232     49.1280    9.3525 Obersulm-Willsbach                                                               Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
03739 20050301 20240206            596     49.4521   12.4365 Oberviechtach                                                                    Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03761 19550101 20240206            276     49.2070    9.5176 Öhringen                                                                         Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
03791 19910101 20121001             11     53.1763    8.1824 Oldenburg                                                                        Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
03811 19820701 20240206            150     51.2960   13.0928 Oschatz                                                                          Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
03815 19510101 20101130             95     52.2553    8.0534 Osnabrück                                                                        Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
03821 19840801 20240206            244     51.0872   11.9293 Osterfeld                                                                        Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
03836 20060301 20240206            314     50.4538   10.2211 Ostheim v.d. Rhön                                                                Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03857 20050101 20240206            886     47.6362   10.3892 Oy-Mittelberg-Petersthal                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03875 20050101 20240206            549     49.1510   11.6896 Parsberg/Oberpfalz-Eglwang                                                       Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03879 19480101 19970101            409     48.5779   13.4694 Passau-Oberhaus                                                                  Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03897 20020101 20240206              2     54.0893   10.8773 Pelzerhaken                                                                      Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
03904 20040901 20240206            152     49.5354    6.3789 Perl-Nennig                                                                      Saarland                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
03925 20050901 20240206            332     48.9329    8.6973 Pforzheim-Ispringen                                                              Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
03927 20040701 20240206            630     47.9345    9.2869 Pfullendorf                                                                      Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
03939 20041001 20240206            385     49.1912    7.5879 Pirmasens                                                                        Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
03946 19510101 20240206            387     50.4818   12.1300 Plauen                                                                           Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
03975 20050301 20240206            522     49.4777   11.5357 Pommelsbrunn-Mittelburg                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
03987 18930101 20240206             81     52.3812   13.0622 Potsdam                                                                          Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
04018 19820101 19830901            550     48.1877   11.2206 Puch                                                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04024 19820101 20240206             40     54.3643   13.4771 Putbus                                                                           Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04032 20061201 20240206            142     51.7953   11.1320 Quedlinburg                                                                      Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
04036 20070301 20240206            204     51.3895   11.5412 Querfurt-Mühle Lodersleben                                                       Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
04039 19880111 20240206             11     53.7331    9.8776 Quickborn                                                                        Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
04063 20030701 20240206             41     52.4461    8.5906 Rahden-Kleinendorf                                                               Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
04094 20040601 20240206            441     47.8062    9.6206 Weingarten, Kr. Ravensburg                                                       Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04104 19480101 20240206            365     49.0425   12.1019 Regensburg                                                                       Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04127 20050101 20240206            347     50.9906    7.6958 Reichshof-Eckenhagen                                                             Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
04154 20110201 20180630            345     51.1800    7.2505 Remscheid-Lennep                                                                 Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
04160 20040701 20240206            478     48.7425    8.9240 Renningen-Ihinger Hof                                                            Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04169 20021101 20240206            131     48.6703    7.9939 Rheinau-Memprechtshofen                                                          Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04174 20020101 20171220             40     52.2887    7.3866 Rheine-Bentlage                                                                  Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
04175 20040601 20240206            283     47.5590    7.7721 Rheinfelden                                                                      Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04177 20081101 20240206            116     48.9726    8.3301 Rheinstetten                                                                     Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04189 20040801 20240206            534     48.1479    9.4596 Altheim, Kreis Biberach                                                          Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04261 20060301 20240206            442     47.8753   12.1280 Rosenheim                                                                        Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04271 19470101 20240206              5     54.1803   12.0808 Rostock-Warnemünde                                                               Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04275 20041201 20240206             32     53.1289    9.3398 Rotenburg (Wümme)                                                                Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
04280 20020101 20240206            386     49.2162   11.1035 Roth                                                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04287 20050101 20240206            415     49.3849   10.1732 Rothenburg ob der Tauber                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04294 19820101 19970101            360     48.4704    8.9687 Rottenburg-Kiebingen                                                             Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04300 20040701 20240206            589     48.1815    8.6356 Rottweil                                                                         Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04301 20050301 20240206            102     49.8502    7.8710 Kreuznach, Bad                                                                   Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
04323 20050301 20240206            461     49.6468    7.8837 Ruppertsecken                                                                    Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
04336 19620501 20240206            319     49.2128    7.1077 Saarbrücken-Ensheim                                                              Saarland                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
04339 19560101 19710101            193     49.2231    7.0168 Saarbrücken-Sankt Johann                                                         Saarland                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
04347 20001101 20030708            293     51.5909   10.5691 Sachsa, Bad                                                                      Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
04349 20040601 20240206            251     48.9569    9.0711 Sachsenheim                                                                      Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04350 19710101 20081229            339     47.5619    7.9399 Säckingen, Bad (Bergseestr.)                                                     Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04354 20060101 20240206            457     48.7832   13.3146 Saldenburg-Entschenreuth                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04371 19500101 20240206            135     52.1042    8.7521 Salzuflen, Bad                                                                   Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
04373 19520101 19720101             29     52.8568   11.1319 Salzwedel                                                                        Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
04377 20050901 20240206            518     50.3518   10.0034 Sandberg                                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04393 19991201 20240206              5     54.3279    8.6031 Sankt Peter-Ording                                                               Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
04411 20020124 20240206            155     49.9195    8.9672 Schaafheim-Schlierbach                                                           Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04445 19891001 20240206            609     51.7658   10.6533 Wernigerode-Schierke                                                             Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
04464 19890801 20240206            501     50.5679   11.8041 Schleiz                                                                          Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
04466 19510101 20240206             43     54.5275    9.5487 Schleswig                                                                        Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
04477 20050531 20100501            993     47.8208    8.1860 Schluchsee                                                                       Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04480 20040901 20240206            230     50.3447    9.5533 Schlüchtern-Herolz                                                               Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04485 20050201 20170301            296     50.7250   10.4539 Schmalkalden, Kurort                                                             Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
04501 19780701 20240206            938     50.6545   10.7696 Schmücke                                                                         Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
04508 20040801 20240206            649     50.2968    6.4194 Schneifelforsthaus                                                               Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
04517 19961001 20081201            635     48.7859    8.6451 Schömberg, Kr. Calw                                                              Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04548 20070701 20240206            608     50.1847   12.0791 Schönwald/Ofr.-Brunn                                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04559 20050501 20240206            398     49.1644   12.6175 Schorndorf-Knöbling                                                              Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04560 20050201 20220102            265     50.4925    9.1226 Schotten                                                                         Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04584 19680401 19700401            444     48.3667   11.8000 Schwaigermoos                                                                    Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04592 20051201 20240206            356     49.3278   12.0871 Schwandorf                                                                       Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04605 20041101 20240206            277     50.6441   11.1936 Schwarzburg                                                                      Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
04625 19500101 20240206             59     53.6424   11.3871 Schwerin                                                                         Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04629 19930401 19991201             37     54.5166    9.1420 Schwesing                                                                        Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
04642 19761001 20240206             21     52.8911   11.7297 Seehausen                                                                        Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
04651 20041101 20240206            189     51.9040   10.1885 Seesen                                                                           Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
04665 19690101 19750514            431     49.5281    7.0417 Selbach (Tholey)                                                                 Saarland                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
04692 20080301 20181130            229     50.8534    7.9966 Siegen (Kläranlage)                                                              Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
04702 20021103 20071115            645     48.1000    9.2500 Sigmaringen (Flugplatz)                                                          Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04703 20021101 20240206            581     48.0719    9.1943 Sigmaringen-Laiz                                                                 Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04704 20050501 20240201            508     47.5776    9.7404 Sigmarszell-Zeisertsweiler                                                       Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04706 20050301 20240206            358     48.2718   13.0273 Simbach/Inn                                                                      Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04709 20111101 20240206            445     49.9996    7.5981 Simmern-Wahlbach                                                                 Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
04719 20020101 20070828            169     49.2447    8.8787 Sinsheim                                                                         Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04745 19660101 20240206             75     52.9604    9.7930 Soltau                                                                           Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
04748 20041101 20240206            185     51.3691   10.8800 Sondershausen                                                                    Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
04752 19510101 20080701            626     50.3746   11.1828 Sonneberg-Neufang                                                                Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
04763 20041001 20240206            265     51.0607    9.9266 Sontra                                                                           Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04813 20200801 20240206            318     50.0806   11.0467 Staffelstein, Bad-Stublang                                                       Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04841 20040701 20240206             -0     53.6946    8.8735 Steinau, Kr. Cuxhaven                                                            Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
04857 20040901 20240206              2     53.5534    9.6097 Mittelnkirchen-Hohenfelde                                                        Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
04878 20050201 20240206            504     51.6646   10.8811 Oberharz am Brocken-Stiege                                                       Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
04887 19480101 20240206            734     48.6656    9.8648 Stötten                                                                          Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04896 20050701 20221130             40     54.6654    9.8050 Wagersrott                                                                       Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
04911 19940501 20240206            351     48.8275   12.5597 Straubing                                                                        Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04926 19790401 20130514            224     48.7896    9.2167 Stuttgart (Neckartal)                                                            Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04927 19760101 19840801            286     48.7693    9.1814 Stuttgart-Stadt                                                                  Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04928 19770701 20240206            314     48.8281    9.2000 Stuttgart (Schnarrenberg)                                                        Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04931 19880101 20240206            371     48.6883    9.2235 Stuttgart-Echterdingen                                                           Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04933 19510101 19760101            401     48.7091    9.2147 Stuttgart-Hohenheim                                                              Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
04978 20021101 20240206            395     50.6390   10.0228 Tann/Rhön                                                                        Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
04997 20050301 20240206            196     50.9771   12.3419 Starkenberg-Tegkwitz                                                             Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
05009 19730101 20240206             33     53.7610   12.5574 Teterow                                                                          Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05014 20040701 20240206              7     53.2758    8.9857 Worpswede-Hüttenbusch                                                            Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
05017 20051101 20240206            633     50.4002   11.3888 Teuschnitz                                                                       Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05029 19750515 20240206            387     49.4737    7.0385 Tholey                                                                           Saarland                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
05046 20080301 20240206            501     49.8576   12.3542 Tirschenreuth-Lodermühl                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05049 19981106 20080501            846     47.8991    8.1460 Titisee-Neustadt-Titisee                                                         Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
05064 20041201 20240206             37     51.2897    6.4437 Tönisvorst                                                                       Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
05068 19530101 19710101             80     51.5833   13.0000 Torgau                                                                           Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
05097 20050101 20240206             10     54.0654   12.7655 Tribsees                                                                         Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05099 20080601 20240206            132     49.7326    6.6131 Trier-Zewen                                                                      Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
05100 19410101 20240206            261     49.7479    6.6583 Trier-Petrisberg                                                                 Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
05109 20020101 20240206             68     53.5998   13.3039 Trollenhagen                                                                     Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05111 20060401 20240206            560     48.0311   12.5396 Trostberg                                                                        Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05133 20040901 20240206            295     51.3344    8.9132 Twistetal-Mühlhausen                                                             Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05142 19510101 20240206              1     53.7445   14.0698 Ueckermünde                                                                      Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05146 20040601 20240206             50     52.9414   10.5289 Uelzen                                                                           Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
05149 20050101 20221004            318     49.5679   10.1969 Gollhofen                                                                        Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05155 19480101 20140901            567     48.3837    9.9524 Ulm                                                                              Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
05158 19890101 20240206            159     52.1601   11.1759 Ummendorf                                                                        Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
05229 20040801 20240206            719     48.0453    8.4608 Villingen-Schwenningen                                                           Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
05275 20040601 20240206            105     49.2445    8.5374 Waghäusel-Kirrlach                                                               Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
05277 20020101 20090630            349     50.8119    9.1280 Wahlen                                                                           Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05279 20040901 20240206            176     51.6194    9.5749 Wesertal-Lippoldsberg                                                            Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05280 20070301 20240206             33     53.9224   10.2267 Wittenborn                                                                       Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
05282 19410101 19710101            246     51.1197   13.6744 Wahnsdorf bei Dresden                                                            Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
05300 20040701 20240206            380     50.2596    8.3607 Waldems-Reinborn                                                                 Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05335 20060801 20240206            352     50.8963   10.5483 Waltershausen                                                                    Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
05347 20010402 20240206            236     51.5039    9.1118 Warburg                                                                          Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
05349 19810101 20240206             73     53.5196   12.6654 Waren (Müritz)                                                                   Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05371 19480101 20240206            920     50.4973    9.9427 Wasserkuppe                                                                      Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05397 19510101 20240206            440     49.6662   12.1844 Weiden                                                                           Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05404 19750101 20240206            477     48.4024   11.6946 Weihenstephan-Dürnast                                                            Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05419 19510101 20070630            264     50.9751   11.3076 Weimar                                                                           Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
05424 20070601 20240206            328     51.0177   11.3544 Weimar-Schöndorf                                                                 Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
05426 19540101 20240206            553     49.3758    8.1212 Weinbiet                                                                         Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
05431 19730101 19761001             24     53.0333   11.8000 Weisen bei Wittenberge                                                           Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
05433 20040901 20240206            380     49.5534    6.8120 Weiskirchen/Saar                                                                 Saarland                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
05440 19550101 20240206            439     49.0115   10.9308 Weißenburg-Emetzheim                                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05467 19560701 20120921           1832     47.7035   12.0119 Wendelstein                                                                      Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05480 20030910 20240206             85     51.5763    7.8879 Werl                                                                             Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
05490 19510101 20240206            233     51.8454   10.7686 Wernigerode                                                                      Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
05516 19960531 20240206              3     54.5283   11.0606 Fehmarn                                                                          Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
05538 20050101 20240206            551     47.8827   11.1576 Wielenbach (Demollstr.)                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05541 20040801 20240206            263     50.1321    8.3169 Wiesbaden-Auringen                                                               Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05546 19860701 20240206            187     52.1206   12.4586 Wiesenburg                                                                       Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
05562 20040601 20240206            571     48.6516    8.6801 Neubulach-Oberhaugstett                                                          Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
05629 19510101 20240206            105     51.8891   12.6446 Wittenberg                                                                       Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
05640 20020101 20240206             10     53.5503    7.6672 Wittmundhafen                                                                    Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
05643 20041101 20240206             68     53.1864   12.4949 Wittstock-Rote Mühle                                                             Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
05663 19820101 19960101            118     53.4618   13.6099 Woldegk                                                                          Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05664 20040701 20240206            296     48.2953    8.2391 Wolfach                                                                          Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
05665 19900101 20100501            677     47.8180    9.7970 Wolfegg                                                                          Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
05676 20100901 20240102             82     52.3962   10.6892 Wolfsburg (Südwest)                                                              Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
05688 20181101 20240206            881     47.7004    8.1057 Dachsberg-Wolpadingen                                                            Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
05692 20040901 20240206             88     49.6051    8.3659 Worms                                                                            Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
05705 19480101 20240206            268     49.7704    9.9576 Würzburg                                                                         Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05715 20020101 20240206             49     52.4626    9.4245 Wunstorf                                                                         Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
05717 20060901 20240206            134     51.2256    7.1052 Wuppertal-Buchenhofen                                                            Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
05719 20041001 20091210            235     51.2051    7.2000 Remscheid                                                                        Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
05731 20040801 20240206            395     47.6783    8.3801 Wutöschingen-Ofteringen                                                          Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
05732 19510101 19710101              9     54.6928    8.5271 Wrixum/Föhr                                                                      Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
05745 19810101 20240206             51     52.9664   13.3268 Zehdenick                                                                        Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
05750 20060301 20240206            264     51.0314   12.1495 Zeitz                                                                            Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
05779 19710101 20240206            877     50.7313   13.7516 Zinnwald-Georgenfeld                                                             Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
05792 19500101 20240206           2956     47.4210   10.9848 Zugspitze                                                                        Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05797 20051201 20240206            349     50.6879   12.4329 Lichtentanne                                                                     Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
05800 20020101 20240206            615     49.0280   13.2385 Zwiesel                                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05802 19480101 20031001            615     49.0007   13.2137 Zwieselberg                                                                      Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05822 20040701 20240206             42     52.8630    8.6989 Bassum                                                                           Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
05825 20040501 20240206             40     52.6198   12.7867 Berge                                                                            Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
05832 19510101 19541201             50     53.1007   11.0455 Dannenberg                                                                       Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
05839 19970701 20240206             -0     53.3881    7.2287 Emden                                                                            Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
05856 19970103 20240206            476     48.5451   13.3532 Fürstenzell                                                                      Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
05871 19970701 20240206            497     49.9463    7.2645 Hahn                                                                             Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
05906 19480101 20240206             98     49.5063    8.5584 Mannheim                                                                         Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
05930 19910101 20240206              1     54.6410   10.0238 Schönhagen (Ostseebad)                                                           Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
05941 20070301 20240206            686     47.6754   12.4698 Reit im Winkl                                                                    Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
06093 20040501 20240206             62     53.2139   10.4704 Wendisch Evern                                                                   Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
06105 20040501 20240206             15     54.3194    9.8051 Ostenfeld (Rendsburg)                                                            Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
06109 20040901 20240206             52     53.3837   14.3728 Grambow-Schwennenz                                                               Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
06129 20041101 20240206            291     51.0594   14.4266 Sohland/Spree                                                                    Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
06157 20071001 20240206              4     53.6411    8.0809 Wangerland-Hooksiel                                                              Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
06158 20041101 20240206            454     49.2249   10.6085 Weidenbach-Weiherschneidbach                                                     Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
06159 20081201 20240206              8     52.9542    7.3197 Dörpen                                                                           Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
06163 20010401 20240206             27     54.1654   10.3519 Dörnick                                                                          Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
06170 20040601 20240206             39     52.0192   14.7254 Coschen                                                                          Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
06182 20000401 20120327            404     48.7757   12.1743 Mallersdorf-Pfaffenberg                                                          Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
06184 20020101 20090615              6     53.5333    8.1667 Wilhelmshaven (Flugplatz)                                                        Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
06186 20040801 20190527            268     50.1989    7.8651 Nastätten                                                                        Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
06192 19990801 20081101            115     49.8083    7.8458 Münster am Stein, Bad                                                            Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
06197 20020101 20240206            258     51.8664    9.2710 Lügde-Paenbruch                                                                  Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
06199 20041001 20240206             17     54.2484   13.0419 Steinhagen-Negast                                                                Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
06217 20041001 20240206            190     49.2406    6.9351 Saarbrücken-Burbach                                                              Saarland                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
06242 20020107 20210701             64     50.4088    7.4890 Mülheim-Kärlich                                                                  Rheinland-Pfalz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
06243 20020101 20240206             96     49.2506    8.4422 Philippsburg KKW                                                                 Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
06244 20020101 20240206            145     49.3650    9.0804 Obrigheim                                                                        Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
06245 20020101 20240206            180     49.0423    9.1733 Neckarwestheim KKW                                                               Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
06246 20020103 20240206            368     47.6213    8.2167 Waldshut KKW                                                                     Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
06247 20020101 20240206            307     47.6078    8.1813 Dogern (Leibstadt)                                                               Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
06254 20020101 20070702             19     53.5408    9.9528 Hamburg-Lotsenhöft                                                               Hamburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
06255 20020107 20181231            351     49.4667    6.3968 Perl/Saar                                                                        Saarland                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
06256 20020101 20240206            201     47.9100    7.5838 Bremgarten (Fessenheim)                                                          Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
06258 20030101 20240206            461     47.6845    9.4409 Friedrichshafen-Unterraderach                                                    Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
06259 20040601 20240206            524     49.0210    9.6033 Großerlach-Mannenweiler                                                          Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
06260 20021201 20240206            385     49.3328    9.7040 Ingelfingen-Stachenhausen                                                        Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
06262 20021101 20240206            412     48.7695    9.8737 Schwäbisch Gmünd-Weiler                                                          Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
06263 20040701 20240206            445     47.7738    8.8219 Singen                                                                           Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
06264 20040601 20240206            457     51.4140    8.6500 Brilon-Thülen                                                                    Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
06265 20040501 20240206             36     52.3613   12.3867 Wusterwitz                                                                       Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
06266 20040901 20240206            112     52.0304   10.9626 Huy-Pabstorf                                                                     Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
06272 20041001 20240206            284     50.8426   10.2518 Salzungen, Bad-Gräfen-Nitzendorf                                                 Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
06273 20040601 20240206             36     52.5075   11.8551 Demker                                                                           Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
06275 20040701 20240206            327     48.6705    9.4627 Notzingen                                                                        Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
06305 20041201 20240206            193     51.2061   10.4978 Mühlhausen/Thüringen-Görmar                                                      Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
06310 20040801 20240206              1     54.1049   13.8239 Karlshagen                                                                       Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
06312 20041101 20200930            362     49.5314   10.6418 Markt Erlbach-Mosbach                                                            Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
06314 20050801 20240206            306     51.0507   13.3003 Nossen                                                                           Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
06336 20051101 20240206            288     50.0132    9.6540 Lohr/Main-Halsbach                                                               Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
06337 20040801 20240206             59     51.7663    7.5194 Lüdinghausen-Brochtrup                                                           Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
06344 20041201 20240206            168     50.3940    8.1423 Runkel-Ennerich                                                                  Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
06346 20050201 20240206            531     48.2070   11.2035 Maisach-Galgen                                                                   Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
06347 20050301 20240206            305     50.0579   10.2972 Schonungen-Mainberg                                                              Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07075 20050201 20240206            429     48.7020   11.8493 Elsendorf-Horneck                                                                Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07099 20041101 20211004            187     52.0111   10.3966 Liebenburg-Othfresen                                                             Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
07105 20050601 20240206            719     47.8350   12.6548 Siegsdorf-Höll                                                                   Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07106 20060901 20240206            105     52.0714    8.4565 Bielefeld-Deppendorf                                                             Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
07135 19750601 19960701            565     47.9655    9.6804 Aulendorf-Haslach                                                                Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
07187 20041201 20240206            194     49.7636    9.4063 Freudenberg/Main-Boxtal                                                          Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
07244 19810101 20040930             62     53.1424   13.0319 Neuglobsow (HM)                                                                  Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
07298 20050701 20240206              4     54.5268    9.0425 Hattstedt                                                                        Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
07319 20050301 20240206            435     48.7374   10.7393 Donauwörth-Osterweiler                                                           Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07321 20050901 20240206            160     51.1507   11.3321 Olbersleben                                                                      Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
07329 20051101 20240206            465     50.5467   12.2863 Treuen                                                                           Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
07330 20051001 20240206            159     51.4633    7.9780 Arnsberg-Neheim                                                                  Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
07331 20050901 20240206            467     48.6099   10.2674 Hermaringen-Allewind                                                             Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
07341 20050716 20240206            119     50.0900    8.7862 Offenbach-Wetterpark                                                             Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07343 20060401 20240206            689     50.6200   13.4817 Deutschneudorf-Brüderwiese                                                       Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
07350 20060801 20240206            585     49.1088   12.8231 Prackenbach-Neuhäusl                                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07351 20050908 20240206            115     53.3176   13.4175 Feldberg/Mecklenburg                                                             Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07364 20070101 20240206             74     51.6818   12.3053 Jeßnitz                                                                          Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
07367 20071201 20240206            144     51.9643    9.8072 Alfeld                                                                           Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
07368 20071101 20240206            312     51.0007   10.3621 Eisenach                                                                         Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
07369 20071101 20240206            475     49.1623   10.3661 Feuchtwangen-Heilbronn                                                           Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07370 20061211 20240206            499     49.3910   12.6838 Waldmünchen                                                                      Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07373 20060301 20240206              3     53.5984    6.7024 Borkum-Flugplatz                                                                 Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
07374 20060301 20240206             46     52.0813    6.9409 Ahaus                                                                            Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
07389 20061201 20240206             83     52.7461   13.8427 Heckelberg                                                                       Brandenburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
07393 20100101 20240206            116     51.4492   14.2533 Hoyerswerda                                                                      Sachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
07394 20060601 20240206            622     50.0315   11.9745 Wunsiedel-Schönbrunn                                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07395 20071201 20240206            351     48.6595   12.5388 Gottfrieding                                                                     Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07396 20080501 20240206            740     50.5084    9.2246 Hoherodskopf/Vogelsberg                                                          Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07403 20070330 20240206            672     47.7955   10.0325 Leutkirch-Herlazhofen                                                            Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
07410 20110201 20240206            350     50.7513    9.0224 Neu-Ulrichstein                                                                  Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07412 20061001 20240206            340     50.0083    9.4238 Neuhütten/Spessart                                                               Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07419 20061201 20240206            389     50.6610   12.0756 Langenwetzendorf-Göttendorf                                                      Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
07420 20070401 20240206            246     51.1044   11.7112 Naumburg/Saale-Kreipitzsch                                                       Sachsen-Anhalt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
07424 20061201 20240206            457     47.7724   12.9073 Piding                                                                           Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07427 20070901 20240206             17     54.0188    9.9255 Padenstedt (Pony-Park)                                                           Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
07428 20070501 20240206            397     50.4167   10.8156 Veilsdorf                                                                        Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
07431 20071101 20240206            604     48.0130   11.5524 Oberhaching-Laufzorn                                                             Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
07432 20070501 20240206             71     52.6423   10.6628 Wittingen-Vorhop                                                                 Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
13667 20061123 20080706            274     48.0006    7.8450 Freiburg-Mitte                                                                   Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
13670 20070601 20240206             24     51.5088    6.7018 Duisburg-Baerl                                                                   Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
13674 20070801 20240206            237     49.2943    8.9053 Waibstadt                                                                        Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
13675 20071101 20240206             75     52.0818    9.4077 Hameln-Hastenbeck                                                                Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
13696 20071201 20240206             60     51.5966    7.4048 Waltrop-Abdinghof                                                                Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
13700 20080501 20240206            203     51.3329    7.3412 Gevelsberg-Oberbröking                                                           Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
13710 20080401 20240206            490     48.5734   12.2576 Landshut-Reithof                                                                 Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
13711 20071201 20240206            289     50.6820   11.5150 Krölpa-Rockendorf                                                                Thüringen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
13713 20071101 20240206            386     51.0899    7.6289 Meinerzhagen-Redlendorf                                                          Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
13776 20080301 20110104             85     52.1789    9.9524 Hildesheim-Drispenstedt                                                          Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
13777 20080601 20240206            109     52.2467   10.9592 Helmstedt-Emmerstedt                                                             Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
13904 20080915 20100426              3     55.0000    6.3333 Nordseeboje 2                                                                    Hamburg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
13965 20081201 20240206            619     48.2639    8.8134 Balingen-Bronnhaupten                                                            Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
14003 19610103 19920629            728     47.8619   10.6144 Kaufbeuren (Flugplatz)                                                           Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
15000 20110401 20240206            231     50.7983    6.0244 Aachen-Orsbach                                                                   Nordrhein-Westfalen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
15207 20131101 20240206            317     51.2835    9.3590 Schauenburg-Elgershausen                                                         Hessen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
15444 20140901 20240206            593     48.4418    9.9216 Ulm-Mähringen                                                                    Baden-Württemberg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
15555 20160501 20240206            815     47.8761   10.5849 Kaufbeuren-Oberbeuren                                                            Bayern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
15813 20220301 20240206             40     52.5126    7.4131 Lingen-Baccum                                                                    Niedersachsen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
19171 20200901 20240206             13     54.0039    9.8555 Hasenkrug-Hardebek                                                               Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
19172 20200901 20240206             48     54.0246    9.3880 Wacken                                                                           Schleswig-Holstein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
19207 20230401 20240206             16     53.8178   12.0645 Gülzow-Prüzen                                                                    Mecklenburg-Vorpommern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
"""

### make df with all 6 above lists as columns
df_meta = pd.DataFrame(list(zip(stations_id_list, stationshoehe_list, geobreite_list, geolaenge_list, stationsname_list, bundesland_list)), columns =['id','hoehe', 'geobreite', 'geolaenge', 'stationsname', 'bundesland'])
#### turn id column to index
df_meta.set_index('id', inplace=True)

### save df as df_meta in data interim folder to clean it in weather_data_cleaning.py
df_meta.to_csv(r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather/data/interim/df_meta.csv")

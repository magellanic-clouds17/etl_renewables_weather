import pandas as pd
import folium
from folium.plugins import MarkerCluster

# extract air temperature data using download_and_extract_file function and \data\interim\df_sample_stations.csv

## List of filenames
filename_string_raw ="""
stundenwerte_TU_00044_akt.zip
stundenwerte_TU_00073_akt.zip
stundenwerte_TU_00078_akt.zip
stundenwerte_TU_00091_akt.zip
stundenwerte_TU_00096_akt.zip
stundenwerte_TU_00102_akt.zip
stundenwerte_TU_00125_akt.zip
stundenwerte_TU_00131_akt.zip
stundenwerte_TU_00142_akt.zip
stundenwerte_TU_00150_akt.zip
stundenwerte_TU_00151_akt.zip
stundenwerte_TU_00154_akt.zip
stundenwerte_TU_00161_akt.zip
stundenwerte_TU_00164_akt.zip
stundenwerte_TU_00167_akt.zip
stundenwerte_TU_00183_akt.zip
stundenwerte_TU_00191_akt.zip
stundenwerte_TU_00198_akt.zip
stundenwerte_TU_00217_akt.zip
stundenwerte_TU_00222_akt.zip
stundenwerte_TU_00232_akt.zip
stundenwerte_TU_00257_akt.zip
stundenwerte_TU_00259_akt.zip
stundenwerte_TU_00282_akt.zip
stundenwerte_TU_00294_akt.zip
stundenwerte_TU_00298_akt.zip
stundenwerte_TU_00303_akt.zip
stundenwerte_TU_00314_akt.zip
stundenwerte_TU_00320_akt.zip
stundenwerte_TU_00330_akt.zip
stundenwerte_TU_00342_akt.zip
stundenwerte_TU_00368_akt.zip
stundenwerte_TU_00377_akt.zip
stundenwerte_TU_00379_akt.zip
stundenwerte_TU_00390_akt.zip
stundenwerte_TU_00400_akt.zip
stundenwerte_TU_00403_akt.zip
stundenwerte_TU_00420_akt.zip
stundenwerte_TU_00427_akt.zip
stundenwerte_TU_00430_akt.zip
stundenwerte_TU_00433_akt.zip
stundenwerte_TU_00445_akt.zip
stundenwerte_TU_00460_akt.zip
stundenwerte_TU_00535_akt.zip
stundenwerte_TU_00555_akt.zip
stundenwerte_TU_00591_akt.zip
stundenwerte_TU_00596_akt.zip
stundenwerte_TU_00603_akt.zip
stundenwerte_TU_00617_akt.zip
stundenwerte_TU_00656_akt.zip
stundenwerte_TU_00662_akt.zip
stundenwerte_TU_00691_akt.zip
stundenwerte_TU_00701_akt.zip
stundenwerte_TU_00704_akt.zip
stundenwerte_TU_00722_akt.zip
stundenwerte_TU_00755_akt.zip
stundenwerte_TU_00757_akt.zip
stundenwerte_TU_00760_akt.zip
stundenwerte_TU_00766_akt.zip
stundenwerte_TU_00769_akt.zip
stundenwerte_TU_00817_akt.zip
stundenwerte_TU_00840_akt.zip
stundenwerte_TU_00850_akt.zip
stundenwerte_TU_00853_akt.zip
stundenwerte_TU_00856_akt.zip
stundenwerte_TU_00860_akt.zip
stundenwerte_TU_00867_akt.zip
stundenwerte_TU_00880_akt.zip
stundenwerte_TU_00891_akt.zip
stundenwerte_TU_00896_akt.zip
stundenwerte_TU_00917_akt.zip
stundenwerte_TU_00953_akt.zip
stundenwerte_TU_00954_akt.zip
stundenwerte_TU_00963_akt.zip
stundenwerte_TU_00979_akt.zip
stundenwerte_TU_00983_akt.zip
stundenwerte_TU_00991_akt.zip
stundenwerte_TU_01001_akt.zip
stundenwerte_TU_01048_akt.zip
stundenwerte_TU_01050_akt.zip
stundenwerte_TU_01051_akt.zip
stundenwerte_TU_01052_akt.zip
stundenwerte_TU_01072_akt.zip
stundenwerte_TU_01078_akt.zip
stundenwerte_TU_01103_akt.zip
stundenwerte_TU_01107_akt.zip
stundenwerte_TU_01161_akt.zip
stundenwerte_TU_01197_akt.zip
stundenwerte_TU_01200_akt.zip
stundenwerte_TU_01207_akt.zip
stundenwerte_TU_01214_akt.zip
stundenwerte_TU_01224_akt.zip
stundenwerte_TU_01228_akt.zip
stundenwerte_TU_01246_akt.zip
stundenwerte_TU_01255_akt.zip
stundenwerte_TU_01262_akt.zip
stundenwerte_TU_01266_akt.zip
stundenwerte_TU_01270_akt.zip
stundenwerte_TU_01279_akt.zip
stundenwerte_TU_01297_akt.zip
stundenwerte_TU_01300_akt.zip
stundenwerte_TU_01303_akt.zip
stundenwerte_TU_01327_akt.zip
stundenwerte_TU_01332_akt.zip
stundenwerte_TU_01339_akt.zip
stundenwerte_TU_01346_akt.zip
stundenwerte_TU_01357_akt.zip
stundenwerte_TU_01358_akt.zip
stundenwerte_TU_01411_akt.zip
stundenwerte_TU_01420_akt.zip
stundenwerte_TU_01424_akt.zip
stundenwerte_TU_01443_akt.zip
stundenwerte_TU_01451_akt.zip
stundenwerte_TU_01468_akt.zip
stundenwerte_TU_01503_akt.zip
stundenwerte_TU_01504_akt.zip
stundenwerte_TU_01526_akt.zip
stundenwerte_TU_01544_akt.zip
stundenwerte_TU_01550_akt.zip
stundenwerte_TU_01572_akt.zip
stundenwerte_TU_01580_akt.zip
stundenwerte_TU_01584_akt.zip
stundenwerte_TU_01587_akt.zip
stundenwerte_TU_01590_akt.zip
stundenwerte_TU_01602_akt.zip
stundenwerte_TU_01605_akt.zip
stundenwerte_TU_01612_akt.zip
stundenwerte_TU_01639_akt.zip
stundenwerte_TU_01645_akt.zip
stundenwerte_TU_01666_akt.zip
stundenwerte_TU_01684_akt.zip
stundenwerte_TU_01691_akt.zip
stundenwerte_TU_01694_akt.zip
stundenwerte_TU_01721_akt.zip
stundenwerte_TU_01735_akt.zip
stundenwerte_TU_01736_akt.zip
stundenwerte_TU_01757_akt.zip
stundenwerte_TU_01759_akt.zip
stundenwerte_TU_01766_akt.zip
stundenwerte_TU_01792_akt.zip
stundenwerte_TU_01803_akt.zip
stundenwerte_TU_01832_akt.zip
stundenwerte_TU_01863_akt.zip
stundenwerte_TU_01869_akt.zip
stundenwerte_TU_01886_akt.zip
stundenwerte_TU_01964_akt.zip
stundenwerte_TU_01975_akt.zip
stundenwerte_TU_01981_akt.zip
stundenwerte_TU_02014_akt.zip
stundenwerte_TU_02023_akt.zip
stundenwerte_TU_02039_akt.zip
stundenwerte_TU_02044_akt.zip
stundenwerte_TU_02074_akt.zip
stundenwerte_TU_02110_akt.zip
stundenwerte_TU_02115_akt.zip
stundenwerte_TU_02171_akt.zip
stundenwerte_TU_02174_akt.zip
stundenwerte_TU_02201_akt.zip
stundenwerte_TU_02211_akt.zip
stundenwerte_TU_02252_akt.zip
stundenwerte_TU_02261_akt.zip
stundenwerte_TU_02290_akt.zip
stundenwerte_TU_02303_akt.zip
stundenwerte_TU_02306_akt.zip
stundenwerte_TU_02315_akt.zip
stundenwerte_TU_02319_akt.zip
stundenwerte_TU_02323_akt.zip
stundenwerte_TU_02362_akt.zip
stundenwerte_TU_02385_akt.zip
stundenwerte_TU_02410_akt.zip
stundenwerte_TU_02429_akt.zip
stundenwerte_TU_02437_akt.zip
stundenwerte_TU_02444_akt.zip
stundenwerte_TU_02480_akt.zip
stundenwerte_TU_02483_akt.zip
stundenwerte_TU_02485_akt.zip
stundenwerte_TU_02486_akt.zip
stundenwerte_TU_02497_akt.zip
stundenwerte_TU_02559_akt.zip
stundenwerte_TU_02564_akt.zip
stundenwerte_TU_02575_akt.zip
stundenwerte_TU_02578_akt.zip
stundenwerte_TU_02597_akt.zip
stundenwerte_TU_02600_akt.zip
stundenwerte_TU_02601_akt.zip
stundenwerte_TU_02618_akt.zip
stundenwerte_TU_02627_akt.zip
stundenwerte_TU_02629_akt.zip
stundenwerte_TU_02638_akt.zip
stundenwerte_TU_02641_akt.zip
stundenwerte_TU_02667_akt.zip
stundenwerte_TU_02680_akt.zip
stundenwerte_TU_02700_akt.zip
stundenwerte_TU_02704_akt.zip
stundenwerte_TU_02708_akt.zip
stundenwerte_TU_02712_akt.zip
stundenwerte_TU_02750_akt.zip
stundenwerte_TU_02773_akt.zip
stundenwerte_TU_02794_akt.zip
stundenwerte_TU_02796_akt.zip
stundenwerte_TU_02812_akt.zip
stundenwerte_TU_02814_akt.zip
stundenwerte_TU_02856_akt.zip
stundenwerte_TU_02878_akt.zip
stundenwerte_TU_02886_akt.zip
stundenwerte_TU_02905_akt.zip
stundenwerte_TU_02907_akt.zip
stundenwerte_TU_02925_akt.zip
stundenwerte_TU_02928_akt.zip
stundenwerte_TU_02932_akt.zip
stundenwerte_TU_02947_akt.zip
stundenwerte_TU_02951_akt.zip
stundenwerte_TU_02953_akt.zip
stundenwerte_TU_02961_akt.zip
stundenwerte_TU_02968_akt.zip
stundenwerte_TU_02985_akt.zip
stundenwerte_TU_03015_akt.zip
stundenwerte_TU_03028_akt.zip
stundenwerte_TU_03031_akt.zip
stundenwerte_TU_03032_akt.zip
stundenwerte_TU_03034_akt.zip
stundenwerte_TU_03042_akt.zip
stundenwerte_TU_03083_akt.zip
stundenwerte_TU_03086_akt.zip
stundenwerte_TU_03093_akt.zip
stundenwerte_TU_03098_akt.zip
stundenwerte_TU_03126_akt.zip
stundenwerte_TU_03137_akt.zip
stundenwerte_TU_03147_akt.zip
stundenwerte_TU_03155_akt.zip
stundenwerte_TU_03158_akt.zip
stundenwerte_TU_03164_akt.zip
stundenwerte_TU_03166_akt.zip
stundenwerte_TU_03167_akt.zip
stundenwerte_TU_03181_akt.zip
stundenwerte_TU_03196_akt.zip
stundenwerte_TU_03204_akt.zip
stundenwerte_TU_03226_akt.zip
stundenwerte_TU_03231_akt.zip
stundenwerte_TU_03234_akt.zip
stundenwerte_TU_03244_akt.zip
stundenwerte_TU_03254_akt.zip
stundenwerte_TU_03257_akt.zip
stundenwerte_TU_03268_akt.zip
stundenwerte_TU_03271_akt.zip
stundenwerte_TU_03278_akt.zip
stundenwerte_TU_03284_akt.zip
stundenwerte_TU_03287_akt.zip
stundenwerte_TU_03289_akt.zip
stundenwerte_TU_03307_akt.zip
stundenwerte_TU_03319_akt.zip
stundenwerte_TU_03321_akt.zip
stundenwerte_TU_03340_akt.zip
stundenwerte_TU_03348_akt.zip
stundenwerte_TU_03362_akt.zip
stundenwerte_TU_03366_akt.zip
stundenwerte_TU_03376_akt.zip
stundenwerte_TU_03379_akt.zip
stundenwerte_TU_03402_akt.zip
stundenwerte_TU_03426_akt.zip
stundenwerte_TU_03442_akt.zip
stundenwerte_TU_03484_akt.zip
stundenwerte_TU_03485_akt.zip
stundenwerte_TU_03490_akt.zip
stundenwerte_TU_03509_akt.zip
stundenwerte_TU_03513_akt.zip
stundenwerte_TU_03527_akt.zip
stundenwerte_TU_03540_akt.zip
stundenwerte_TU_03545_akt.zip
stundenwerte_TU_03571_akt.zip
stundenwerte_TU_03591_akt.zip
stundenwerte_TU_03603_akt.zip
stundenwerte_TU_03612_akt.zip
stundenwerte_TU_03621_akt.zip
stundenwerte_TU_03623_akt.zip
stundenwerte_TU_03631_akt.zip
stundenwerte_TU_03639_akt.zip
stundenwerte_TU_03660_akt.zip
stundenwerte_TU_03667_akt.zip
stundenwerte_TU_03668_akt.zip
stundenwerte_TU_03679_akt.zip
stundenwerte_TU_03730_akt.zip
stundenwerte_TU_03734_akt.zip
stundenwerte_TU_03739_akt.zip
stundenwerte_TU_03761_akt.zip
stundenwerte_TU_03811_akt.zip
stundenwerte_TU_03821_akt.zip
stundenwerte_TU_03836_akt.zip
stundenwerte_TU_03857_akt.zip
stundenwerte_TU_03875_akt.zip
stundenwerte_TU_03897_akt.zip
stundenwerte_TU_03904_akt.zip
stundenwerte_TU_03925_akt.zip
stundenwerte_TU_03927_akt.zip
stundenwerte_TU_03939_akt.zip
stundenwerte_TU_03946_akt.zip
stundenwerte_TU_03975_akt.zip
stundenwerte_TU_03987_akt.zip
stundenwerte_TU_04024_akt.zip
stundenwerte_TU_04032_akt.zip
stundenwerte_TU_04036_akt.zip
stundenwerte_TU_04039_akt.zip
stundenwerte_TU_04063_akt.zip
stundenwerte_TU_04094_akt.zip
stundenwerte_TU_04104_akt.zip
stundenwerte_TU_04127_akt.zip
stundenwerte_TU_04160_akt.zip
stundenwerte_TU_04169_akt.zip
stundenwerte_TU_04175_akt.zip
stundenwerte_TU_04177_akt.zip
stundenwerte_TU_04189_akt.zip
stundenwerte_TU_04261_akt.zip
stundenwerte_TU_04271_akt.zip
stundenwerte_TU_04275_akt.zip
stundenwerte_TU_04280_akt.zip
stundenwerte_TU_04287_akt.zip
stundenwerte_TU_04300_akt.zip
stundenwerte_TU_04301_akt.zip
stundenwerte_TU_04323_akt.zip
stundenwerte_TU_04336_akt.zip
stundenwerte_TU_04349_akt.zip
stundenwerte_TU_04354_akt.zip
stundenwerte_TU_04371_akt.zip
stundenwerte_TU_04377_akt.zip
stundenwerte_TU_04393_akt.zip
stundenwerte_TU_04411_akt.zip
stundenwerte_TU_04445_akt.zip
stundenwerte_TU_04464_akt.zip
stundenwerte_TU_04466_akt.zip
stundenwerte_TU_04480_akt.zip
stundenwerte_TU_04501_akt.zip
stundenwerte_TU_04508_akt.zip
stundenwerte_TU_04548_akt.zip
stundenwerte_TU_04559_akt.zip
stundenwerte_TU_04560_akt.zip
stundenwerte_TU_04592_akt.zip
stundenwerte_TU_04605_akt.zip
stundenwerte_TU_04625_akt.zip
stundenwerte_TU_04642_akt.zip
stundenwerte_TU_04651_akt.zip
stundenwerte_TU_04703_akt.zip
stundenwerte_TU_04704_akt.zip
stundenwerte_TU_04706_akt.zip
stundenwerte_TU_04709_akt.zip
stundenwerte_TU_04745_akt.zip
stundenwerte_TU_04748_akt.zip
stundenwerte_TU_04763_akt.zip
stundenwerte_TU_04813_akt.zip
stundenwerte_TU_04841_akt.zip
stundenwerte_TU_04857_akt.zip
stundenwerte_TU_04878_akt.zip
stundenwerte_TU_04887_akt.zip
stundenwerte_TU_04896_akt.zip
stundenwerte_TU_04911_akt.zip
stundenwerte_TU_04928_akt.zip
stundenwerte_TU_04931_akt.zip
stundenwerte_TU_04978_akt.zip
stundenwerte_TU_04997_akt.zip
stundenwerte_TU_05009_akt.zip
stundenwerte_TU_05014_akt.zip
stundenwerte_TU_05017_akt.zip
stundenwerte_TU_05029_akt.zip
stundenwerte_TU_05046_akt.zip
stundenwerte_TU_05064_akt.zip
stundenwerte_TU_05097_akt.zip
stundenwerte_TU_05099_akt.zip
stundenwerte_TU_05100_akt.zip
stundenwerte_TU_05109_akt.zip
stundenwerte_TU_05111_akt.zip
stundenwerte_TU_05133_akt.zip
stundenwerte_TU_05142_akt.zip
stundenwerte_TU_05146_akt.zip
stundenwerte_TU_05149_akt.zip
stundenwerte_TU_05158_akt.zip
stundenwerte_TU_05229_akt.zip
stundenwerte_TU_05275_akt.zip
stundenwerte_TU_05279_akt.zip
stundenwerte_TU_05280_akt.zip
stundenwerte_TU_05300_akt.zip
stundenwerte_TU_05335_akt.zip
stundenwerte_TU_05347_akt.zip
stundenwerte_TU_05349_akt.zip
stundenwerte_TU_05371_akt.zip
stundenwerte_TU_05397_akt.zip
stundenwerte_TU_05404_akt.zip
stundenwerte_TU_05424_akt.zip
stundenwerte_TU_05426_akt.zip
stundenwerte_TU_05433_akt.zip
stundenwerte_TU_05440_akt.zip
stundenwerte_TU_05480_akt.zip
stundenwerte_TU_05490_akt.zip
stundenwerte_TU_05516_akt.zip
stundenwerte_TU_05538_akt.zip
stundenwerte_TU_05541_akt.zip
stundenwerte_TU_05546_akt.zip
stundenwerte_TU_05562_akt.zip
stundenwerte_TU_05629_akt.zip
stundenwerte_TU_05640_akt.zip
stundenwerte_TU_05643_akt.zip
stundenwerte_TU_05664_akt.zip
stundenwerte_TU_05676_akt.zip
stundenwerte_TU_05688_akt.zip
stundenwerte_TU_05692_akt.zip
stundenwerte_TU_05705_akt.zip
stundenwerte_TU_05715_akt.zip
stundenwerte_TU_05717_akt.zip
stundenwerte_TU_05731_akt.zip
stundenwerte_TU_05745_akt.zip
stundenwerte_TU_05750_akt.zip
stundenwerte_TU_05779_akt.zip
stundenwerte_TU_05792_akt.zip
stundenwerte_TU_05797_akt.zip
stundenwerte_TU_05800_akt.zip
stundenwerte_TU_05822_akt.zip
stundenwerte_TU_05825_akt.zip
stundenwerte_TU_05839_akt.zip
stundenwerte_TU_05856_akt.zip
stundenwerte_TU_05871_akt.zip
stundenwerte_TU_05906_akt.zip
stundenwerte_TU_05930_akt.zip
stundenwerte_TU_05941_akt.zip
stundenwerte_TU_06093_akt.zip
stundenwerte_TU_06105_akt.zip
stundenwerte_TU_06109_akt.zip
stundenwerte_TU_06129_akt.zip
stundenwerte_TU_06157_akt.zip
stundenwerte_TU_06158_akt.zip
stundenwerte_TU_06159_akt.zip
stundenwerte_TU_06163_akt.zip
stundenwerte_TU_06170_akt.zip
stundenwerte_TU_06197_akt.zip
stundenwerte_TU_06199_akt.zip
stundenwerte_TU_06217_akt.zip
stundenwerte_TU_06258_akt.zip
stundenwerte_TU_06259_akt.zip
stundenwerte_TU_06260_akt.zip
stundenwerte_TU_06262_akt.zip
stundenwerte_TU_06263_akt.zip
stundenwerte_TU_06264_akt.zip
stundenwerte_TU_06265_akt.zip
stundenwerte_TU_06266_akt.zip
stundenwerte_TU_06272_akt.zip
stundenwerte_TU_06273_akt.zip
stundenwerte_TU_06275_akt.zip
stundenwerte_TU_06305_akt.zip
stundenwerte_TU_06310_akt.zip
stundenwerte_TU_06314_akt.zip
stundenwerte_TU_06336_akt.zip
stundenwerte_TU_06337_akt.zip
stundenwerte_TU_06344_akt.zip
stundenwerte_TU_06346_akt.zip
stundenwerte_TU_06347_akt.zip
stundenwerte_TU_07075_akt.zip
stundenwerte_TU_07099_akt.zip
stundenwerte_TU_07105_akt.zip
stundenwerte_TU_07106_akt.zip
stundenwerte_TU_07187_akt.zip
stundenwerte_TU_07298_akt.zip
stundenwerte_TU_07319_akt.zip
stundenwerte_TU_07321_akt.zip
stundenwerte_TU_07329_akt.zip
stundenwerte_TU_07330_akt.zip
stundenwerte_TU_07331_akt.zip
stundenwerte_TU_07341_akt.zip
stundenwerte_TU_07343_akt.zip
stundenwerte_TU_07350_akt.zip
stundenwerte_TU_07351_akt.zip
stundenwerte_TU_07364_akt.zip
stundenwerte_TU_07367_akt.zip
stundenwerte_TU_07368_akt.zip
stundenwerte_TU_07369_akt.zip
stundenwerte_TU_07370_akt.zip
stundenwerte_TU_07373_akt.zip
stundenwerte_TU_07374_akt.zip
stundenwerte_TU_07389_akt.zip
stundenwerte_TU_07393_akt.zip
stundenwerte_TU_07394_akt.zip
stundenwerte_TU_07395_akt.zip
stundenwerte_TU_07396_akt.zip
stundenwerte_TU_07403_akt.zip
stundenwerte_TU_07410_akt.zip
stundenwerte_TU_07412_akt.zip
stundenwerte_TU_07419_akt.zip
stundenwerte_TU_07420_akt.zip
stundenwerte_TU_07424_akt.zip
stundenwerte_TU_07427_akt.zip
stundenwerte_TU_07428_akt.zip
stundenwerte_TU_07431_akt.zip
stundenwerte_TU_07432_akt.zip
stundenwerte_TU_13670_akt.zip
stundenwerte_TU_13674_akt.zip
stundenwerte_TU_13675_akt.zip
stundenwerte_TU_13696_akt.zip
stundenwerte_TU_13700_akt.zip
stundenwerte_TU_13710_akt.zip
stundenwerte_TU_13711_akt.zip
stundenwerte_TU_13713_akt.zip
stundenwerte_TU_13777_akt.zip
stundenwerte_TU_13965_akt.zip
stundenwerte_TU_15000_akt.zip
stundenwerte_TU_15207_akt.zip
stundenwerte_TU_15444_akt.zip
stundenwerte_TU_15555_akt.zip
stundenwerte_TU_15813_akt.zip
stundenwerte_TU_19171_akt.zip
stundenwerte_TU_19172_akt.zip
stundenwerte_TU_19207_akt.zip
"""
filename_list = filename_string_raw.split("\n")
### drop empty strings
filename_list = list(filter(None, filename_list))
### identify ids from filenames
stations_id_list = []
for i in filename_list:
    stations_id_list.append(i.split("_")[2])
### change type to int
stations_id_list = list(map(int, stations_id_list))

## list of stations ids from \data\interim\df_sample_stations.csv.
### load data
df_sample = pd.read_csv(r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\data\interim\weather\df_sample_stations.csv", index_col = 0)
## sort df_sample by index
df_sample = df_sample.sort_index()

## find common ids
common_ids = list(set(stations_id_list).intersection(df_sample.index.tolist()))

len(stations_id_list)
len(df_sample)
len(common_ids)

# make new df_sample with common ids
df_sample_common = df_sample.loc[common_ids]
# Create a map object
m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

# Add marker for each station
"""marker_cluster = MarkerCluster().add_to(m)
for i in range(0, len(df_sample_common)):
    folium.Marker(
        location=[df_sample_common.iloc[i]['geobreite'], df_sample_common.iloc[i]['geolaenge']],
        popup=df_sample_common.iloc[i].name
    ).add_to(marker_cluster)"""
    
for i in range(0, len(df_sample_common)):
    folium.Marker(
        location=[df_sample_common.iloc[i]['geobreite'], df_sample_common.iloc[i]['geolaenge']],
        popup=df_sample_common.iloc[i].name
    ).add_to(m)


# Save the map
m.save(r"C:\Users\Latitude\Desktop\data_engineering\etl_renewables_weather\reports\stations_map_no_clusters.html")

import numpy as np

country_codes = {0: 'Uoplyst (1)', 5001: 'Uoplyst (2)', 5100: 'Danmark', 5101: 'Grønland', 5102: 'Udlandet uoplyst', 5103: 'Statsløs', 5104: 'Finland', 5105: 'Island, ligeret dansk', 5106: 'Island', 5107: 'Liechtenstein',  5108: 'Luxembourg', 5109: 'Monaco', 5110: 'Norge', 5114: 'Europa uoplyst',  5115: 'Kongelig', 5120: 'Sverige', 5122: 'Albanien', 5124: 'Andorra', 5126: 'Belgien', 5128: 'Bulgarien', 5129: 'Tjekkoslovakiet', 5130: 'Frankrig', 5134: 'Grækenland', 5140: 'Nederlandene', 5142: 'Irland', 5150: 'Italien', 5151: 'Serbien og Montenegro', 5152: 'Jugoslavien', 5153: 'Malta', 5154: 'Polen', 5156: 'Portugal', 5158: 'Rumænien', 5159: 'San Marino', 5160: 'Schweiz', 5162: 'Sovjetunionen', 5164: 'Spanien', 5170: 'Storbritannien', 5172: 'Tyrkiet', 5174: 'Ungarn', 5176: 'Vatikanstaten', 5180: 'Tyskland', 5182: 'Østrig', 5199: 'Europa uoplyst', 5202: 'Algeriet', 5204: 'Angola', 5207: 'Botswana', 5213: 'Burundi', 5214: 'Etiopien', 5215: 'Comorerne', 5216: 'Eritrea', 5222: 'Gambia', 5228: 'Ghana', 5230: 'Ækvatorialguinea', 5231: 'Guinea-Bissau', 5232: 'Guinea', 5233: 'Kap Verde', 5234: 'Kenya', 5235: 'Lesotho', 5236: 'Liberia', 5238: 'Libyen', 5240: 'Mozambique', 5242: 'Madagaskar', 5243: 'Mali', 5244: 'Marokko', 5245: 'Mauritius', 5246: 'Nigeria', 5247: 'Namibia', 5248: 'Marshalløerne', 5255: 'Sierra Leone', 5258: 'Sudan', 5259: 'Swaziland', 5260: 'Sydsudan', 5262: 'Sydafrika', 5266: 'Tanzania', 5268: 'Tunesien', 5269: 'Uganda', 5272: 'Egypten', 5273: 'Tuvalu', 5274: 'Kiribati', 5275: 'Vanuatu', 5276: 'Centralafrikanske Republik', 5277: 'Cameroun', 5278: 'Congo, Demokratiske Republik', 5279: 'Congo, Republikken', 5281: 'Benin', 5282: 'Elfenbenskysten', 5283: 'Gabon', 5284: 'Mauretanien', 5285: 'Niger', 5287: 'Rwanda', 5288: 'Senegal', 5289: 'Somalia', 5292: 'Tchad', 5293: 'Togo', 5294: 'Burkina Faso', 5295: 'Zimbabwe', 5296: 'Zambia', 5297: 'Malawi', 5298: 'Seychellerne', 5299: 'Afrika uoplyst', 5302: 'Argentina', 5303: 'Bahamas', 5304: 'Bolivia', 5305: 'Barbados', 5306: 'Brasilien', 5308: 'Guyana', 5309: 'Antigua og Barbuda', 5310: 'Nauru', 5311: 'Skt. Vincent og Grenadinerne', 5314: 'Canada', 5316: 'Chile', 5318: 'Colombia', 5319: 'Syd- og Mellemamerika uoplyst', 5322: 'Costa Rica', 5324: 'Cuba', 5326: 'Dominikanske Republik', 5328: 'Ecuador', 5338: 'Guatemala', 5339: 'Grenada', 5342: 'Haiti', 5344: 'Surinam', 5345: 'Dominica', 5347: 'Skt. Lucia', 5348: 'Honduras', 5352: 'Jamaica', 5354: 'Mexico', 5356: 'Nicaragua', 5358: 'Panama', 5364: 'Paraguay', 5366: 'Peru', 5372: 'El Salvador', 5374: 'Trinidad og Tobago', 5376: 'Uruguay', 5390: 'USA', 5392: 'Venezuela', 5395: 'Vestindiske Øer', 5397: 'Nordamerika uoplyst', 5398: 'Syd- og Mellemamerika uoplyst', 5402: 'Yemen', 5403: 'Forenede Arabiske Emirater', 5404: 'Afghanistan', 5406: 'Bahrain', 5408: 'Bhutan', 5410: 'Bangladesh', 5412: 'Brunei', 5414: 'Myanmar', 5416: 'Cambodja', 5418: 'Sri Lanka', 5422: 'Cypern', 5424: 'Taiwan', 5432: 'Indien', 5434: 'Indonesien', 5435: 'Østtimor', 5436: 'Irak', 5438: 'Iran', 5442: 'Israel', 5444: 'Japan', 5446: 'Jordan', 5448: 'Kina', 5452: 'Kuwait', 5454: 'Laos', 5456: 'Libanon', 5457: 'Maldiverne', 5458: 'Malaysia', 5459: 'Mongoliet', 5462: 'Oman', 5464: 'Nepal', 5466: 'Nordkorea', 5468: 'Vietnam (1)', 5471: 'Asien uoplyst', 5472: 'Pakistan', 5474: 'Filippinerne', 5478: 'Saudi-Arabien', 5482: 'Singapore', 5484: 'Sydkorea', 5486: 'Syrien', 5487: 'Mellemøsten uoplyst', 5488: 'Vietnam (2)', 5492: 'Thailand', 5496: 'Qatar', 5499: 'Asien uoplyst', 5502: 'Australien', 5505: 'Tonga', 5508: 'Fiji', 5514: 'New Zealand', 5522: 'Samoa', 5525: 'Djibouti', 5526: 'Belize', 5534: 'Papua Ny Guinea', 5599: 'Øer i Stillehavet', 5607: 'Estland', 5609: 'Letland', 5611: 'Litauen', 5621: 'Sao Tome og Principe', 5623: 'Salomonøerne', 5625: 'Skt. Kitts og Nevis', 5700: 'Rusland', 5704: 'Ukraine', 5706: 'Hviderusland', 5708: 'Armenien', 5710: 'Aserbajdsjan', 5712: 'Moldova', 5714: 'Usbekistan', 5716: 'Kasakhstan', 5718: 'Turkmenistan', 5720: 'Kirgisistan', 5722: 'Tadsjikistan', 5724: 'Georgien', 5750: 'Kroatien', 5752: 'Slovenien', 5754: 'Bosnien-Hercegovina', 5756: 'Makedonien', 5757: 'Serbien', 5758: 'Jugoslavien, Forbundsrepublikken', 5759: 'Montenegro', 5761: 'Kosovo', 5776: 'Tjekkiet', 5778: 'Slovakiet', 5779: 'Cookøerne', 5800: 'Land ukendt (2)', 5901: 'Færøerne uoplyst', 5902: 'Færøerne', 5999: 'Land ukendt (1)'}

native_english_speakers = [5170, 5228, 5234, 5236, 5246, 5255, 5303, 5305, 5308, 5309, 5311, 5314, 5339, 5345, 5347, 5352, 5374, 5390, 5502, 5514, 5526, 5625, 5779]

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 10: 'Amager Vest', 99: 'Udenfor'}

# part 2
def get_data():
    filename = './befkbhalderstatkode.csv'
    
    #Load data from a text file. Each line past the first skip_header lines is split at the delimiter character
    bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    
    return bef_stats_df

# part 3
def no_english_and_non_english():
    data = get_data()
    
    # for each country_code check if it is a navtive english speaking country
    eng_mask = [i in native_english_speakers for i in data[:,3]]
    
    # sum data from all native english speaking countries for each year
    no_english = np.array([data[(data[:,0] == n) & eng_mask][:,-1].sum() for n in list(set(data[:,0]))])
    # sum all data for each year
    
    total = np.array([data[data[:,0] == n][:,-1].sum() for n in list(set(data[:,0]))])
    no_non_english = total - no_english
    
    return no_english, no_non_english

# part 4
def filter_data(data, mask):
    return data[mask]

# part 5
def accumulated_population_of_xval(data, xkey):
    # sum data for same xkey
    data_dict = {n:data[data[:,xkey] == n][:,-1].sum() for n in list(set(data[:,xkey]))}
    
    sorted_data = sorted(list(data_dict.items()),key=lambda x:x[0])
    data2d = np.array(sorted_data)
    
    return data2d
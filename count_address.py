import pandas as pd
import datetime

meteor_nfts = pd.read_csv('http://165.22.125.123/meteor_nfts.csv ')
dust_nfts = pd.read_csv('http://165.22.125.123/meteor_dust_nfts.csv ')
egg_nfts = pd.read_csv('http://165.22.125.123/egg_nfts.csv ')
nested_egg_nfts = pd.read_csv('http://165.22.125.123/nested_egg_nfts.csv')
loot_nfts = pd.read_csv('http://165.22.125.123/loot_nfts.csv')

current_nft_dict = {'nested_egg':nested_egg_nfts, 'loot':loot_nfts, 'eggs':egg_nfts, 'meteor_dust':dust_nfts, 'meteors':meteor_nfts}

new_df = pd.read_csv('stats_headers.csv')
total_df = pd.concat([meteor_nfts, dust_nfts, egg_nfts, nested_egg_nfts, loot_nfts])
old_df = pd.read_csv('address_count_stats.csv', index_col=None)

new_list = []
for nft in current_nft_dict:
    new_list.append(pd.DataFrame({'TIMESTAMP':[datetime.datetime.now()], 'NFT':[nft], 'TOTAL_TOKEN_COUNT':[len(current_nft_dict[nft])], 'UNIQUE_ADDRESS_COUNT':[len(current_nft_dict[nft]['user_addr'].unique())]}))

new_df = pd.concat([pd.concat(new_list), pd.DataFrame({'TIMESTAMP':[datetime.datetime.now()], 'NFT':'Total', 'TOTAL_TOKEN_COUNT':[len(total_df)], 'UNIQUE_ADDRESS_COUNT':[len(total_df['user_addr'].unique())]})])
new_df = pd.concat([old_df, new_df])
new_df.to_csv('address_count_stats.csv', index=False)


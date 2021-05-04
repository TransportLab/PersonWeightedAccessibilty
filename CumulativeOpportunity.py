import pandas as pd

centroidsdf = pd.read_csv('./centroids.csv') #reading centriods file which includes names(or IDs) and opportunities on each centroid
#in this example we use jobs as the opportunities and population to measure the weighted average accessibility for all centroids
accessibilitydf = pd.DataFrame(columns=['centroids_name','PWA']) #creating an empty data frame for PWA 
source = "./traveltime_matrix.csv" #reading the OD matrix file which contains travel time between origins and destinations
ttdf = pd.read_csv(source)

threshold = 1800 #defining time threshold for generalized travel cost function

mergedf = pd.merge(ttdf,centroidsdf[['name','pop','job']],left_on=['origin'], right_on=['name'],how='left')
mergedf = pd.merge(mergedf,centroidsdf[['name','pop','job']],left_on=['destination'], right_on=['name'],how='left')
mergedf = mergedf.rename(columns={'pop_x':'origin_pop', 'pop_y':'destination_pop','job_x':'origin_job', 'job_y':'destination_job'})
mergedf['cost_function'] = mergedf['travel_time'].map(lambda x: 1 if x <= threshold else 0)
mergedf['PjFc'] = mergedf['cost_function']*mergedf['destination_job']
groupdf = mergedf.groupby(['origin']).agg({'PjFc':sum, 'origin_pop':'first'})
groupdf['PiAi'] = groupdf['origin_pop']*groupdf['PjFc']
groupdf.to_csv(('./LocationalAccessibility.csv'))
PWA = (groupdf['PiAi'].sum())/(groupdf['origin_pop'].sum())
accessibilitydf = accessibilitydf.append({'sub_name':'total', 'PWA':PWA }, ignore_index=True) #saving the locational results where PjFc shows the cumulative opportunities 
accessibilitydf.to_csv('./PWA.csv',index=False)

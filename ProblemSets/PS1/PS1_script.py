import pandas as pd
import matplotlib.pyplot as plt

natl_chunks = pd.read_csv('natl2015.csv', chunksize = 10000, 
						  iterator = True, low_memory = False)
natl = pd.concat(natl_chunks, ignore_index = True)


# descriptive statistics for Mother’s Bridged Race
mbrace_1 = len(natl[natl['mbrace']==1]) / len(natl['mbrace'])
mbrace_2 = len(natl[natl['mbrace']==2]) / len(natl['mbrace'])
mbrace_3 = len(natl[natl['mbrace']==3]) / len(natl['mbrace'])
mbrace_4 = len(natl[natl['mbrace']==4]) / len(natl['mbrace'])

# descriptive statistics for Father’s Bridged Race
fbrace_1 = len(natl[natl['fbrace']==1]) / len(natl['fbrace'])
fbrace_2 = len(natl[natl['fbrace']==2]) / len(natl['fbrace'])
fbrace_3 = len(natl[natl['fbrace']==3]) / len(natl['fbrace'])
fbrace_4 = len(natl[natl['fbrace']==4]) / len(natl['fbrace'])
fbrace_5 = len(natl[natl['fbrace']==9]) / len(natl['fbrace'])

# descriptive statistics for Mother’s Education
meduc_1 = len(natl[natl['meduc']==1]) / len(natl['meduc'])
meduc_2 = len(natl[natl['meduc']==2]) / len(natl['meduc'])
meduc_3 = len(natl[natl['meduc']==3]) / len(natl['meduc'])
meduc_4 = len(natl[natl['meduc']==4]) / len(natl['meduc'])
meduc_5 = len(natl[natl['meduc']==5]) / len(natl['meduc'])
meduc_6 = len(natl[natl['meduc']==6]) / len(natl['meduc'])
meduc_7 = len(natl[natl['meduc']==7]) / len(natl['meduc'])
meduc_8 = len(natl[natl['meduc']==8]) / len(natl['meduc'])
meduc_9 = len(natl[natl['meduc']==9]) / len(natl['meduc'])

# descriptive statistics for Father’s Education
feduc_1 = len(natl[natl['feduc']==1]) / len(natl['feduc'])
feduc_2 = len(natl[natl['feduc']==2]) / len(natl['feduc'])
feduc_3 = len(natl[natl['feduc']==3]) / len(natl['feduc'])
feduc_4 = len(natl[natl['feduc']==4]) / len(natl['feduc'])
feduc_5 = len(natl[natl['feduc']==5]) / len(natl['feduc'])
feduc_6 = len(natl[natl['feduc']==6]) / len(natl['feduc'])
feduc_7 = len(natl[natl['feduc']==7]) / len(natl['feduc'])
feduc_8 = len(natl[natl['feduc']==8]) / len(natl['feduc'])
feduc_9 = len(natl[natl['feduc']==9]) / len(natl['feduc'])

# descriptive statistics for Mother’s Age
mager_1 = len(natl[natl['mager9']==1]) / len(natl['mager9'])
mager_2 = len(natl[natl['mager9']==2]) / len(natl['mager9'])
mager_3 = len(natl[natl['mager9']==3]) / len(natl['mager9'])
mager_4 = len(natl[natl['mager9']==4]) / len(natl['mager9'])
mager_5 = len(natl[natl['mager9']==5]) / len(natl['mager9'])
mager_6 = len(natl[natl['mager9']==6]) / len(natl['mager9'])
mager_7 = len(natl[natl['mager9']==7]) / len(natl['mager9'])
mager_8 = len(natl[natl['mager9']==8]) / len(natl['mager9'])
mager_9 = len(natl[natl['mager9']==9]) / len(natl['mager9'])

# descriptive statistics for Father’s Age
fagerec_1 = len(natl[natl['fagerec11']==1]) / len(natl['fagerec11'])
fagerec_2 = len(natl[natl['fagerec11']==2]) / len(natl['fagerec11'])
fagerec_3 = len(natl[natl['fagerec11']==3]) / len(natl['fagerec11'])
fagerec_4 = len(natl[natl['fagerec11']==4]) / len(natl['fagerec11'])
fagerec_5 = len(natl[natl['fagerec11']==5]) / len(natl['fagerec11'])
fagerec_6 = len(natl[natl['fagerec11']==6]) / len(natl['fagerec11'])
fagerec_7 = len(natl[natl['fagerec11']==7]) / len(natl['fagerec11'])
fagerec_8 = len(natl[natl['fagerec11']==8]) / len(natl['fagerec11'])
fagerec_9 = len(natl[natl['fagerec11']==9]) / len(natl['fagerec11'])
fagerec_10 = len(natl[natl['fagerec11']==10]) / len(natl['fagerec11'])
fagerec_11 = len(natl[natl['fagerec11']==11]) / len(natl['fagerec11'])

# descriptive statistics for Month Prenatal Care Began Recode
precare_1 = len(natl[natl['precare5']==1]) / len(natl['precare5'])
precare_2 = len(natl[natl['precare5']==2]) / len(natl['precare5'])
precare_3 = len(natl[natl['precare5']==3]) / len(natl['precare5'])
precare_4 = len(natl[natl['precare5']==4]) / len(natl['precare5'])
precare_5 = len(natl[natl['precare5']==5]) / len(natl['precare5'])

# descriptive statistics for Marital Status
dmar_1 = len(natl[natl['dmar']==1]) / len(natl['dmar'])
dmar_2 = len(natl[natl['dmar']==2]) / len(natl['dmar'])


# plot the relationship between mother's race and prenatal care begin month
precare_white = natl[natl['mbrace']==1]['precare5'].dropna()
precare_black = natl[natl['mbrace']==2]['precare5'].dropna()
precare_indian = natl[natl['mbrace']==3]['precare5'].dropna()
precare_aisan = natl[natl['mbrace']==4]['precare5'].dropna()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.hist([precare_white, precare_black, precare_indian, precare_aisan],
		 bins=5, stacked=True, normed=True, label = ['White', 'Black',\
		 'American Indian or Alaskan Native', 'Asian or Pacific Islander'])
plt.title("The relationship between mother's race and prenatal care begin month")
ax.set_xlabel(r"Prenatal care begin month")
ax.get_yaxis().set_visible(False)

xtickvals = [1.4, 2.2, 3, 3.8, 4.6]
xticklabs = ['1st to 3rd month', '4th to 6th month', '7th to final month',\
             'No prenatal care', 'Unknown']
plt.xticks(xtickvals, xticklabs)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='best', bbox_to_anchor=(1, 0.95))


# plot mother's race info with the condition of mother's marital status
mbrace_m = natl[natl['dmar']==1]['mbrace'].dropna()
mbrace_um = natl[natl['dmar']==2]['mbrace'].dropna()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.hist([mbrace_m, mbrace_um],
		 bins=4, stacked=True, normed=True, label = ['Married', 'Unmarried'])
plt.title("Mother's race")
ax.get_yaxis().set_visible(False)

xtickvals = [1.4, 2.15, 2.85, 3.6]
xticklabs = ['White', 'Black','American Indian or Alaskan Native',\
			 'Asian or Pacific Islander']
plt.xticks(xtickvals, xticklabs)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='best', bbox_to_anchor=(1, 0.95))


# plot mother's education info with the condition of mother's marital status
meduc_m = natl[natl['dmar']==1]['meduc'].dropna()
meduc_um = natl[natl['dmar']==2]['meduc'].dropna()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.hist([meduc_m, meduc_um],
		 bins=9, stacked=True, normed=True, label = ['Married', 'Unmarried'])
plt.title("Mother's education")
ax.get_yaxis().set_visible(False)

xtickvals = [1.2, 2, 2.8, 3.7, 4.7, 5.5, 6.2, 6.9, 8.1, 9]
xticklabs = ['<= 8th grade', '9th-12th grade',\
'High school graduate', 'Some college credit',\
'Associate degree', 'Bachelor’s degree', 'Master’s degree',\
'Doctorate Degree', 'Unknown']
plt.xticks(xtickvals, xticklabs, rotation=30)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='best', bbox_to_anchor=(1, 0.95))


# plot mother's education info with the condition of mother's marital status
mager_m = natl[natl['dmar']==1]['mager9'].dropna()
mager_um = natl[natl['dmar']==2]['mager9'].dropna()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.hist([mager_m, mager_um],
		 bins=9, stacked=True, normed=True, label = ['Married', 'Unmarried'])
plt.title("Mother's age")
ax.get_yaxis().set_visible(False)

xtickvals = [1.4, 2.3, 3.2, 4.1, 5, 5.9, 6.8, 7.7, 8.6]
xticklabs = ['< 15', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44',\
			 '45-49', '50-54']
plt.xticks(xtickvals, xticklabs)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='best', bbox_to_anchor=(1, 0.95))
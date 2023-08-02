import pandas as pd 
import numpy as np
import stemgraphic
import matplotlib.pyplot as plt


smiles = pd.read_csv("smiles.txt", sep = " ", header = None, names = ["groups","scores"])

#Part One
'''
felt = smiles[smiles.groups == 'felt'] #all the groups with felt 
felt_scores = felt.iloc[:,1] #all the scores with felt
#fig_felt , ax_felt = stemgraphic.stem_graphic(felt_scores)
'''
'''
false = smiles[smiles.groups == 'false']
false_scores = false.iloc[:,1] 
#fig_false , ax_false = stemgraphic.stem_graphic(false_scores)
'''

'''
miserable = smiles[smiles.groups == 'miserable'] #all the groups with felt 
miserable_scores = miserable.iloc[:,1] #all the scores with felt
#fig_miserable , ax_miserable = stemgraphic.stem_graphic(miserable_scores)
'''

neutral = smiles[smiles.groups == 'neutral'] #all the groups with felt 
neutral_scores = neutral.iloc[:,1] #all the scores with felt
#fig_neautral , ax_neutral = stemgraphic.stem_graphic(neutral_scores)


#plt.hist(neutral_scores)

# PART TWO

#felt = np.percentile(felt_scores, [0,25,50,75,100], interpolation = 'midpoint') #[2.5, 3.5, 4.75, 5.75, 9]
#false = np.percentile(false_scores, [0,25,50,75,100], interpolation = 'midpoint') #[2.5, 3.75, 5.5, 6.5, 9]
#miserable = np.percentile(miserable_scores, [0,25,50,75,100], interpolation = 'midpoint') #[2.5, 4, 4.75, 5.5, 8]
#neutral = np.percentile(neutral_scores, [0,25,50,75,100], interpolation = 'midpoint') #[2, 3, 4, 4.75, 8]

plt.boxplot(neutral_scores)

plt.show()
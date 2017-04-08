
# coding: utf-8

# In[102]:

import nbimporter
import pandas as pd
import numpy as np
import re
import shutil
import NetworkAnalysisCode as nac
# from NetworkAnalysisCode import NetworkAnalysis
# from NetworkAnalysisCode import Make_Graph
reload(nac)


# In[103]:


data=pd.read_csv("tweets.csv",usecols=["username","tweets"])


obj= nac.NetworkAnalysis()
nodes,edges=obj.Extract_Username_And_Edges(data)


# In[97]:

# for i in nodes:
#     print i


# In[98]:

# for i in edges:
#     print i


# In[106]:

Graph,UsernameMapping=obj.Make_Graph(nodes,edges)

InverseUsernameMapping = {v: k for k, v in UsernameMapping.iteritems()}

# for i in range(0,2865):
#     for j in range(0,2865):
#         if Graph[i][j]>100 :
# #             print str(i)+" -> "+str(j)
#             print InverseUsernameMapping[i]+" -> "+InverseUsernameMapping[j]
                

obj.Languages_Used(np.array(data["tweets"]))
obj.Most_Active_Users(data)
obj.Actual_And_Retweets(data)
obj.Most_Mentioned_Users(Graph,InverseUsernameMapping)



# In[105]:

obj.Languages_Used(np.array(data["tweets"]))


# In[101]:

obj.Most_Active_Users(data)
obj.Actual_And_Retweets(data)
obj.Most_Mentioned_Users(Graph,InverseUsernameMapping)



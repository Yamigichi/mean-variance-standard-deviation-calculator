import numpy as np

def calculate(list):
  #Exeption message
  if(len(list)!=9):
    raise ValueError("List must contain nine numbers. ")

#Numpy array
  ls = np.array(list)
  print(ls)

  #Mean
  meanRows = [ls[[0,1,2]].mean(), ls[[3,4,5,]].mean(), ls[[6,7,8]].mean()]
  meanColumns = ([ls[[0,3,6]].mean(),ls[[1,4,7]].mean(), ls[[2,5,8]].mean()])

  #Variance
  varianceRows = [ls[[0,1,2]].var(), ls[[3,4,5,]].var(), ls[[6,7,8]].var()]
  varianceColumns = ([ls[[0,3,6]].var(),ls[[1,4,7]].var(), ls[[2,5,8]].var()])

  #Standard Deviation
  standardDeviationRows = [ls[[0,1,2]].std(), ls[[3,4,5,]].std(), ls[[6,7,8]].std()]
  standardDeviationColumns = ([ls[[0,3,6]].std(),ls[[1,4,7]].std(), ls[[2,5,8]].std()])

  #Max
  maxRows = [ls[[0,1,2]].max(), ls[[3,4,5,]].max(), ls[[6,7,8]].max()]
  maxColumns = ([ls[[0,3,6]].max(),ls[[1,4,7]].max(), ls[[2,5,8]].max()])

  #Min
  minRows = [ls[[0,1,2]].min(), ls[[3,4,5,]].min(), ls[[6,7,8]].min()]
  minColumns = ([ls[[0,3,6]].min(),ls[[1,4,7]].min(), ls[[2,5,8]].min()])

  #Sum
  sumRows = [ls[[0,1,2]].sum(), ls[[3,4,5,]].sum(), ls[[6,7,8]].sum()]
  sumColumns = ([ls[[0,3,6]].sum(),ls[[1,4,7]].sum(), ls[[2,5,8]].sum()])

  return {
    'mean': [meanColumns, meanRows, ls.mean()],
    'variance': [varianceColumns, varianceRows, ls.var()],
    'standard deviation': [standardDeviationColumns, standardDeviationRows, ls.std()],
    'max': [maxColumns, maxRows, ls.max()],
    'min': [minColumns, minRows, ls.min()],
    'sum': [sumColumns, sumRows, ls.sum()]
  }

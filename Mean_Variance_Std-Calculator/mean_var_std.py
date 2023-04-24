import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    m_list = np.reshape(list, (3, 3))
    meanc = np.mean(m_list, axis = 0).tolist()
    meanr = np.mean(m_list, axis = 1).tolist()
    meanf = np.mean(list).tolist()
    #meanv = [axis1, axis2, flattened]

    varc = np.var(m_list, axis = 0).tolist()
    varr = np.var(m_list, axis = 1).tolist()
    varf = np.var(list).tolist()
    #variancev = [axis1, axis2, flattened]
    #print('variance: ', variancev)

    stdc = np.std(m_list, axis = 0).tolist()
    stdr = np.std(m_list, axis = 1).tolist()
    stdf = np.std(list).tolist()
    #standard_deviation = [axis1, axis2, flattened]
    #print('standard deviation: ', standard_deviation)

    maxc = np.max(m_list, axis = 0).tolist()
    maxr = np.max(m_list, axis = 1).tolist()
    maxf = np.max(list).tolist()
    #maxi = [axis1, axis2, flattened]
    #print('max: ', maxi)

    minc = np.min(m_list, axis = 0).tolist()
    minr = np.min(m_list, axis = 1).tolist()
    minf = np.min(list).tolist()
    #mini = [axis1, axis2, flattened]
    #print('mean: ', mini)

    sumc = np.sum(m_list, axis = 0).tolist()
    sumr = np.sum(m_list, axis = 1).tolist()
    sumf = np.sum(list).tolist()
    #sumy = [axis1, axis2, flattened]
    #print('sum: ', sum)

    calculations = {
        "mean": [meanc, meanr, minf],
        "variance": [varc, varr,varf],
        "standard deviation": [stdc, stdr, stdf],
        "max": [maxc, maxr, maxf],
        "min": [minc, minr, minf],
        "sum": [sumc, sumr, sumf]
    }
    return calculations
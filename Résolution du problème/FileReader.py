# -*- coding: utf-8 -*-
import numpy as np
"""
@author: Amadéo DAVID
@date  : Sun May 12 12:35:46 2019
"""

def readFile(file_name):
    """
    Cette fonction lit un fichier formatté au type utilise dans les exemples du
    projet
    @pre                : Le fichier file_name est organise de la meme maniere
                          que les exemples donnes sur Moodle.
    
    @param file_name    : contient un String avec le nom du fichier a lire.
    
    @return n_points    : Contient un 'int' avec le nombre de points
    @return n_conduites : Contient un 'int' avec le nombre de conduites
    @return X           : Contient un 'numpy.array' avec les abscisses des points.
    @return Y           : Contient un 'numpy.array' avec les ordonnees des points.
    @return Z           : Contient un 'numpy.array' avec la hauteur des points.
    @return A           : Contient un 'numpy.array' avec la matrice d'incidence
                          des conduites.
    @return alpha       : Contient un 'float' avecla valeur de alpha.
    @return R           : Contient un 'float' avec le rayon des conduites.
    @return pa          : Contient un 'numpy.array' avec les points
                          d'approvisionnement.
    @return da_max      : Contient un 'numpy.array' avec les debits maximaux
                          extractibles.
    @return C           : Contient un 'numpy.array' avec les couts d'extraction.
    @return pc          : Contient un 'numpy.array' avec les points de
                          consommation.
    @return dc_min      : Contient un 'numpy.array' avec les debits minimaux
                          consommables.
    @return dc_max      : Contient un 'numpy.array' avec les debits maximaux
                          consommables.
    @return Pf          : Contient un 'float' avec le prix facture.
    @return pi          : Contient un 'numpy.array' avec les points
                          intermediaires.
    @return unit        : Contient un 'String' avec l'unite des coordonnes des
                          points.
    """
    with open(file_name,'r') as f:
        n_points    = (int)(f.readline().split()[0])
        n_conduites = (int)(f.readline().split()[0])
        f.readline()
        unit        = (f.readline().split(" = ")[1])
        
        coord       = np.array(list(list(float(w) for w in f.readline().split()[:]) for i in range(n_points)))
        X           = coord[:,0]
        Y           = coord[:,1]
        Z           = coord[:,2]
        
        f.readline()
        f.readline()
        A           = np.array(list(list(float(w) for w in f.readline().split()[:]) for i in range(n_points)))
        f.readline()
        
        UL_alpha    = f.readline().split(" = ")[1]
        UL_alpha    = UL_alpha.split()[0]
        UL2_alpha   = np.array(UL_alpha.split("^"))
        if(len(UL2_alpha) == 1):
            alpha   = (float)(UL2_alpha)
        else:
            alpha   = (float)(UL2_alpha[0]) ** (float)(UL2_alpha[1])
        
        R           = (float)(f.readline().split()[4])
        f.readline()
        
        UL_pa       = f.readline().split(" = [")[1]
        UL_pa       = UL_pa.split("]")[0]
        pa          = np.array(list(float(w) for w in UL_pa.split()[:]))
        
        UL_da_max   = f.readline().split(" = [")[1]
        UL_da_max   = UL_da_max.split("]")[0]
        da_max      = np.array(list(float(w) for w in UL_da_max.split()[:]))
        
        UL_C        = f.readline().split(" = [")[1]
        UL_C        = UL_C.split("]")[0]
        C           = np.array(list(float(w) for w in UL_C.split()[:]))
        
        f.readline()
        
        UL_pc       = f.readline().split(" = [")[1]
        UL_pc       = UL_pc.split("]")[0]
        pc          = np.array(list(float(w) for w in UL_pc.split()[:]))
        
        UL_dc_min   = f.readline().split(" = [")[1]
        UL_dc_min   = UL_dc_min.split("]")[0]
        dc_min      = np.array(list(float(w) for w in UL_dc_min.split()[:]))
        
        UL_dc_max   = f.readline().split(" = [")[1]
        UL_dc_max   = UL_dc_max.split("]")[0]
        dc_max      = np.array(list(float(w) for w in UL_dc_max.split()[:]))
        
        Pf          = (float)(f.readline().split()[3])
        
        f.readline()
        
        UL_pi       = f.readline().split("[")[1]
        UL_pi       = UL_pi.split("]")[0]
        pi          = np.array(list(float(w) for w in UL_pi.split()[:]))
        
    return (n_points, n_conduites, X, Y, Z, A, alpha, R, pa, da_max, C, pc, dc_min, dc_max, Pf, pi, unit)
    

filename = "Mini-exemple-avec-solution/Data-mini-exemple-avec-solution.txt"
aka = readFile(filename)
for w in aka:
    print(w)

#String = "1 2 3 4 5 6 7"
#list(float(w) for w in f.readline().split()[:])
#list(float(w) for w in String.split()[:])